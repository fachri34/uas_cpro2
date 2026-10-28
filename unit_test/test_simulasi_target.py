import pytest

from feature.target_simulasi import simulasi_target  # sesuaikan nama modulnya


def buat_mk(sks, poin):
    """Helper kecil untuk membuat data mata kuliah."""
    return {"nama": "MK", "sks": sks, "nilai": "-", "bobot": poin / sks, "poin": poin}


def isi_input(monkeypatch, daftar_jawaban):
    """Mengganti input() dengan jawaban berurutan."""
    jawaban = iter(daftar_jawaban)
    monkeypatch.setattr("builtins.input", lambda _: next(jawaban))


# ---------- Ada data mata kuliah (hanya minta sisa SKS dan target) ----------

def test_data_saat_ini_diambil_dari_daftar(monkeypatch, capsys):
    # 6 SKS, 21 poin -> IPK 3.50
    daftar_mk = [buat_mk(3, 12.0), buat_mk(3, 9.0)]
    isi_input(monkeypatch, ["6", "3.0"])  # sisa SKS, target IPK

    simulasi_target(daftar_mk)

    output = capsys.readouterr().out
    assert "Data saat ini: IPK 3.50 | SKS Selesai: 6 SKS" in output


def test_target_bisa_dicapai(monkeypatch, capsys):
    # (3.0 * 12 - 21) / 6 = 2.50
    daftar_mk = [buat_mk(3, 12.0), buat_mk(3, 9.0)]
    isi_input(monkeypatch, ["6", "3.0"])

    simulasi_target(daftar_mk)

    output = capsys.readouterr().out
    assert "BISA DICAPAI!" in output
    assert "Rata-rata Nilai Dibutuhkan: 2.50 (pada 6 SKS tersisa)" in output
    assert "minimal 2.50" in output


def test_target_tepat_di_batas_nilai_a(monkeypatch, capsys):
    # (3.75 * 12 - 21) / 6 = 4.00 -> masih bisa dicapai (tidak > 4.0)
    daftar_mk = [buat_mk(3, 12.0), buat_mk(3, 9.0)]
    isi_input(monkeypatch, ["6", "3.75"])

    simulasi_target(daftar_mk)

    output = capsys.readouterr().out
    assert "BISA DICAPAI!" in output
    assert "Rata-rata Nilai Dibutuhkan: 4.00" in output


def test_target_tidak_mungkin_dicapai(monkeypatch, capsys):
    # (4.0 * 12 - 21) / 6 = 4.50 > 4.0; IPK maks = (21 + 24) / 12 = 3.75
    daftar_mk = [buat_mk(3, 12.0), buat_mk(3, 9.0)]
    isi_input(monkeypatch, ["6", "4.0"])

    simulasi_target(daftar_mk)

    output = capsys.readouterr().out
    assert "TIDAK MUNGKIN DICAPAI!" in output
    assert "Butuh rata-rata 4.50" in output
    assert "IPK Maksimal yang Mungkin : 3.75" in output
    assert "Jika seluruh 6 SKS sisa mendapat nilai A" in output
    assert "BISA DICAPAI!" not in output


@pytest.mark.parametrize("target", ["2.0", "0.0"])
def test_target_sudah_aman(monkeypatch, capsys, target):
    # IPK 4.00 (6 SKS, 24 poin).
    # target 2.0 -> (24 - 24) / 6 = 0 (tepat nol), target 0.0 -> -4.0 (negatif)
    daftar_mk = [buat_mk(3, 12.0), buat_mk(3, 12.0)]
    isi_input(monkeypatch, ["6", target])

    simulasi_target(daftar_mk)

    output = capsys.readouterr().out
    assert "TARGET SUDAH AMAN TERCAPAI!" in output
    assert "BISA DICAPAI!" not in output
    assert "TIDAK MUNGKIN DICAPAI!" not in output


def test_sisa_sks_nol_menghentikan_simulasi(monkeypatch, capsys):
    daftar_mk = [buat_mk(3, 12.0)]
    isi_input(monkeypatch, ["0"])  # hanya satu input; target tidak ditanya

    simulasi_target(daftar_mk)

    output = capsys.readouterr().out
    assert "Sisa SKS tidak boleh 0 untuk melakukan simulasi." in output
    assert "HASIL SIMULASI" not in output


# ---------- Daftar kosong (SKS dan IPK diinput manual) ----------

def test_mahasiswa_baru(monkeypatch, capsys):
    # SKS selesai 0, IPK 0, sisa 144, target 3.5 -> butuh rata-rata 3.50
    isi_input(monkeypatch, ["0", "0", "144", "3.5"])

    simulasi_target([])

    output = capsys.readouterr().out
    assert "Data saat ini" not in output
    assert "BISA DICAPAI!" in output
    assert "Rata-rata Nilai Dibutuhkan: 3.50 (pada 144 SKS tersisa)" in output


def test_input_manual_sks_dan_ipk(monkeypatch, capsys):
    # 60 SKS, IPK 3.0, sisa 60, target 3.5 -> (420 - 180) / 60 = 4.00
    isi_input(monkeypatch, ["60", "3.0", "60", "3.5"])

    simulasi_target([])

    output = capsys.readouterr().out
    assert "BISA DICAPAI!" in output
    assert "Rata-rata Nilai Dibutuhkan: 4.00 (pada 60 SKS tersisa)" in output


def test_validasi_semua_input(monkeypatch, capsys):
    isi_input(
        monkeypatch,
        [
            "-5", "abc", "0",     # SKS selesai: minus, bukan angka, valid
            "-1", "x", "0",       # IPK: minus, bukan angka, valid
            "-3", "abc", "10",    # sisa SKS: minus, bukan angka, valid
            "5", "abc", "2.0",    # target: di luar 0-4, bukan angka, valid
        ],
    )

    simulasi_target([])

    output = capsys.readouterr().out
    assert output.count("Angka tidak boleh minus.") == 3
    assert output.count("Input tidak valid! Harap masukkan angka.") == 4
    assert "Target IPK harus di antara 0.0 sampai 4.0" in output
    # (2.0 * 10 - 0) / 10 = 2.00
    assert "Rata-rata Nilai Dibutuhkan: 2.00 (pada 10 SKS tersisa)" in output