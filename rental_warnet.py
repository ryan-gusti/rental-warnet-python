#=== Dokumentasi untuk Program Rental Warnet Maju Jaya ===

"""
Mengimport library datetime yang berfungsi untuk konversi string menjadi satuan jam
"""
import datetime

"""
### List Fungsi pada program ini
Fungsi untuk mengkonversi dari string menjadi satuan jam menggunakan library datetime
"""
def konversi(jam):
    return datetime.datetime.strptime(jam, '%H:%M')

"""
Fungsi untuk menghitung selisih penyewaan yang didapatkan dari jam mulai dan jam selesai
"""
def selisih(mulai, selesai):
    hasil = selesai - mulai
    lama_jam = hasil.days * 24 + hasil.seconds / 3600
    return lama_jam

"""
Fungsi untuk menghitung total bayar penyewa dengan cara mengkali total jam sewa dengan Rp3000
"""
def hitung_bayar(lama_jam):
    total = lama_jam * 3000
    return total

"""
Fungsi untuk menampilkan data pembayaran untuk penyewa komputer
"""
def pembayaran(nama, notelp, lama_jam, total):
    print("- Data Pembayaran -")
    print("Nama Pembeli : ", nama)
    print("Nomor Telp Pembeli : ", notelp)
    print("Lama Jam Sewa : ", lama_jam, "jam")
    print("Total Bayar : Rp", total)

"""
### Menu Awal Program
Ucapan selamat datang dan perintah untuk mengisi inputan yang berisi
list variabel untuk menyimpan data penyewa

1. **nama** - untuk menyimpan nama penyewa
2. **notelp** - untuk menyimpan nomor telpon penyewa
3. **mulai** - untuk menyimpan jam mulai sewa
4. **selesai** - untuk menyimpan jam selesai sewa

"""
print("Selamat Datang di Warnet Maju Jaya")
print("Silahkan Isi Data Berikut")
nama = input("Nama Anda : ")
notelp = input("Nomor Telepon Anda : ")
mulai = input("Input Jam Mulai Sewa : ",)
selesai = input("Input Jam Selesai Sewa : ")

"""
### Algoritma pada program
1. mengkonversi nilai string pada variabel **mulai** dan **selesai**
2. menghitung selisih dari kedua variabel tersebut dengan cara menguranginya
3. menghitung total bayar yang didapatkan dari selisih dan dikali 3000
4. menampilkan hasil pada pembayaran
"""
mulai = konversi(mulai)
selesai = konversi(selesai)
lama_jam = selisih(mulai, selesai)
total = hitung_bayar(lama_jam)
pembayaran(nama, notelp, lama_jam, total)

