Belajar Pemrograman Berorientasi Objek (OOP) dengan Python untuk SMP
Apa Itu OOP?
OOP adalah cara menulis program dengan membagi kode menjadi class dan object.

Class: Seperti cetakan kue. Cetakan ini bisa membuat banyak kue yang bentuknya sama.
Object: Adalah hasil dari cetakan, seperti kue yang sudah jadi.
Konsep Penting OOP
1. Class (Cetakan)
Class adalah seperti cetakan untuk membuat objek. Di dalamnya, kita bisa membuat atribut (sifat) dan metode (kegiatan).

Contoh:

python
Copy code
class Kucing:
    nama = "Milo"  # Sifat (atribut)

    def meong(self):  # Kegiatan (metode)
        print("Meooong!")
2. Object (Hasil Cetakan)
Object adalah hasil dari class. Misalnya, kucing yang kita buat dari cetakan class.

Contoh:

python
Copy code
kucingku = Kucing()  # Membuat objek dari class Kucing
print(kucingku.nama)  # Output: Milo
kucingku.meong()  # Output: Meooong!
Fitur Keren OOP
1. Constructor (Pembangun Objek)
Constructor adalah metode khusus untuk memberikan sifat ke objek saat dibuat.

Contoh:

python
Copy code
class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

    def perkenalan(self):
        print(f"Halo, namaku {self.nama} dari kelas {self.kelas}.")

siswa1 = Siswa("Budi", "7A")
siswa1.perkenalan()  # Output: Halo, namaku Budi dari kelas 7A.
2. Pewarisan (Inheritance)
Pewarisan memungkinkan class baru untuk "mewarisi" sifat dan kegiatan dari class lain.

Contoh:

python
Copy code
class Hewan:
    def suara(self):
        print("Hewan membuat suara")

class Anjing(Hewan):
    def suara(self):
        print("Guk guk!")

anjingku = Anjing()
anjingku.suara()  # Output: Guk guk!
3. Polymorphism (Berbagai Bentuk)
Satu metode bisa punya bentuk berbeda tergantung siapa yang menggunakannya.

Contoh:

python
Copy code
class Burung:
    def terbang(self):
        print("Burung bisa terbang")

class Penguin(Burung):
    def terbang(self):
        print("Penguin tidak bisa terbang")

burung1 = Burung()
burung2 = Penguin()

burung1.terbang()  # Output: Burung bisa terbang
burung2.terbang()  # Output: Penguin tidak bisa terbang
Latihan Seru
1. Membuat Sistem Sederhana: Kebun Binatang
Tugas:

Buat class Hewan dengan sifat nama dan kegiatan suara().
Buat class Harimau dan Burung yang mewarisi class Hewan.
Contoh Kode:

python
Copy code
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        print("Hewan ini bersuara.")

class Harimau(Hewan):
    def suara(self):
        print(f"{self.nama}: Auuum!")

class Burung(Hewan):
    def suara(self):
        print(f"{self.nama}: Cuit cuit!")

harimau = Harimau("Harimau Sumatra")
burung = Burung("Burung Merak")

harimau.suara()  # Output: Harimau Sumatra: Auuum!
burung.suara()   # Output: Burung Merak: Cuit cuit!
Kesimpulan
Class: Cetakan untuk membuat objek.
Object: Hasil dari class.
Pewarisan (Inheritance): Class baru mewarisi sifat/kegiatan dari class lama.
Polymorphism: Satu metode bisa punya bentuk berbeda.
Semoga materi ini membantu kamu memahami dasar-dasar OOP di Python! Yuk, coba praktekkan kode-kode di atas. 😊





You said:
buat contoh yg lebih mudah di mengerti
ChatGPT said:
ChatGPT
Berikut adalah contoh program yang lebih sederhana untuk membantu memahami konsep Object-Oriented Programming (OOP) dengan lebih mudah.

Contoh Program Sederhana: Sistem Pemesanan Minuman
Fitur:

Menambahkan pesanan minuman.
Menampilkan pesanan.
Menghitung total harga.
Kode:

python
Copy code
class Drink:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_info(self):
        print(f"{self.name} - Rp{self.price}")


class DrinkOrder:
    def __init__(self):
        self.orders = []

    def add_order(self, name, price):
        drink = Drink(name, price)  # Membuat objek minuman
        self.orders.append(drink)  # Menambahkan ke daftar pesanan
        print(f"{name} telah ditambahkan ke pesanan.")

    def show_orders(self):
        if not self.orders:  # Jika tidak ada pesanan
            print("Belum ada pesanan.")
            return
        print("Daftar Pesanan:")
        for drink in self.orders:  # Menampilkan semua pesanan
            drink.display_info()

    def calculate_total(self):
        total = sum(drink.price for drink in self.orders)  # Menghitung total harga
        print(f"Total Harga: Rp{total}")


# Pemakaian
order = DrinkOrder()
order.add_order("Es Teh", 5000)
order.add_order("Kopi Hitam", 10000)
order.show_orders()
order.calculate_total()
Penjelasan
Class Drink:

Merepresentasikan minuman dengan atribut name (nama) dan price (harga).
Memiliki metode display_info untuk menampilkan informasi minuman.
Class DrinkOrder:

Merepresentasikan daftar pesanan.
Memiliki daftar (list) untuk menyimpan objek minuman.
Metode:
add_order untuk menambahkan pesanan.
show_orders untuk menampilkan semua pesanan.
calculate_total untuk menghitung total harga.
Output Program:

yaml
Copy code
Es Teh telah ditambahkan ke pesanan.
Kopi Hitam telah ditambahkan ke pesanan.
Daftar Pesanan:
Es Teh - Rp5000
Kopi Hitam - Rp10000
Total Harga: Rp15000
Program ini lebih sederhana, tetapi tetap menunjukkan konsep dasar OOP seperti:

Class dan Object: Drink adalah class, dan setiap minuman adalah objek.
Encapsulation: Data (nama dan harga minuman) terbungkus dalam class.
Method: Fungsi-fungsi dalam class membantu mengorganisasi kode dengan baik.
