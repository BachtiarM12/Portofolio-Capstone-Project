# Data barang_dijual from store_inventory Han Bookstore
#### Data barang yang dijual 
store_inventory = {
    'Fiction Books': {'price': 80000, 'stock': 10},
    'Non-Fiction Books': {'price': 90000, 'stock': 8},
    'Textbooks': {'price': 120000, 'stock': 5},
    "Children's Books": {'price': 70000, 'stock': 12},
    'HB Pencil': {'price': 5000, 'stock': 30},
    '2B Pencil': {'price': 6000, 'stock': 25},
    'Colored Pencils': {'price': 25000, 'stock': 15},
    'A4 Paper': {'price': 35000, 'stock': 20},
    'Notebook': {'price': 15000, 'stock': 18},
    'Drawing Paper': {'price': 20000, 'stock': 10},
    'Backpack': {'price': 100000, 'stock': 7},
    'Lunch Box': {'price': 40000, 'stock': 10},
    'Geometry Set': {'price': 30000, 'stock': 9},
    'Water Bottle': {'price': 25000, 'stock': 14}
}

# Initialize cart and transaction history
keranjang = []
riwayat_transaksi = []

# Function to display items
def tampilkan_barang():
    print("\n")
    print(f"{'No':<4} {'Nama Barang':<30} {'Stok':<6} {'Harga Jual':<15}")
    print("-" * 55)
    for i, (nama, info) in enumerate(store_inventory.items(), 1):
        print(f"{i:<4} {nama:<30} {info['stock']:<6} Rp{int(info['price']):,}")

# Function to add items to cart
def tambah_ke_keranjang():
    tampilkan_barang()
    no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
    if 1 <= no_barang <= len(store_inventory):
        nama = list(store_inventory.keys())[no_barang - 1]
        jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        if jumlah <= 0:
            print("Jumlah tidak boleh negatif atau nol.")
            return
        if jumlah > store_inventory[nama]['stock']:
            print(f"Stok tidak mencukupi. Stok tersedia: {store_inventory[nama]['stock']}")
            return
        keranjang.append({'No': no_barang, 'Nama': nama, 'Jumlah': jumlah, 'Harga': store_inventory[nama]['price']})
        print(f"{nama} sebanyak {jumlah} berhasil ditambahkan ke keranjang.")
    else:
        print("Barang tidak ditemukan.")

# Function to edit or remove items from cart
def ubah_atau_hapus_keranjang():
    if not keranjang:
        print("Keranjang Anda kosong.")
        return
    print("\n=== Keranjang Belanja ===")
    for index, item in enumerate(keranjang, 1):
        print(f"{index}. {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Jumlah'] * item['Harga']):,}")
    pilihan = int(input("Masukkan nomor barang yang ingin diubah atau dihapus dari keranjang: "))
    if 1 <= pilihan <= len(keranjang):
        barang_dipilih = keranjang[pilihan - 1]
        nama = barang_dipilih['Nama']
        stok_tersedia = store_inventory[nama]['stock']
        aksi = input("Apakah Anda ingin mengubah jumlah (u) atau menghapus barang (h)? (u/h): ").lower()
        if aksi == 'u':
            jumlah_baru = int(input(f"Masukkan jumlah baru untuk {barang_dipilih['Nama']} (maksimal {stok_tersedia}): "))
            if jumlah_baru <= 0:
                print("Jumlah tidak boleh negatif atau nol.")
                return
            if jumlah_baru > stok_tersedia:
                print(f"Stok tidak mencukupi. Stok tersedia: {stok_tersedia}")
                return
            barang_dipilih['Jumlah'] = jumlah_baru
            print(f"Jumlah {barang_dipilih['Nama']} berhasil diubah menjadi {jumlah_baru}.")
        elif aksi == 'h':
            keranjang.pop(pilihan - 1)
            print(f"Barang {barang_dipilih['Nama']} berhasil dihapus dari keranjang.")
        else:
            print("Pilihan tidak valid.")
    else:
        print("Nomor barang tidak valid.")

# Function to view cart
def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    print("\n=== Keranjang Belanja ===")
    total_harga = 0
    for item in keranjang:
        subtotal = item['Jumlah'] * item['Harga']
        print(f"{item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(subtotal):,}")
        total_harga += subtotal
    print(f"Total harga: Rp{int(total_harga):,}")

# Function for checkout
def checkout(username):
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
    transaksi = {'Pembeli': username, 'Barang': [], 'Total': 0}
    print("\n=== Detail Barang yang Akan Di-checkout ===")
    print(f"{'No':<3} {'Nama Barang':<17} {'Jumlah':<9} {'Harga Satuan':<18} {'Total':<14}")
    print("="*61)
    for idx, item in enumerate(keranjang, 1):
        nama = item['Nama']
        harga_total_item = item['Jumlah'] * store_inventory[nama]['price']
        total_harga += harga_total_item
        transaksi['Barang'].append({'Nama': nama, 'Jumlah': item['Jumlah'], 'Harga Jual': store_inventory[nama]['price']})
        print(f"{idx:<3} {item['Nama']:<17} {item['Jumlah']:<9} Rp{int(store_inventory[nama]['price']):<18,} Rp{int(harga_total_item):<14,}")
    print("="*61)
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

# Function to buy an item directly
def beli_barang(username):
    tampilkan_barang()
    no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
    if 1 <= no_barang <= len(store_inventory):
        nama = list(store_inventory.keys())[no_barang - 1]
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
        transaksi = {'Pembeli': username, 'Barang': [{'Nama': nama, 'Jumlah': qty, 'Harga Jual': store_inventory[nama]['price']}], 'Total': total}
        riwayat_transaksi.append(transaksi)
    else:
        print("Barang tidak ditemukan.")

# Customer menu
def customer_menu(username):
    choice = '0'
    while choice != '6':
        print("\nCustomer Menu")
        print("1. View All Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Edit or Remove from Cart")
        print("5. Checkout")
        print("6. Exit")
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
            checkout(username)
        elif choice == '6':
            print("Thank you for visiting Han Bookstore!")
        else:
            print("Invalid choice. Please try again.")

# Main program
if __name__ == "__main__":
    print("Welcome to the Han Bookstore!")
    customer_menu("customer")
