from add_matkul import tambah_mk
from target_simulasi  import simulasi_target
from hitung_ipk import tampilkan_ipk

SKALA_NILAI = {
    "A": 4.0, 
    "B+": 3.5, 
    "B": 3.0, 
    "C+": 2.5, 
    "C": 2.0, 
    "D": 1.0, 
    "E": 0.0
}
daftar_mk = []

def tampilkan_menu():
    print("\n=============================================")
    print("   TARGETIPK - KALKULATOR & SIMULASI IPK")
    print("=============================================")
    print("1. Tambah Mata Kuliah")
    print("2. Lihat Daftar Mata Kuliah")
    print("3. Hitung IPK & Predikat Saat Ini")
    print("4. Simulasi Target IPK")
    print("5. Hapus Mata Kuliah")
    print("0. Keluar")
    print("---------------------------------------------")

def main():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (0-5): ").strip()
        if pilihan == '1':
            tambah_mk(daftar_mk, SKALA_NILAI)
        elif pilihan == '2':
            print("\n[Fitur 2: Lihat Daftar - Akan dikerjakan Jason]")
        elif pilihan == '3':
            tampilkan_ipk(daftar_mk)
        elif pilihan == '4':
            simulasi_target(daftar_mk)
        elif pilihan == '5':
            print("\n[Fitur 5: Hapus Matkul - Akan dikerjakan Fachri]")
        elif pilihan == '0':
            print("\nTerima kasih telah menggunakan TargetIPK! Program selesai.")
            break          
        else:
            print("\n[!] Pilihan tidak valid! Silakan ketik angka 0 sampai 5.")

if __name__ == "__main__":
    main()