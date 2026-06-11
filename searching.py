# searching.py

def linear_search(data_servis, nomor_cari):
    for data in data_servis:
        if data.nomor == nomor_cari:
            return data

    return None