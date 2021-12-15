"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""
from typing import Dict
from gempaterkini import ekstraksi_data, tampilkan_data

def main():
    print("\n==============")
    print("Aplikasi Utama")
    print("==============")

    result = ekstraksi_data()
    tampilkan_data(result)

if __name__ == '__main__':
    main()
    
   