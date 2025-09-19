# ===========================================================================================================================
# Nah! Bookstore
# ===========================================================================================================================
# Bachtiar Mardiansyah
# JCDS - BSDAM29

# /**************************************************************************************************************************/

# Data barang_dijual from store_inventory Nah! Bookstore
# Categories: International Novel, Children's Book, Non-Fiction Book, Fiction Book, Investment Book, Social Studies Book, Accessories, CLutch, Wallet, Bag, Pencil, and Toy
store_inventory = {
    'A Curtain Twitcher\'s Book of Murder': {'Category': 'International Novel', 'price': 103500, 'stock': 10},
    'The Book Censor\'s Library': {'Category': 'International Novel', 'price': 90000, 'stock': 8},
    'The Arcanum of Aalisha': {'Category': 'International Novel', 'price': 129000, 'stock': 17},
    'The Traveling Cat Chronicles': {'Category': 'International Novel', 'price': 109000, 'stock': 15},
    'My First Book of Emotions': {'Category': 'Children\'s Book', 'price': 47200, 'stock': 120},
    'My First Book of My Body': {'Category': 'Children\'s Book', 'price': 44250, 'stock': 15},
    'The Book of Ikigai': {'Category': 'Children\'s Book', 'price': 69000, 'stock': 5},
    'Budi Daya Tanaman Buah dalam Pot': {'Category': 'Children\'s Book', 'price': 174000, 'stock': 21},
    'Unofficial Book BTS': {'Category': 'Non-Fiction Book', 'price': 85950, 'stock': 18},
    'Trials Of Apollo Book One: The Hidden Oracle': {'Category': 'Fiction Book', 'price': 20000, 'stock': 10},
    'Ghibli-Princess Mononoke': {'Category': 'Fiction Book', 'price': 520000, 'stock': 7},
    'Naruto Official Animation Book: Hiden Douga Emaki': {'Category': 'Fiction Book', 'price': 37500, 'stock': 14},
    'Main Book of Candlestick': {'Category': 'Investment Book', 'price': 89000, 'stock': 110},
    'SMA/MA Kl 10 Ekonomi 1 Kelompok Peminatan Ilmu Sosial': {'Category': 'Social Studies Book', 'price': 102600, 'stock': 9},
    'Naruto Official Animation Book: Hiden Douga Emaki': {'Category': 'Fiction Book', 'price': 37500, 'stock': 14},
    'Kukiko Keychain Plush Monkey Light Brown Yj3052': {'Category': 'Accessories', 'price': 30000, 'stock': 14},
    'Kukiko Keychain Plush Corn ': {'Category': 'Accessories', 'price': 30000, 'stock': 13},
    'Kukiko Keychain Plush Broccoli Flower ': {'Category': 'Accessories', 'price': 35000, 'stock': 9},
    'Kukiko Keychain Plush Rabbit Grey ': {'Category': 'Accessories', 'price': 35000, 'stock': 2},
    'Eversac Office Schwarz': {'Category': 'Clutch', 'price': 49000, 'stock': 1},
    'Tfg Wallet Washington 203': {'Category': 'Wallet', 'price': 169000, 'stock': 123},
    'Piknik Backpack Drawstring Cuba Petrol': {'Category': 'Bag', 'price': 169000, 'stock': 123},
    'Eversac Laptop Sleeve X Pakai Lagi': {'Category': 'Bag', 'price': 219000, 'stock': 3},
    'Faber Castell - Crayon Hexagonal Oil Pastel 48 Warna': {'Category': 'Pencil', 'price': 219000, 'stock': 3},
    'Faber Castell - Crayon Hexagonal Oil Pastel 24 Warna': {'Category': 'Pencil', 'price': 98000, 'stock': 5},
    'Blokees Transformers Cc17 Movie Soundwave': {'Category': 'Toy', 'price': 198000, 'stock': 2}
}
# /**************************************************************************************************************************/

# Penetapan nilai awal dari keranjang belanja dan riwayat transaksi
keranjang = []
riwayat_transaksi = []

# /**************************************************************************************************************************/


