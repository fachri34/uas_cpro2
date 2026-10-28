import pytest

from feature.daftar_matkul import lihat_daftar  # sesuaikan nama modulnya


def buat_daftar():
    """Daftar mata kuliah baru untuk setiap test."""
    return [
        {"nama": "Kalkulus", "sks": 3, "nilai": "A", "bobot": 4.0, "poin": 12.0},
        {"nama": "Fisika", "sks": 2, "nilai": "B", "bobot": 3.0, "poin": 6.0},
        {"nama": "Algoritma", "sks": 4, "nilai": "B+", "bobot": 3.5, "poin": 14.0},
    ]


def test_daftar_kosong(capsys):
    lihat_daftar([])

    output = capsys.readouterr().out
    assert "--- DAFTAR MATA KULIAH ---" in output
    assert "Belum ada mata kuliah." in output
    assert "No | Nama Mata Kuliah" not in output
    assert "Total SKS" not in output


def test_menampilkan_header_dan_garis(capsys):
    lihat_daftar(buat_daftar())

    output = capsys.readouterr().out
    assert "No | Nama Mata Kuliah | SKS | Nilai | Bobot | Poin" in output
    # Garis pemisah dicetak dua kali (sebelum dan sesudah baris data)
    assert output.count("-" * 60) == 2
    assert "Belum ada mata kuliah." not in output


def test_menampilkan_semua_baris_data(capsys):
    lihat_daftar(buat_daftar())

    output = capsys.readouterr().out
    assert "1 | Kalkulus | 3 | A | 4.0 | 12.0" in output
    assert "2 | Fisika | 2 | B | 3.0 | 6.0" in output
    assert "3 | Algoritma | 4 | B+ | 3.5 | 14.0" in output


def test_urutan_baris_sesuai_daftar(capsys):
    lihat_daftar(buat_daftar())

    output = capsys.readouterr().out
    assert output.index("Kalkulus") < output.index("Fisika") < output.index("Algoritma")


def test_total_sks_dan_poin(capsys):
    # SKS: 3 + 2 + 4 = 9 ; Poin: 12.0 + 6.0 + 14.0 = 32.0
    lihat_daftar(buat_daftar())

    output = capsys.readouterr().out
    assert "Total SKS : 9 SKS | Total Poin : 32.0" in output


def test_satu_mata_kuliah(capsys):
    daftar_mk = [{"nama": "Kalkulus", "sks": 3, "nilai": "A", "bobot": 4.0, "poin": 12.0}]

    lihat_daftar(daftar_mk)

    output = capsys.readouterr().out
    assert "1 | Kalkulus | 3 | A | 4.0 | 12.0" in output
    assert "Total SKS : 3 SKS | Total Poin : 12.0" in output


def test_tidak_mengubah_daftar(capsys):
    daftar_mk = buat_daftar()

    lihat_daftar(daftar_mk)

    assert daftar_mk == buat_daftar()  # Pastikan daftar_mk tetap sama setelah fungsi dijalankan