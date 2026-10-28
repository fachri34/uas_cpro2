def lihat_daftar(daftar_mk):
    print("\n--- DAFTAR MATA KULIAH ---")
    if len(daftar_mk) == 0:
        print("Belum ada mata kuliah.")
    else:
        print("No | Nama Mata Kuliah | SKS | Nilai | Bobot | Poin")
        print("-" * 60)
        for no, mk in enumerate(daftar_mk, 1):
            print(no, "|", mk['nama'], "|", mk['sks'], "|", mk['nilai'], "|", mk['bobot'], "|", mk['poin'])
        print("-" * 60)
        
        # PERBAIKAN: Gunakan fungsi sum() secara langsung untuk menghitung total
        total_sks = sum(mk['sks'] for mk in daftar_mk)
        total_poin = sum(mk['poin'] for mk in daftar_mk)
        
        print("Total SKS :", total_sks, "SKS | Total Poin :", total_poin)