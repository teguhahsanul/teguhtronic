import tkinter as tk
from tkinter import ttk

# Inisialisasi data produk
produk = {
    1: {'nama': 'Laptop', 'harga': 8000000, 'stok': 10},
    2: {'nama': 'Smartphone', 'harga': 5000000, 'stok': 15},
    3: {'nama': 'TV', 'harga': 6000000, 'stok': 8},
    4: {'nama': 'Kamera', 'harga': 7000000, 'stok': 5},
    # Tambahkan produk lain di sini jika diperlukan
}

# Fungsi untuk menampilkan produk
def tampilkan_produk():
    tree.delete(*tree.get_children())
    for id_produk, data in produk.items():
        tree.insert('', 'end', values=(id_produk, data['nama'], data['harga'], data['stok']))

# Fungsi untuk melakukan transaksi
def transaksi():
    keranjang = {}
    total_belanja = 0
    while True:
        try:
            pilihan = entry_produk.get()
            if pilihan == "0":
                break
            if not pilihan.isdigit():
                raise ValueError("Masukkan ID produk yang valid")
            pilihan = int(pilihan)
            if pilihan in produk and produk[pilihan]['stok'] > 0:
                if pilihan in keranjang:
                    keranjang[pilihan]['qty'] += 1
                else:
                    keranjang[pilihan] = {'nama': produk[pilihan]['nama'], 'harga': produk[pilihan]['harga'], 'qty': 1}
                produk[pilihan]['stok'] -= 1
                total_belanja += produk[pilihan]['harga']
            else:
                label_notif.config(text="Produk tidak tersedia atau stok habis.")
        except ValueError as e:
            label_notif.config(text=str(e))
    
    # Menampilkan detail transaksi
    transaksi_text = "Detail Transaksi:\nNama\t\tHarga\tQty\tTotal\n"
    for item in keranjang.values():
        subtotal = item['harga'] * item['qty']
        transaksi_text += f"{item['nama']}\t{item['harga']}\t{item['qty']}\t{subtotal}\n"
    
    transaksi_text += f"\nTotal Pembelian: {total_belanja}"
    label_transaksi.config(text=transaksi_text)
    tampilkan_produk()

# Buat window Tkinter
root = tk.Tk()
root.title("Teguh Tronic")

# Buat tabel untuk menampilkan produk
tree = ttk.Treeview(root, columns=('ID', 'Nama', 'Harga', 'Stok'), show='headings')
tree.heading('ID', text='ID')
tree.heading('Nama', text='Nama')
tree.heading('Harga', text='Harga')
tree.heading('Stok', text='Stok')
tree.grid(row=0, column=0, padx=10, pady=5)

# Tampilkan produk saat aplikasi dijalankan
tampilkan_produk()

# Label dan entry untuk produk
label_produk = tk.Label(root, text="Masukkan ID Produk:")
label_produk.grid(row=1, column=0, padx=10, pady=5)

entry_produk = tk.Entry(root)
entry_produk.grid(row=2, column=0, padx=10, pady=5)

# Tombol untuk transaksi
button_transaksi = tk.Button(root, text="Mulai Transaksi", command=transaksi)
button_transaksi.grid(row=3, column=0, padx=10, pady=5)

# Label untuk notifikasi dan transaksi
label_notif = tk.Label(root, text="")
label_notif.grid(row=4, column=0, padx=10, pady=5)

label_transaksi = tk.Label(root, text="")
label_transaksi.grid(row=5, column=0, padx=10, pady=5)

root.mainloop()
