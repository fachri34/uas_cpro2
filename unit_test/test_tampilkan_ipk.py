import pytest

from feature.hitung_ipk import tampilkan_ipk  # sesuaikan nama modulnya


def buat_mk(sks, poin):
    """Helper kecil untuk membuat data mata kuliah."""
    return {"nama": "MK", "sks": sks, "nilai": "-", "bobot": poin / sks, "poin": poin}


def test_daftar_kosong(capsys):
    tampilkan_ipk([])

    output = capsys.readouterr().out
    assert "Belum ada mata kuliah untuk dihitung" in output
    assert "IPK Saat Ini" not in output


def test_satu_matkul_nilai_a(capsys):
    daftar_mk = [buat_mk(3, 12.0)]

    tampilkan_ipk(daftar_mk)

    output = capsys.readouterr().out
    assert "Total SKS Selesai : 3 SKS" in output
    assert "Total Poin Mutu   : 12.00" in output
    assert "IPK Saat Ini      : 4.00 / 4.00" in output
    assert "[" + "#" * 20 + "] 100.0%" in output
    assert "Predikat Saat Ini : Cum Laude" in output


def test_beberapa_matkul(capsys):
    # A (3 SKS) = 12, B (3 SKS) = 9, C+ (2 SKS) = 5 -> 8 SKS, 26 poin, IPK 3.25
    daftar_mk = [buat_mk(3, 12.0), buat_mk(3, 9.0), buat_mk(2, 5.0)]

    tampilkan_ipk(daftar_mk)

    output = capsys.readouterr().out
    assert "Total SKS Selesai : 8 SKS" in output
    assert "Total Poin Mutu   : 26.00" in output
    assert "IPK Saat Ini      : 3.25 / 4.00" in output
    assert "[" + "#" * 16 + "-" * 4 + "]" in output
    assert "Predikat Saat Ini : Sangat Memuaskan" in output


@pytest.mark.parametrize(
    "ipk, predikat",
    [
        (4.00, "Cum Laude"),
        (3.50, "Cum Laude"),               # batas bawah Cum Laude
        (3.49, "Sangat Memuaskan"),
        (3.00, "Sangat Memuaskan"),        # batas bawah Sangat Memuaskan
        (2.99, "Memuaskan"),
        (2.50, "Memuaskan"),               # batas bawah Memuaskan
        (2.49, "Cukup"),
        (2.00, "Cukup"),                   # batas bawah Cukup
        (1.99, "Perlu Ditingkatkan"),
        (0.00, "Perlu Ditingkatkan"),
    ],
)
def test_predikat_berdasarkan_ipk(capsys, ipk, predikat):
    # 1 SKS sehingga poin = IPK
    tampilkan_ipk([buat_mk(1, ipk)])

    output = capsys.readouterr().out
    assert f"Predikat Saat Ini : {predikat}" in output


def test_progress_bar_separuh(capsys):
    tampilkan_ipk([buat_mk(1, 2.0)])  # IPK 2.0 -> 50%

    output = capsys.readouterr().out
    assert "[" + "#" * 10 + "-" * 10 + "] 50.0%" in output


def test_progress_bar_kosong(capsys):
    tampilkan_ipk([buat_mk(3, 0.0)])  # IPK 0.0 -> 0%

    output = capsys.readouterr().out
    assert "[" + "-" * 20 + "] 0.0%" in output
    assert "Predikat Saat Ini : Perlu Ditingkatkan" in output