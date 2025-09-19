# Initialize barang_dijual from store_inventory
store_inventory = {
    'Books': {
        'Fiction': {'price': 80000, 'stock': 10},
        'Non-Fiction': {'price': 90000, 'stock': 8},
        'Textbooks': {'price': 120000, 'stock': 5},
        "Children's Books": {'price': 70000, 'stock': 12}
    },
    'Pencils': {
        'HB Pencil': {'price': 5000, 'stock': 30},
        '2B Pencil': {'price': 6000, 'stock': 25},
        'Colored Pencils': {'price': 25000, 'stock': 15}
    },
    'Papers': {
        'A4 Paper': {'price': 35000, 'stock': 20},
        'Notebook': {'price': 15000, 'stock': 18},
        'Drawing Paper': {'price': 20000, 'stock': 10}
    },
    'School Supplies': {
        'Backpack': {'price': 100000, 'stock': 7},
        'Lunch Box': {'price': 40000, 'stock': 10},
        'Geometry Set': {'price': 30000, 'stock': 9},
        'Water Bottle': {'price': 25000, 'stock': 14}
    }
}
for category, items in store_inventory.items():
    for name, info in items.items():
        harga_jual = info['price']
        harga_beli = round(harga_jual / 1.2)
        stok = info['stock']
        barang_dijual.append({'No': no, 'Nama': f"{category} - {name}", 'Stok': stok, 'Harga Beli': harga_beli, 'Harga Jual': harga_jual})
        no += 1

# Fungsi untuk menampilkan daftar barang yang dijual
# tampilkan_barang(role): Fungsi untuk menampilkan barang yang ada, dengan dua tampilan berbeda untuk penjual dan pembeli. 
# Pembeli tidak bisa melihat harga beli.
def tampilkan_barang(role):
    print("\n")
    if role == 'customer':
        print(f"{'No':<4} {'Nama Barang':<30} {'Stok':<6} {'Harga Jual':<15}")
        print("-" * 55)
        for barang in barang_dijual:
            print(f"{barang['No']:<4} {barang['Nama']:<30} {barang['Stok']:<6} Rp{int(barang['Harga Jual']):,}")
    else:
        print(f"{'No':<4} {'Nama Barang':<30} {'Stok':<6} {'Harga Beli':<15} {'Harga Jual':<15}")
        print("-" * 70)
        for barang in barang_dijual:
            print(f"{barang['No']:<4} {barang['Nama']:<30} {barang['Stok']:<6} Rp{int(barang['Harga Beli']):<15} Rp{int(barang['Harga Jual']):,}")

# Fungsi untuk menambahkan barang baru oleh penjual
# tambah_barang(): Fungsi untuk menambahkan barang baru oleh penjual. 
# Stok dan harga beli tidak boleh negatif atau nol. Harga jual dihitung otomatis dengan markup 20%.
def tambah_barang():
    nama = input("Nama barang: ")
    while True:
        try:
            stok = int(input("Stok barang: "))
            if stok <= 0:
                print("Stok tidak boleh negatif atau nol.")
            else:
                break
        except ValueError:
            print("Invalid input. Masukkan angka.")
    while True:
        try:
            harga_beli = int(input("Harga beli: "))
            if harga_beli <= 0:
                print("Harga beli tidak boleh negatif atau nol.")
            else:
                break
        except ValueError:
            print("Invalid input. Masukkan angka.")
    harga_jual = harga_beli * 1.2  # Harga jual ditentukan dengan markup 20%
    no_baru = len(barang_dijual) + 1
    barang_dijual.append({'No': no_baru, 'Nama': nama, 'Stok': stok, 'Harga Beli': harga_beli, 'Harga Jual': harga_jual})
    print(f"{nama} berhasil ditambahkan.")

