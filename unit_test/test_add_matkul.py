import pytest

from feature.add_matkul import tambah_mk


SKALA_NILAI_TEST = {
    "A": 4.0,
    "B+": 3.5,
    "B": 3.0,
    "C+": 2.5,
    "C": 2.0,
    "D": 1.0,
    "E": 0.0,
}


def test_tambah_matkul_dengan_nilai_a(monkeypatch):
    daftar_mk = []

    # Urutan input: nama, SKS, nilai.
    jawaban = iter(["Discrete Mathematics", "3", "A"])
    monkeypatch.setattr("builtins.input", lambda _: next(jawaban))

    tambah_mk(daftar_mk, SKALA_NILAI_TEST)

    assert len(daftar_mk) == 1
    assert daftar_mk[0]["nama"] == "Discrete Mathematics"
    assert daftar_mk[0]["sks"] == 3
    assert daftar_mk[0]["nilai"] == "A"
    assert daftar_mk[0]["bobot"] == 4.0
    assert daftar_mk[0]["poin"] == 12.0