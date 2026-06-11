# linked_list.py

from ui import panel
from ui import akhir
from ui import kembali_ke_menu


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class RiwayatServis:
    def __init__(self):
        self.head = None

    def tambah_riwayat(self, data):
        node_baru = Node(data)

        if self.head is None:
            self.head = node_baru
        else:
            bantu = self.head

            while bantu.next is not None:
                bantu = bantu.next

            bantu.next = node_baru

    def tampilkan_riwayat(self):
        panel("RIWAYAT SERVIS")

        if self.head is None:
            print("Belum ada riwayat servis.")
            akhir()
            kembali_ke_menu()
            return

        bantu = self.head
        nomor_urut = 1

        while bantu is not None:
            data = bantu.data

            print(f"\nRiwayat ke-{nomor_urut}")
            print(f"Nomor Servis   : {data.nomor}")
            print(f"Nama Pelanggan : {data.nama}")
            print(f"Perangkat      : {data.perangkat}")
            print(f"Kerusakan      : {data.kerusakan}")
            print(f"Biaya Servis   : Rp{data.biaya:,}")

            bantu = bantu.next
            nomor_urut += 1

        akhir()
        kembali_ke_menu()