# Fungsi untuk mengubah informasi barang (nama, stok, harga beli) oleh penjual
# ubah_barang(): Fungsi untuk mengubah informasi barang (nama, stok, dan harga beli). 
# Sama seperti aturan sebelumnya, stok dan harga beli tidak boleh negatif atau nol. Harga jual dihitung ulang secara otomatis.
def ubah_barang():
    try:
        no_barang = int(input("Masukkan nomor barang yang ingin diubah: "))
    except ValueError:
        print("Invalid input. Masukkan angka.")
        return
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            barang['Nama'] = input("Nama barang baru: ")
            while True:
                try:
                    stok_baru = int(input("Stok barang baru: "))
                    if stok_baru <= 0:
                        print("Stok tidak boleh negatif atau nol.")
                    else:
                        barang['Stok'] = stok_baru
                        break
                except ValueError:
                    print("Invalid input. Masukkan angka.")
            while True:
                try:
                    harga_beli_baru = int(input("Harga beli baru: "))
                    if harga_beli_baru <= 0:
                        print("Harga beli tidak boleh negatif atau nol.")
                    else:
                        barang['Harga Beli'] = harga_beli_baru
                        barang['Harga Jual'] = harga_beli_baru * 1.2  # Update harga jual sesuai harga beli baru
                        break
                except ValueError:
                    print("Invalid input. Masukkan angka.")
            print(f"Barang nomor {no_barang} berhasil diubah.")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk menghapus barang oleh penjual
# hapus_barang(): Fungsi untuk menghapus barang dari daftar barang yang dijual. Barang dihapus berdasarkan nomor barang.
def hapus_barang():
    try:
        no_barang = int(input("Masukkan nomor barang yang ingin dihapus: "))
    except ValueError:
        print("Invalid input. Masukkan angka.")
        return
    for i, barang in enumerate(barang_dijual):
        if barang['No'] == no_barang:
            del barang_dijual[i]
            # Renumber the remaining items
            for j in range(i, len(barang_dijual)):
                barang_dijual[j]['No'] = j + 1
            print(f"Barang nomor {no_barang} berhasil dihapus.")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk menampilkan riwayat transaksi oleh penjual
# lihat_riwayat_transaksi_penjual(): Fungsi ini menampilkan semua riwayat transaksi yang telah dilakukan oleh pembeli. 
# Riwayat mencakup nama pembeli, barang yang dibeli, dan total transaksi.
def lihat_riwayat_transaksi_penjual():
    if not riwayat_transaksi:
        print("Belum ada transaksi yang dilakukan.")
        return

    print("\n=== Riwayat Transaksi ===")
    for transaksi in riwayat_transaksi:
        # Menampilkan detail transaksi pembeli
        print(f"Pembeli: {transaksi['Pembeli']}")
        for item in transaksi['Barang']:
            print(f" - {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Harga Jual'] * item['Jumlah'])}")
        print(f"Total: Rp{int(transaksi['Total'])}")
        print("="*40)

# Fungsi untuk menambah barang ke keranjang pembeli
# tambah_ke_keranjang(): Fungsi ini memungkinkan pembeli untuk menambahkan barang ke dalam keranjang. 
# Jika stok barang tidak mencukupi, pembeli akan diberi peringatan.
def tambah_ke_keranjang():
    tampilkan_barang('customer')
    try:
        no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
    except ValueError:
        print("Invalid input. Masukkan angka.")
        return
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            while True:
                try:
                    jumlah = int(input("Masukkan jumlah barang yang ingin dibeli: "))
                    # Validasi jumlah barang yang ditambahkan ke keranjang
                    if jumlah <= 0:
                        print("Jumlah barang tidak boleh negatif atau nol.")
                    elif jumlah > barang['Stok']:
                        print(f"Stok tidak mencukupi. Stok saat ini: {barang['Stok']}.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Masukkan angka.")
            # Menambahkan barang ke dalam keranjang
            keranjang.append({'No': no_barang, 'Nama': barang['Nama'], 'Jumlah': jumlah, 'Harga': barang['Harga Jual']})
            print(f"{barang['Nama']} sebanyak {jumlah} berhasil ditambahkan ke keranjang.")
            return
    print("Barang tidak ditemukan.")

