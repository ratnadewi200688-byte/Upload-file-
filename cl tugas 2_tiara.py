#python 3.7.1

#class

class AlatMusik:
    def __init__(self, nama, jenis, bahan, asal, harga):
        self.nama = nama
        self.jenis = jenis
        self.bahan = bahan
        self.asal = asal
        self.harga = harga

alat1 = AlatMusik("Gitar", "Petik", "Kayu Mahoni", "Spanyol", 1500000)
alat2 = AlatMusik("Piano", "Tekan", "Kayu Oak", "Italia", 7500000)

print(alat1.nama)
print(alat1.jenis)
print(alat1.bahan)
print(alat1.asal)
print(alat1.harga)
print(alat2.nama)
print(alat2.jenis)
print(alat2.bahan)
print(alat2.asal)
print(alat2.harga)
