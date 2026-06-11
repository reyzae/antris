from models import Servis
from linked_list import RiwayatServis
from sorting import bubble_sort_nama
from searching import linear_search
from ui import panel, akhir, kembali_ke_menu


# Array atau List untuk menyimpan antrean servis
antrean_servis = []


# Objek Linked List untuk riwayat servis
riwayat_servis = RiwayatServis()


# Nomor servis otomatis
nomor_berikutnya = 1

# Menu 1: untuk Tambah data servis
def tambah_data():
    global nomor_berikutnya

    panel("TAMBAH DATA SERVIS")

    nomor = f"SRV{nomor_berikutnya:03d}"

    nama = input("Nama pelanggan   : ").strip()
    perangkat = input("Jenis perangkat  : ").strip()
    kerusakan = input("Jenis kerusakan  : ").strip()

    if nama == "" or perangkat == "" or kerusakan == "":
        print("\nData tidak boleh kosong.")
        akhir()
        return

    try:
        biaya = int(input("Biaya servis (Rp): "))

        if biaya < 0:
            print("\nBiaya tidak boleh negatif.")
            akhir()
            return

    except ValueError:
        print("\nBiaya harus berupa angka.")
        akhir()
        return

    data_baru = Servis(
        nomor,
        nama,
        perangkat,
        kerusakan,
        biaya
    )

    # Queue: data baru masuk ke bagian belakang
    antrean_servis.append(data_baru)

    nomor_berikutnya += 1

    panel("DATA SERVIS BERHASIL DITAMBAHKAN")
    print(f"Nomor Servis   : {data_baru.nomor}")
    print(f"Nama Pelanggan : {data_baru.nama}")
    print(f"Perangkat      : {data_baru.perangkat}")
    print(f"Kerusakan      : {data_baru.kerusakan}")
    print(f"Biaya Servis   : Rp{data_baru.biaya:,}")
    print(f"Posisi Antrean : {len(antrean_servis)}")
    akhir()
    kembali_ke_menu()   


# Menu 2: untuk menampilkan antrean
def tampilkan_data():
    panel("DAFTAR ANTREAN SERVIS")

    if len(antrean_servis) == 0:
        print("Antrean servis masih kosong.")
        akhir()
        kembali_ke_menu()
        return

    for i in range(len(antrean_servis)):
        data = antrean_servis[i]

        print(f"\nAntrean ke-{i + 1}")
        print(f"Nomor Servis   : {data.nomor}")
        print(f"Nama Pelanggan : {data.nama}")
        print(f"Perangkat      : {data.perangkat}")
        print(f"Kerusakan      : {data.kerusakan}")
        print(f"Biaya Servis   : Rp{data.biaya:,}")

    print(f"\nJumlah antrean: {len(antrean_servis)} pelanggan")
    akhir()
    kembali_ke_menu()


# Menu 3: untuk Cari data servis
def cari_data():
    panel("CARI DATA SERVIS")

    if len(antrean_servis) == 0:
        print("Antrean servis masih kosong.")
        akhir()
        kembali_ke_menu()
        return

    nomor_cari = input("Masukkan nomor servis: ").strip().upper()

    hasil = linear_search(antrean_servis, nomor_cari)

    if hasil is not None:
        print("\nData berhasil ditemukan.")
        print(f"Nomor Servis   : {hasil.nomor}")
        print(f"Nama Pelanggan : {hasil.nama}")
        print(f"Perangkat      : {hasil.perangkat}")
        print(f"Kerusakan      : {hasil.kerusakan}")
        print(f"Biaya Servis   : Rp{hasil.biaya:,}")
    else:
        print(f"\nNomor servis {nomor_cari} tidak ditemukan.")

    akhir()
    kembali_ke_menu()


# Menu 4: untuk mengurutkan nama A-Z
def urutkan_nama():
    panel("URUTKAN DATA BERDASARKAN NAMA")

    if len(antrean_servis) == 0:
        print("Antrean servis masih kosong.")
        akhir()
        kembali_ke_menu()
        return

    bubble_sort_nama(antrean_servis)

    print("Data berhasil diurutkan dari A-Z.")

    for i in range(len(antrean_servis)):
        data = antrean_servis[i]

        print(
            f"{i + 1}. {data.nama} - "
            f"{data.nomor} - {data.perangkat}"
        )

    akhir()
    kembali_ke_menu()


# Menu 5: Proses antrean
def proses_antrean():
    panel("PROSES ANTREAN SERVIS")

    if len(antrean_servis) == 0:
        print("Tidak ada antrean yang dapat diproses.")
        akhir()
        kembali_ke_menu()
        return

    # Queue FIFO: data paling depan diproses pertama
    data_diproses = antrean_servis.pop(0)

    # Data yang selesai dimasukkan ke Linked List
    riwayat_servis.tambah_riwayat(data_diproses)

    print("Servis berhasil diproses.")
    print(f"Nomor Servis   : {data_diproses.nomor}")
    print(f"Nama Pelanggan : {data_diproses.nama}")
    print(f"Perangkat      : {data_diproses.perangkat}")
    print(f"Kerusakan      : {data_diproses.kerusakan}")
    print(f"Biaya Servis   : Rp{data_diproses.biaya:,}")
    print(f"Sisa Antrean   : {len(antrean_servis)} pelanggan")
    akhir()
    kembali_ke_menu()