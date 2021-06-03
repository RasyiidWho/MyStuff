import numpy as np
import os

numpy_array = np.array([["Bob", 54, "L"], ["John", 60, "L"], ["Carla", 18, "P"], ["Kuchid", 24, "P"], ["Doom", 120, "P"]] )


def ngecrot_sakpuase(sempak):
    if sempak:
        print("Anda mengulangi kembali dari awal! Apa yang ingin Anda pilih?\n")
    else:
        print("Selamat datang! Ini pertama kalinya Anda membuka program ini. Silahkan pilih menu dibawah ini:\n")
    print("(1) Tampilkan Data")
    print("(2) Mencari Data")
    pilihan = input("Masukkan pilihan Anda: ")
    # pilihan = "2"
    if "1" in pilihan:
        print("Baiklah, ini adalah isi array saya:\n",numpy_array)
        metu_mlebu()
    else:
        lonet = input("Oke, sekarang masukkan apa yang ingin Anda cari: ")
        # lonet = "Carla"
        jem, bud = np.where(numpy_array == lonet)
        # print(mambu)
        print("Berikut data yang saya peroleh dari array program ini: ", numpy_array[(jem)])
        metu_mlebu()

def metu_mlebu():
    pilihan2 = input("\nApakah Anda ingin mengulangi lagi? (y/n) ")
    # pilihan2 = "y"
    if "n" in pilihan2:
        os.system('cls')
        exit()
    else:
        os.system('cls')
        ngecrot_sakpuase(sempak=True)

ngecrot_sakpuase(sempak=False)