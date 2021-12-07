"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""
from typing import Dict


def ekstraksi_data():
    """
    Tanggal : 06 Desember 2021
    Waktu : 09:39:55 WIB
    Magnitudo : 4.9
    Kedalaman : 10 km
    Lokasi : 8.72 LS - 118.36 BT
    Pusat Gempa : Pusat gempa berada di Laut 23 Km Barat Daya Dompu
    keterangan : Dirasakan (Skala MMI): III Dompu, III Bima
    """
    hasil = dict()
    hasil["tanggal"] = "06 Desember 2021"
    hasil["waktu"] = "09:39:55 WIB"
    hasil["magnitudo"] = 4.8
    hasil["lokasi"] = {"ls": 8.72, "bt": 118.36}
    hasil["pusat"] = "Pusat gempa berada di Laut 23 Km Barat Daya Dompu"
    hasil["dirasakan"] = "Dirasakan (Skala MMI): III Dompu, III Bima"

    return hasil


def tampilkan_data(result):
    print("\nGempa Terakhir Berdasarkan BMKG")
    print(f"Tanggal \t: {result['tanggal']}")
    print(f"Waktu \t\t: {result['waktu']}")
    print(f"Magnitudo \t: {result['magnitudo']}")
    print(
        f"Lokasi \t\t: LS = {result['lokasi']['ls']}, BT = {result['lokasi']['bt']}")
    print(f"Pusat \t\t: {result['pusat']}")
    print(f"Dirasakan \t: {result['dirasakan']}")


if __name__ == '__main__':
    print("\n==============")
    print("Aplikasi Utama")
    print("==============")

    result = ekstraksi_data()
    tampilkan_data(result)
