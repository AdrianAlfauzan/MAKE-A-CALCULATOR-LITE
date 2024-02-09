import tkinter as tk
from tkinter import ttk


def tambahkan_ke_input(nilai):
    input_value = input_entry.get()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_value + nilai)


def hitung_hasil():
    input_value = input_entry.get()
    try:
        # Evaluasi ekspresi matematika
        hasil = eval(input_value)
        input_entry.delete(0, tk.END)
        input_entry.insert(0, str(hasil))
    except Exception as e:
        # Tampilkan pesan kesalahan jika ekspresi tidak valid
        input_entry.delete(0, tk.END)
        input_entry.insert(0, "Error")


def hapus_input():
    input_entry.delete(0, tk.END)


kotak = tk.Tk()
kotak.configure(bg="lightblue")
kotak.geometry("350x400")
kotak.resizable(True, True)
kotak.title("Calculator")

# Membuat frame dan mengatur style
input_frame = ttk.Frame(kotak)
input_frame.pack(pady=80, padx=0, fill="both", expand=True)

input_entry = ttk.Entry(input_frame, width=50)
input_entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Menggunakan grid layout untuk tombol pertama
Tombol_Button1 = ttk.Button(
    input_frame, text="1", width=10, command=lambda: tambahkan_ke_input("1")
)
Tombol_Button1.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol kedua di sebelah kanan
Tombol_Button2 = ttk.Button(
    input_frame, text="2", width=10, command=lambda: tambahkan_ke_input("2")
)
Tombol_Button2.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol kedua di sebelah kanan
Tombol_Button3 = ttk.Button(
    input_frame, text="3", width=10, command=lambda: tambahkan_ke_input("3")
)
Tombol_Button3.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

# Menggunakan grid layout untuk tombol pertama
Tombol_Button4 = ttk.Button(
    input_frame, text="4", width=10, command=lambda: tambahkan_ke_input("4")
)
Tombol_Button4.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol kedua di sebelah kanan
Tombol_Button5 = ttk.Button(
    input_frame, text="5", width=10, command=lambda: tambahkan_ke_input("5")
)
Tombol_Button5.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol kedua di sebelah kanan
Tombol_Button6 = ttk.Button(
    input_frame, text="6", width=10, command=lambda: tambahkan_ke_input("6")
)
Tombol_Button6.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

# Menggunakan grid layout untuk tombol pertama
Tombol_Button7 = ttk.Button(
    input_frame, text="7", width=10, command=lambda: tambahkan_ke_input("7")
)
Tombol_Button7.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol kedua di sebelah kanan
Tombol_Button8 = ttk.Button(
    input_frame, text="8", width=10, command=lambda: tambahkan_ke_input("8")
)
Tombol_Button8.grid(row=3, column=1, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol kedua di sebelah kanan
Tombol_Button9 = ttk.Button(
    input_frame, text="9", width=10, command=lambda: tambahkan_ke_input("9")
)
Tombol_Button9.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

# Menambahkan tombol delete,titik,samadengan, kali,bagi,tambah,kurang
Tombol_delete = ttk.Button(input_frame, text="Delete", width=10, command=hapus_input)
Tombol_delete.grid(row=1, column=3, padx=10, pady=10, sticky="nsew")

Tombol_titik = ttk.Button(
    input_frame, text=".", width=10, command=lambda: tambahkan_ke_input(".")
)
Tombol_titik.grid(row=2, column=3, padx=10, pady=10, sticky="nsew")

Tombol_kurang = ttk.Button(
    input_frame, text="-", width=10, command=lambda: tambahkan_ke_input("-")
)
Tombol_kurang.grid(row=3, column=3, padx=10, pady=10, sticky="nsew")

Tombol_kali = ttk.Button(
    input_frame, text="X", width=10, command=lambda: tambahkan_ke_input("*")
)
Tombol_kali.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

Tombol_bagi = ttk.Button(
    input_frame, text="/", width=10, command=lambda: tambahkan_ke_input("/")
)
Tombol_bagi.grid(row=4, column=1, padx=10, pady=10, sticky="nsew")

Tombol_tambah = ttk.Button(
    input_frame, text="+", width=10, command=lambda: tambahkan_ke_input("+")
)
Tombol_tambah.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

Tombol_samadengan = ttk.Button(input_frame, text="=", width=10, command=hitung_hasil)
Tombol_samadengan.grid(row=4, column=3, padx=10, pady=10, sticky="nsew")

kotak.mainloop()