# Fungsi untuk mengubah atau menghapus barang dari keranjang
# ubah_atau_hapus_keranjang(): Fungsi ini memungkinkan pembeli untuk mengubah jumlah barang dalam keranjang atau menghapus barang dari keranjang. 
# Jika jumlah barang baru melebihi stok yang tersedia, pesan kesalahan akan muncul. Barang yang dihapus akan dihapus sepenuhnya dari keranjang.
def ubah_atau_hapus_keranjang():
    if not keranjang:
        print("Keranjang Anda kosong.")
        return
    
    # Menampilkan barang di keranjang
    print("\n=== Keranjang Belanja ===")
    for index, item in enumerate(keranjang, 1):
        print(f"{index}. {item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(item['Jumlah'] * item['Harga'])}")
    
    try:
        pilihan = int(input("Masukkan nomor barang yang ingin diubah atau dihapus dari keranjang: "))
        if 1 <= pilihan <= len(keranjang):
            barang_dipilih = keranjang[pilihan - 1]
            print(f"Barang dipilih: {barang_dipilih['Nama']} (Jumlah: {barang_dipilih['Jumlah']})")

            # Cari stok asli dari barang yang dipilih
            barang_asli = next((b for b in barang_dijual if b['No'] == barang_dipilih['No']), None)
            if barang_asli:
                stok_tersedia = barang_asli['Stok']

                # Menanyakan apakah user ingin mengubah atau menghapus barang
                aksi = input("Apakah Anda ingin mengubah jumlah (u) atau menghapus barang (h)? (u/h): ").lower()

                if aksi == 'u':
                    # Validasi pengubahan jumlah barang
                    while True:
                        try:
                            jumlah_baru = int(input(f"Masukkan jumlah baru untuk {barang_dipilih['Nama']} (maksimal {stok_tersedia}): "))
                            if jumlah_baru <= 0:
                                print("Jumlah harus lebih dari 0.")
                            elif jumlah_baru > stok_tersedia:
                                print(f"Jumlah tidak boleh melebihi stok yang tersedia. Stok saat ini: {stok_tersedia}.")
                            else:
                                barang_dipilih['Jumlah'] = jumlah_baru
                                print(f"Jumlah {barang_dipilih['Nama']} berhasil diubah menjadi {jumlah_baru}.")
                                break
                        except ValueError:
                            print("Invalid input. Masukkan angka.")
                elif aksi == 'h':
                    # Menghapus barang dari keranjang
                    keranjang.pop(pilihan - 1)
                    print(f"Barang {barang_dipilih['Nama']} berhasil dihapus dari keranjang.")
                else:
                    print("Pilihan tidak valid.")
            else:
                print("Barang tidak ditemukan dalam daftar stok.")
        else:
            print("Nomor barang tidak valid.")
    except ValueError:
        print("Input tidak valid, silakan masukkan nomor yang benar.")

# Fungsi untuk melihat barang yang ada di keranjang pembeli
# lihat_keranjang(): Fungsi ini menampilkan semua barang yang ada di keranjang belanja pembeli, termasuk total harga keseluruhan. 
# Jika keranjang kosong, pesan akan muncul.
def lihat_keranjang():
    if not keranjang:
        print("Keranjang kosong.")
        return
    print("\n=== Keranjang Belanja ===")
    total_harga = 0
    # Menampilkan isi keranjang dan total harga
    for item in keranjang:
        subtotal = item['Jumlah'] * item['Harga']
        print(f"{item['Nama']} (Jumlah: {item['Jumlah']}) - Rp{int(subtotal)}")
        total_harga += subtotal
    print(f"Total harga: Rp{int(total_harga)}")

