# HALO SEKARANG KITA BERADA DI HARI KEDUA BELAJAR BAHASA PYTHON GUYSSS !!!!
# DI HARI KEDUA KITA BAHAS APA NIH ?

# DI HARI KEDUA KITA AKAN MEMBAHAS MATERI MENGENAI VARIABLE PADA BAHASA PYTHON
# VARIABLE DI PYTHON BERMACAM MACAM LOHHH !!!

# YUK KITA MASUK KE MATERI NYA

# Variable di python guna nya untuk apasih??
# Variable di python berguna untuk menampung sebuah nilai atau value yang akan kita tuliskan.
# bagaimana sih contohnya dari variable?

# di pembelajaran kemarin kita juga sudah menulis variable loh
# ayo kita buat lagi

nama_pertama = "Rizky"
nama_kedua = "Wahyudi"
nama_lengkap = "Rizky Wahyudi"
print(nama_pertama)
print(nama_kedua)
print(nama_lengkap)

# oke kalian sudah tau apa itu variable, sekarang kita lanjut.
# di variable ada jenis jenis nya juga, seperti string, integer, float

# maksudnya kayak gimana tuh? nah contoh variable yang tipe data nya string seperti diatas
# string --->>> biasanya menggunakan kutip "" / ''
# integer ---->>> biasanya angka biasa / angka bulat
# float --->>> angka juga, cuma koma - koma an

# langsung kita ke prakteknya 
x = "Ini tipe data string" # ini contoh dari tipe data string
y = 342 # ini contoh dari tipe data integer
z = 34.67 # ini contoh dari tipe data float
print(x)
print(y)
print(z)
# atau bisa menuliskan nya seperti ini :
x = str("ini string")
y = int(342)
z = float(34)
print(x)
print(y)
print(z)
# bagaimana jika kita ingin tau atau melihat langsung sistem yang menunjukkan tipe data tersebut?
# kita bisa menggunakan cara seperti ini :
x = "Wahyu"
y = 435
z = 342.32
print(type(x))
print(type(y))
print(type(z))

# oke bang, tapi kalo kita make kutip satu untuk tipe data string bagaimana bang? apakah tetap berjalan?
# ya, tetap berjalan, nilai nya sama kok
kutip_dua = "Ini kutip dua"
kutip_satu = 'Ini kutip dua'
print(kutip_dua)
print(kutip_satu)
# sama saja

# python juga meiliki case sensitive 
# case sensitive apa? arti nya sistem python sangat memperhatikan ketikan kita, seperti besar kecil huruf dll
# contohnya seperti ini :
a = "Kocak"
A = "Ya kocak"
print(A)
# yang akan ke print ==> A = "Ya kocak", karena kita memanggil variabel dengan A yang besar 