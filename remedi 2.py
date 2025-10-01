print("=== PILIH JENIS PRODUK ===")
print("1. Elektronik")
print("2. Pakaian")
print("3. Makanan")
print("4. Kosmetik")

pilihan = int(input("Masukkan pilihan (1-4): "))

# Menentukan kategori produk berdasarkan angka
if pilihan == 1:
    kategori = "Elektronik"
elif pilihan == 2:
    kategori = "Pakaian"
elif pilihan == 3:
    kategori = "Makanan"
elif pilihan == 4:
    kategori = "Kosmetik"
else:
    kategori = "Lainnya"

# Input harga dan penjualan
harga = int(input("Masukkan harga produk (dalam rupiah): "))
penjualan = int(input("Masukkan jumlah penjualan produk (unit): "))

# Menentukan kategori harga
if harga > 100000:
    kategori_harga = "Premium"
elif 50000 <= harga <= 100000:
    kategori_harga = "Menengah"
else:
    kategori_harga = "Terjangkau"

# Menentukan kategori penjualan
if penjualan >= 100:
    kategori_penjualan = "Best Seller"
elif 50 <= penjualan <= 99:
    kategori_penjualan = "Populer"
else:
    kategori_penjualan = "Normal"

# Hasil
print("\n=== HASIL KATEGORI PRODUK ===")
print(f"Jenis Produk      : {kategori}")
print(f"Kategori Harga    : {kategori_harga}")
print(f"Kategori Penjualan: {kategori_penjualan}")