# Fungsi checkout untuk pembeli
# checkout(): Fungsi ini digunakan untuk menyelesaikan pembelian. Detail barang yang akan di-checkout, termasuk diskon jika ada, ditampilkan. 
# Setelah pembeli mengonfirmasi, stok barang akan diperbarui, dan riwayat transaksi disimpan. Keuntungan dari penjualan juga diperbarui.
def checkout(username):
    if not keranjang:
        print("Keranjang belanja Anda kosong.")
        return

    total_harga = 0
    transaksi = {'Pembeli': username, 'Barang': [], 'Total': 0}

    # Tampilkan detail barang yang akan di-checkout dalam format tabel
    print("\n=== Detail Barang yang Akan Di-checkout ===")
    print(f"{'No':<3} {'Nama Barang':<17} {'Jumlah':<9} {'Harga Satuan':<18} {'Total':<14} {'Diskon':<9} {'Harga Akhir':<15}")
    print("="*90)

    for idx, item in enumerate(keranjang, 1):
        barang = next((b for b in barang_dijual if b['No'] == item['No']), None)
        
        if barang and barang['Stok'] >= item['Jumlah']:
            harga_total_item = item['Jumlah'] * barang['Harga Jual']
            diskon = 0  # No discount logic specified, so 0
            harga_setelah_diskon = harga_total_item - diskon
            total_harga += harga_setelah_diskon
            transaksi['Barang'].append({'Nama': barang['Nama'], 'Jumlah': item['Jumlah'], 'Harga Jual': barang['Harga Jual']})
            print(f"{idx:<3} {item['Nama']:<17} {item['Jumlah']:<9} Rp{int(barang['Harga Jual']):<18} Rp{int(harga_total_item):<14} {diskon:<9} Rp{int(harga_setelah_diskon):<15}")
        else:
            print(f"Stok tidak mencukupi untuk {item['Nama']} atau barang tidak ditemukan.")
            return

    print("="*90)
    print(f"Total Harga Akhir: Rp{int(total_harga)}")

    konfirmasi = input("Konfirmasi pembelian (y/n): ").lower()
    if konfirmasi == 'y':
        for item in keranjang:
            barang = next((b for b in barang_dijual if b['No'] == item['No']), None)
            if barang:
                barang['Stok'] -= item['Jumlah']
        transaksi['Total'] = total_harga
        riwayat_transaksi.append(transaksi)
        keranjang.clear()
        print("Pembelian berhasil!")
    else:
        print("Pembelian dibatalkan.")

def beli_barang(username):
    tampilkan_barang('customer')
    try:
        no_barang = int(input("Masukkan nomor barang yang ingin dibeli: "))
    except ValueError:
        print("Invalid input. Masukkan angka.")
        return
    for barang in barang_dijual:
        if barang['No'] == no_barang:
            while True:
                try:
                    qty = int(input("Masukkan jumlah yang ingin dibeli: "))
                    if qty <= 0:
                        print("Error: Quantity must be greater than zero.")
                    elif qty > barang['Stok']:
                        print(f"Error: Insufficient stock for {barang['Nama']}. Only {barang['Stok']} available.")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Masukkan angka.")
                    return
            total = barang['Harga Jual'] * qty
            barang['Stok'] -= qty
            print(f"Purchased {qty} x {barang['Nama']} for Rp{int(total):,}. Thank you!")
            transaksi = {'Pembeli': username, 'Barang': [{'Nama': barang['Nama'], 'Jumlah': qty, 'Harga Jual': barang['Harga Jual']}], 'Total': total}
            riwayat_transaksi.append(transaksi)
            return
    print("Barang tidak ditemukan.")

def customer_menu(username):
    while True:
        print("\nCustomer Menu")
        print("1. View All Items")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Edit or Remove from Cart")
        print("5. Checkout")
        print("6. Exit")
        choice = input("Enter the number of your choice (1-6): ").strip()
        if choice == '1':
            tampilkan_barang('customer')
        elif choice == '2':
            tambah_ke_keranjang()
        elif choice == '3':
            lihat_keranjang()
        elif choice == '4':
            ubah_atau_hapus_keranjang()
        elif choice == '5':
            checkout(username)
        elif choice == '6':
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(username):
    while True:
        print("\nUser Menu")
        print("1. View All Items")
        print("2. Add New Item")
        print("3. Edit Item")
        print("4. Delete Item")
        print("5. View Transaction History")
        print("6. Purchase Item")
        print("7. Exit")
        choice = input("Enter the number of your choice (1-7): ").strip()
        if choice == '1':
            tampilkan_barang('user')
        elif choice == '2':
            tambah_barang()
        elif choice == '3':
            ubah_barang()
        elif choice == '4':
            hapus_barang()
        elif choice == '5':
            lihat_riwayat_transaksi_penjual()
        elif choice == '6':
            beli_barang(username)
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    print("Welcome to the Han Bookstore!")
    while True:
        print("\nChoose your role:")
        print("1. Customer")
        print("2. Admin (User)")
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            username = "customer"
            customer_menu(username)
            break
        elif choice == '2':
            username = "admin"
            user_menu(username)
            break
        else:
            print("Invalid choice. Please try again.")