# Function to display items
def tampilkan_barang():
    print("\n")
    print(f"{'No':<4} {'Nama Barang':<60} {'Category':<20} {'Stok':<6} {'Harga Jual':<15}")            #luas kolom disesuaikan dengan panjang teks yang terpanjang
    print("-" * 105)
    for i, (nama, info) in enumerate(store_inventory.items(), 1):                                      #mulai dari 1
        print(f"{i:<4} {nama:<60} {info['Category']:<20} {info['stock']:<6} Rp{int(info['price']):,}") #format angka dengan koma sebagai pemisah ribuan

# Function to add items to cart
def tambah_ke_keranjang():
    try:
        tampilkan_barang()
        no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
        if 1 <= no_barang <= len(store_inventory):                                                      #validasi nomor barang yang dimasukkan 
            nama = list(store_inventory.keys())[no_barang - 1]
            jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
            if jumlah <= 0:                                                                             #validasi jumlah barang yang dimasukkan 
                print("Jumlah tidak boleh negatif atau nol.")
                return
            if jumlah > store_inventory[nama]['stock']:                                                 #validasi stok barang yang tersedia 
                print(f"Stok tidak mencukupi. Stok tersedia: {store_inventory[nama]['stock']}")
                return
            keranjang.append({'No': no_barang, 'Nama': nama, 'Jumlah': jumlah, 'Harga': store_inventory[nama]['price']})
            print(f"{nama} sebanyak {jumlah} berhasil ditambahkan ke keranjang.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# /**************************************************************************************************************************/

# Function to edit or remove items from cart
def ubah_atau_hapus_keranjang():
    if not keranjang:                                                                                     #cek apakah keranjang kosong  
        print("Keranjang Anda kosong.")
        return
    print("\n=== Keranjang Belanja ===")
    for index, item in enumerate(keranjang, 1):                                                           #mulai dari 1   
        print(f"{index}. {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Jumlah'] * item['Harga']):,}")
    try:
        pilihan = int(input("Masukkan nomor barang yang ingin diubah atau dihapus dari keranjang: "))
        if 1 <= pilihan <= len(keranjang):
            barang_dipilih = keranjang[pilihan - 1]
            nama = barang_dipilih['Nama']
            stok_tersedia = store_inventory[nama]['stock']
            aksi = input("Apakah Anda ingin mengubah jumlah (u) atau menghapus barang (h)? (u/h): ").lower()
            if aksi == 'u':
                try:
                    jumlah_baru = int(input(f"Masukkan jumlah baru untuk {barang_dipilih['Nama']} (maksimal {stok_tersedia}): "))
                    if jumlah_baru <= 0:
                        print("Jumlah tidak boleh negatif atau nol.")
                        return
                    if jumlah_baru > stok_tersedia:
                        print(f"Stok tidak mencukupi. Stok tersedia: {stok_tersedia}")
                        return
                    barang_dipilih['Jumlah'] = jumlah_baru
                    print(f"Jumlah {barang_dipilih['Nama']} berhasil diubah menjadi {jumlah_baru}.")
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka.")
            elif aksi == 'h':
                keranjang.pop(pilihan - 1)
                print(f"Barang {barang_dipilih['Nama']} berhasil dihapus dari keranjang.")
            else:
                print("Pilihan tidak valid.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

# /**************************************************************************************************************************/

# Function to view cart
def lihat_keranjang():
    if not keranjang:                                                                                          #cek apakah keranjang kosong 
        print("Keranjang kosong.")
        return
    print("\n=== Keranjang Belanja ===")
    total_harga = 0
    for item in keranjang:
        subtotal = item['Jumlah'] * item['Harga']
        print(f"{item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(subtotal):,}")
        total_harga += subtotal
    print(f"Total harga: Rp{int(total_harga):,}")

# /**************************************************************************************************************************/

# Function for checkout
def checkout(user):
    if not keranjang:
        print("Keranjang belanja Anda kosong.")
        return
    all_sufficient = True
    for item in keranjang:
        nama = item['Nama']
        if nama not in store_inventory or store_inventory[nama]['stock'] < item['Jumlah']:                                         
            print(f"Stok tidak mencukupi untuk {item['Nama']} atau barang tidak ditemukan.")
            all_sufficient = False
    if not all_sufficient:
        return
    total_harga = 0
    transaksi = {'Pembeli': user, 'Barang': [], 'Total': 0}
    print("\n=== Detail Barang yang Akan Checkout dari Nah! Bookstore ===")
    print(f"{'No':<3} {'Nama Barang':<60} {'Category':<20} {'Jumlah':<9} {'Harga Satuan':<18} {'Total':<14}")
    print("="*124)
    for idx, item in enumerate(keranjang, 1):
        nama = item['Nama']
        harga_total_item = item['Jumlah'] * store_inventory[nama]['price']
        total_harga += harga_total_item
        transaksi['Barang'].append({'Nama': nama, 'Jumlah': item['Jumlah'], 'Harga Jual': store_inventory[nama]['price']})
        print(f"{idx:<3} {item['Nama']:<60} {store_inventory[nama]['Category']:<20} {item['Jumlah']:<9} Rp{int(store_inventory[nama]['price']):<18,} Rp{int(harga_total_item):<14,}")
    print("="*124)
    print(f"Total Harga: Rp{int(total_harga):,}")
    konfirmasi = input("Konfirmasi pembelian (y/n): ").lower()
    if konfirmasi == 'y':
        for item in keranjang:
            nama = item['Nama']
            store_inventory[nama]['stock'] -= item['Jumlah']
        transaksi['Total'] = total_harga
        riwayat_transaksi.append(transaksi)
        keranjang.clear()
        print("Pembelian berhasil!")
    else:
        print("Pembelian dibatalkan.")

# /**************************************************************************************************************************/

# Function to buy an item directly
def beli_barang(user):
    try:
        tampilkan_barang()
        no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
        if 1 <= no_barang <= len(store_inventory):                                                              
            nama = list(store_inventory.keys())[no_barang - 1]
            # Pengecekan eksistensi barang
            if nama in store_inventory:
                try:
                    qty = int(input("Masukkan jumlah yang ingin dibeli: "))
                    if qty <= 0:
                        print("Jumlah tidak boleh negatif atau nol.")
                        return
                    if qty > store_inventory[nama]['stock']:
                        print(f"Stok tidak mencukupi. Stok tersedia: {store_inventory[nama]['stock']}")
                        return
                    total = store_inventory[nama]['price'] * qty
                    store_inventory[nama]['stock'] -= qty
                    print(f"Purchased {qty} x {nama} for Rp{int(total):,}. Thank you!")
                    transaksi = {
                        'Pembeli': user,
                        'Barang': [{'Nama': nama, 'Jumlah': qty, 'Harga Jual': store_inventory[nama]['price']}],
                        'Total': total
                    }
                    riwayat_transaksi.append(transaksi)
                except ValueError:
                    print("Input tidak valid. Harap masukkan angka untuk jumlah.")
            else:
                print(f"Barang '{nama}' tidak ditemukan di inventaris.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid. Harap masukkan angka untuk nomor barang.")

# /**************************************************************************************************************************/

# Customer menu
def customer_menu(user):
    choice = '0'
    while choice != '6':
        print("\nCustomer Menu")
        print("1. View All Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Edit or Remove from Cart")
        print("5. Checkout")
        print("6. Exit")
        try:
            choice = input("Enter the number of your choice (1-6): ").strip()
            if choice == '1':
                tampilkan_barang()
            elif choice == '2':
                tambah_ke_keranjang()
            elif choice == '3':
                lihat_keranjang()
            elif choice == '4':
                ubah_atau_hapus_keranjang()
            elif choice == '5':
                checkout(user)
            elif choice == '6':
                print("Thank you for visiting Nah! Bookstore!")
            else:
                print("Pilihan tidak valid. Harap masukkan angka antara 1-6.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

# /**************************************************************************************************************************/

# Main program
if __name__ == "__main__":
    print("-"*150)
    print("Welcome to the Nah! Bookstore!")
    print("By = Bachtiar Mardiansyah")
    print("JCDS - BSDAM29")
    print("-"*150)
    customer_menu("customer")

# /**************************************************************************************************************************/
