# main.py

from data_servis import (
    tambah_data,
    tampilkan_data,
    cari_data,
    urutkan_nama,
    proses_antrean,
    riwayat_servis
)
from ui import garis, judul


def tampilkan_menu():
    print()
    garis()
    judul("APLIKASI ANTREAN SERVIS KOMPUTER")
    garis()
    print("1. Tambah Data Servis")
    print("2. Tampilkan Antrean Servis")
    print("3. Cari Data Servis")
    print("4. Urutkan Data Servis A-Z")
    print("5. Proses Antrean Servis")
    print("6. Tampilkan Riwayat Servis")
    print("7. Keluar")
    garis()


def menu_utama():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu (1-7): ").strip()

        if pilihan == "1":
            tambah_data()

        elif pilihan == "2":
            tampilkan_data()

        elif pilihan == "3":
            cari_data()

        elif pilihan == "4":
            urutkan_nama()

        elif pilihan == "5":
            proses_antrean()

        elif pilihan == "6":
            riwayat_servis.tampilkan_riwayat()

        elif pilihan == "7":
            print()
            garis()
            print("Program berhasil dihentikan.")
            print("Terima kasih telah menggunakan aplikasi.")
            garis()
            break

        else:
            print("\nPilihan tidak valid.")
            print("Silakan masukkan angka dari 1 sampai 7.")


if __name__ == "__main__":
    menu_utama()