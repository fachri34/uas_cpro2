def simulasi_target(daftar_mk):
    """Menu 4: Simulasi Target IPK (semua logika dalam satu fungsi)."""
    print("\n--- SIMULASI TARGET IPK ---")

    # 1. Ambil data saat ini
    if len(daftar_mk) > 0:
        sks_selesai = sum(mk['sks'] for mk in daftar_mk)
        total_poin = sum(mk['poin'] for mk in daftar_mk)
        ipk_sekarang = total_poin / sks_selesai if sks_selesai > 0 else 0.0
        print(f"Data saat ini: IPK {ipk_sekarang:.2f} | SKS Selesai: {sks_selesai} SKS")
    else:
        while True:
            try:
                sks_selesai = int(input("Masukkan SKS selesai saat ini (isi 0 jika mahasiswa baru): "))
                if sks_selesai >= 0:
                    break
                print("[!] Angka tidak boleh minus.")
            except ValueError:
                print("[!] Input tidak valid! Harap masukkan angka.")

        while True:
            try:
                ipk_sekarang = float(input("Masukkan IPK saat ini (isi 0 jika mahasiswa baru): "))
                if ipk_sekarang >= 0:
                    break
                print("[!] Angka tidak boleh minus.")
            except ValueError:
                print("[!] Input tidak valid! Harap masukkan angka.")

    # 2. Input sisa SKS
    while True:
        try:
            sks_sisa = int(input("Masukkan sisa SKS hingga lulus: "))
            if sks_sisa >= 0:
                break
            print("[!] Angka tidak boleh minus.")
        except ValueError:
            print("[!] Input tidak valid! Harap masukkan angka.")

    if sks_sisa == 0:
        print("[!] Sisa SKS tidak boleh 0 untuk melakukan simulasi.")
        return

    # 3. Input target IPK
    while True:
        try:
            target_ipk = float(input("Masukkan Target IPK Akhir (0-4): "))
            if 0.0 <= target_ipk <= 4.0:
                break
            print("[!] Target IPK harus di antara 0.0 sampai 4.0")
        except ValueError:
            print("[!] Input tidak valid! Harap masukkan angka.")

    # 4. Hitung rata-rata nilai yang dibutuhkan
    poin_saat_ini = ipk_sekarang * sks_selesai
    poin_target = target_ipk * (sks_selesai + sks_sisa)
    nilai_dibutuhkan = (poin_target - poin_saat_ini) / sks_sisa

    # 5. Tampilkan hasil
    print("\n--- HASIL SIMULASI ---")
    if nilai_dibutuhkan > 4.0:
        ipk_maks = (poin_saat_ini + sks_sisa * 4.0) / (sks_selesai + sks_sisa)
        print("Status Target             : TIDAK MUNGKIN DICAPAI!")
        print(f"Alasan                    : Butuh rata-rata {nilai_dibutuhkan:.2f} (Melebihi batas nilai A = 4.00).")
        print(f"IPK Maksimal yang Mungkin : {ipk_maks:.2f} (Jika seluruh {sks_sisa} SKS sisa mendapat nilai A).")
    elif 0 < nilai_dibutuhkan <= 4.0:
        print("Status Target             : BISA DICAPAI!")
        print(f"Rata-rata Nilai Dibutuhkan: {nilai_dibutuhkan:.2f} (pada {sks_sisa} SKS tersisa)")
        print(f"Gambaran Target           : Kamu harus menjaga rata-rata IP minimal {nilai_dibutuhkan:.2f}")
        print("                            di sisa SKS/semester ke depan.")
    else:
        print("Status Target             : TARGET SUDAH AMAN TERCAPAI!")