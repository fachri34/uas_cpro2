def tampilkan_ipk(daftar_mk):
    """
    Menu 3: Menghitung total SKS, total Poin, IPK, 
    menentukan predikat, dan mencetak progress bar dalam satu fungsi.
    """
    print("\n--- HASIL PERHITUNGAN IPK ---")

    # Cek apakah daftar mata kuliah kosong
    if len(daftar_mk) == 0:
        print("Belum ada mata kuliah untuk dihitung")
        return

    # Hitung total SKS dan Poin mutu secara langsung
    total_sks = sum(mk['sks'] for mk in daftar_mk)
    total_poin = sum(mk['poin'] for mk in daftar_mk)
    
    # Hitung IPK
    ipk = total_poin / total_sks if total_sks > 0 else 0.0

    # Tentukan Predikat berdasarkan IPK
    if ipk >= 3.50:
        predikat = "Cum Laude"
    elif ipk >= 3.00:
        predikat = "Sangat Memuaskan"
    elif ipk >= 2.50:
        predikat = "Memuaskan"
    elif ipk >= 2.00:
        predikat = "Cukup"
    else:
        predikat = "Perlu Ditingkatkan"

    # Buat Progress Bar visual
    persentase = (ipk / 4.0) * 100
    total_balok = 20
    balok_terisi = int(round((ipk / 4.0) * total_balok))
    bar = "#" * balok_terisi + "-" * (total_balok - balok_terisi)
    progress_bar = f"[{bar}] {persentase:.1f}%"

    # Tampilkan hasil perhitungan akhir
    print(f"Total SKS Selesai : {total_sks} SKS")
    print(f"Total Poin Mutu   : {total_poin:.2f}")
    print(f"IPK Saat Ini      : {ipk:.2f} / 4.00")
    print(f"Progress IPK      : {progress_bar}")
    print(f"Predikat Saat Ini : {predikat}")