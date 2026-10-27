def tambah_mk(daftar_mk, SKALA_NILAI):
    print("\n=== Tambah Mata Kuliah ===")

    # 1. Input dan Validasi Nama Mata Kuliah
    while True:
        nama = input("Masukkan nama mata kuliah: ").strip().title()
        if nama != "":  # Apakah nama tidak kosong?
            break
        print("[!] Nama tidak boleh kosong!")

    # 2. Input dan Validasi SKS
    while True:
        try:
            sks_input = input("Masukkan jumlah SKS: ")
            sks = int(sks_input)
            if 1 <= sks <= 6:  # Apakah 1 <= sks <= 6?
                break
            else:
                print("[!] SKS harus angka 1 sampai 6!")
        except ValueError:
            print("[!] SKS harus berupa angka bulat!")

    # 3. Input dan Validasi Nilai
    while True:
        nilai = input("Masukkan nilai (A, B+, B, C+, C, D, E): ").strip().upper()
        if nilai in SKALA_NILAI:  # Apakah nilai ada di dalam SKALA_NILAI?
            break
        print("[!] Nilai tidak valid! Gunakan A, B+, B, C+, C, D, atau E")

    # 4. Proses Perhitungan & Penyimpanan Data
    bobot = SKALA_NILAI[nilai]
    poin = sks * bobot

    matkul = {
        'nama': nama,
        'sks': sks,
        'nilai': nilai,
        'bobot': bobot,
        'poin': poin
    }

    daftar_mk.append(matkul)

    # 5. Output Sukses & Kembali ke Menu Utama
    print(f"[OK] Berhasil menambahkan: {nama} ({sks} SKS, Nilai {nilai}, Poin {poin})")
    print("Kembali ke Menu Utama\n")



