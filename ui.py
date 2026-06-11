LEBAR_BANNER = 43


def garis():
    print("=" * LEBAR_BANNER)


def judul(teks):
    print(teks.center(LEBAR_BANNER))


def panel(teks):
    print()
    garis()
    judul(teks)
    garis()


def akhir(jumlah_baris=2):
    for _ in range(jumlah_baris):
        print()


def kembali_ke_menu():
    input("\nTekan Enter untuk kembali ke menu utama...")