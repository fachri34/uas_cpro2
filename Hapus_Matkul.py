def hapus_mk(daftar_mk):
    print("\n--- HAPUS MATA KULIAH ---")
    if len(daftar_mk) == 0:
        print("Belum ada mata kuliah untuk dihapus.")
    else:
        for no, mk in enumerate(daftar_mk, 1):
            print(no, ".", mk['nama'], "(", mk['sks'], "SKS, Nilai", mk['nilai'], ")")

        selesai = False
        while not selesai:
            nomor = input("Pilih nomor yang ingin dihapus (0 untuk batal): ")
            if not nomor.isdigit():
                print("[!] Nomor tidak valid!")
            else:
                nomor = int(nomor)
                if nomor == 0:
                    print("Penghapusan dibatalkan.")
                    selesai = True
                elif 1 <= nomor <= len(daftar_mk):
                    mk_terhapus = daftar_mk.pop(nomor - 1)
                    print("[OK] Mata kuliah", mk_terhapus['nama'], "berhasil dihapus.")
                    selesai = True
                else:
                    print("[!] Nomor tidak valid!")