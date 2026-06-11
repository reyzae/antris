# sorting.py

def bubble_sort_nama(data_servis):
    jumlah_data = len(data_servis)

    for i in range(jumlah_data - 1):
        for j in range(jumlah_data - i - 1):

            nama_sekarang = data_servis[j].nama.lower()
            nama_berikutnya = data_servis[j + 1].nama.lower()

            if nama_sekarang > nama_berikutnya:
                data_servis[j], data_servis[j + 1] = (
                    data_servis[j + 1],
                    data_servis[j]
                )

    return data_servis