# 🎓 TargetIPK - Kalkulator & Simulasi Target IPK Mahasiswa

Aplikasi berbasis Python Command-Line Interface (CLI) untuk membantu mahasiswa mengelola nilai mata kuliah, menghitung Indeks Prestasi Kumulatif (IPK), mengetahui predikat akademik, dan menyimulasikan target IPK hingga lulus.

Proyek ini dikerjakan untuk memenuhi tugas pemrograman (Intro to Computer Programming) oleh **Kelompok 4**.

🔗 **Link Repository:** [https://github.com/fachri34/uas_cpro2.git](https://github.com/fachri34/uas_cpro2.git)

---

## 🎯 Tujuan Proyek

- Membantu mahasiswa menghitung IPK berdasarkan SKS dan nilai mata kuliah.
- Menampilkan ringkasan performa akademik mahasiswa dengan visualisasi *progress bar*.
- Memberikan simulasi nilai rata-rata yang dibutuhkan untuk mencapai target IPK akhir.
- Menerapkan konsep pemrograman Python seperti modularisasi, manipulasi list/dictionary, percabangan, perulangan, validasi *input*, dan *unit testing*.

---

## ✨ Fitur Utama

### 1. ➕ Tambah Mata Kuliah
Pengguna memasukkan nama mata kuliah, jumlah SKS (1-6), dan nilai huruf (A-E). Program melakukan validasi menggunakan blok `try-except` agar aplikasi tidak *error* jika pengguna memasukkan tipe data yang salah.
### 2. 📋 Lihat Daftar Mata Kuliah
Menampilkan seluruh mata kuliah yang telah disimpan dalam bentuk tabel yang rapi, lengkap dengan rincian SKS, Bobot, dan Poin, beserta akumulasi Total SKS dan Total Poin.
### 3. 📊 Hitung IPK & Predikat Saat Ini
Menghitung IPK berdasarkan rumus `Total Poin / Total SKS`, menentukan predikat kelulusan (*Cum Laude*, Sangat Memuaskan, dll.), dan menampilkan *progress bar* pencapaian terhadap skala maksimum 4.00.
### 4. 🎯 Simulasi Target IPK
Menghitung **Nilai Rata-rata yang Dibutuhkan** pada sisa SKS untuk mencapai target IPK. Fitur ini akan memberikan peringatan batas IPK maksimal jika target yang diincar mustahil dicapai (membutuhkan rata-rata nilai > 4.00).
### 5. 🗑️ Hapus Mata Kuliah
Menghapus data mata kuliah secara spesifik dan dinamis berdasarkan nomor urut dari dalam tabel menggunakan metode `.pop()`.

---

## 👥 Tim Pengembang (Kelompok 4)

Proyek ini menggunakan arsitektur modular, di mana tugas dibagi berdasarkan fitur di folder `feature/`:

*   **Daniel (26121600005) - Ketua**
    *   Kerangka utama program (`main.py`) dan sistem *looping* menu utama.
    *   Logika **Menu 4 (Simulasi Target IPK)** di `feature/target_simulasi.py`.
*   **Riesya Fachri Rofi (26121600017)**
    *   Logika **Menu 1 (Tambah Mata Kuliah)** beserta validasi *input* di `feature/add_matkul.py`.
*   **Jason Sinar Isac Saputra (26121600013)**
    *   Logika perhitungan dan visualisasi **Menu 3 (Hitung IPK)** di `feature/hitung_ipk.py`.
*   **Imam Maulana Ramadhan (26121600014)**
    *   Pengembangan antarmuka **Menu 2 (Lihat Daftar)** di `feature/daftar_matkul.py` dan **Menu 5 (Hapus Matkul)** di `feature/hapus_mk.py`.

---

## 📁 Struktur Proyek

```text
TargetIPK/
├── main.py                  # Inisialisasi aplikasi dan Menu Utama
├── feature/                 # Folder modul fitur-fitur utama
│   ├── add_matkul.py
│   ├── daftar_matkul.py
│   ├── hitung_ipk.py
│   ├── target_simulasi.py
│   └── hapus_mk.py
├── unit_test/                 # Folder modul unit test fitur utama
│   ├── test_add_matkul.py
|   ├── test_hapus_mk.py
│   ├── test_lihat_daftar.py
│   ├── test_simulasi_target.py
│   ├── test_tampilkan_ipk.py
└── README.md
└── .gitignore
```

---

## 📊 Skala Nilai & Predikat Akademik

**Skala Bobot Poin:**
`A = 4.0` | `B+ = 3.5` | `B = 3.0` | `C+ = 2.5` | `C = 2.0` | `D = 1.0` | `E = 0.0`

**Aturan Predikat:**
*   **Cum Laude:** IPK ≥ 3.50
*   **Sangat Memuaskan:** IPK ≥ 3.00
*   **Memuaskan:** IPK ≥ 2.50
*   **Cukup:** IPK ≥ 2.00
*   **Perlu Ditingkatkan:** IPK < 2.00

---

## 🚀 Cara Menjalankan Program

### 1. Menjalankan Aplikasi Utama
Aplikasi ini hanya membutuhkan Python bawaan (Python 3.6+). Tidak perlu instalasi *library* tambahan untuk menjalankan fitur utama.
1. *Clone repository*: `git clone https://github.com/fachri34/uas_cpro2.git`
2. Masuk ke direktori: `cd uas_cpro2` (atau direktori terkait)
3. Jalankan aplikasi:
   ```bash
   python main.py
   ```

### 2. Menjalankan Unit Test (Pengujian)
Proyek ini mengadopsi *Test-Driven Development* secara parsial dengan `pytest` menggunakan bantuan `monkeypatch` dan `capsys` untuk menguji *input/output* terminal secara otomatis.
1. *Install* pytest (jika belum ada):
   ```bash
   pip install pytest
   ```
2. Jalankan semua *test*:
   ```bash
   pytest
   ```
   Atau untuk *output* yang lebih detail:
   ```bash
   pytest -v
   ```

---
*Dibuat dengan 💡 oleh Kelompok 4.*
