import pytest

from feature.hapus_mk import hapus_mk  # sesuaikan nama modulnya


def buat_daftar():
    """Daftar mata kuliah baru untuk setiap test."""
    return [
        {"nama": "Kalkulus", "sks": 3, "nilai": "A", "bobot": 4.0, "poin": 12.0},
        {"nama": "Fisika", "sks": 2, "nilai": "B", "bobot": 3.0, "poin": 6.0},
        {"nama": "Algoritma", "sks": 4, "nilai": "B+", "bobot": 3.5, "poin": 14.0},
    ]


def isi_input(monkeypatch, daftar_jawaban):
    """Mengganti input() dengan jawaban berurutan."""
    jawaban = iter(daftar_jawaban)
    monkeypatch.setattr("builtins.input", lambda _: next(jawaban))


def test_daftar_kosong(capsys):
    daftar_mk = []

    hapus_mk(daftar_mk)

    output = capsys.readouterr().out
    assert "Belum ada mata kuliah untuk dihapus." in output
    assert daftar_mk == []


def test_menampilkan_daftar_mata_kuliah(monkeypatch, capsys):
    daftar_mk = buat_daftar()
    isi_input(monkeypatch, ["0"])

    hapus_mk(daftar_mk)

    output = capsys.readouterr().out
    assert "1 . Kalkulus ( 3 SKS, Nilai A )" in output