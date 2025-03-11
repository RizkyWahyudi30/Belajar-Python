# HALO SEMUANYA, SELAMAT DATANG KEMBALI DI HARI KEEMPAT INIIII !!!
# KARNA KEMARIN KITA SUDAH MEMBAHAS TENTANG VARIABLES NAME
# SEKARANG KITA AKAN MEMBAHAS LAGI NIH TENTANG VARIABLE

# APA BEDA NYA BANG?
# PADA MATERI INI KITA AKAN MEMBAHAS TENTANG OUTPUT VARIABLE

# MAKSUDNYA KITA AKAN MEMBAHAS HASIL OUTPUT DARI KODINGAN YANG KITA UDAH PRINT 

# YUK KITA MASUK KE MATERI NTA, LETSGOOO

'''
Kalo yang kita tau, kalo ingin meng-running kode python
kita bisa menuliskan kode "print()"

nah kita bisa melalakukan penggabungan variable lewat print()

yuk kita lihat
'''

# kita buat dulu variable nya

KataSatu = "Halo"
KataDua = ", nama saya"
KataTiga = " Rinuu"
print(KataSatu + KataDua + KataTiga)
# kita memakai tanda tambah untuk mengartikan menyambungkan variable lain yang kita buat

'''
Bang, terus kalo semisalnya kita mau gabungin variable yang tipe data nya beda gimana?

Nah, untuk yang ditambahkan dalam artian menggabungkan itu hanya bisa di tipe data string

Mari kita contohkan :
'''

# bagaimana jika kita ingin menggabungkan string dan integer
VarStr = "Ini String"
VarInt = 3
# print(VarStr + VarInt) # ===> ini akan terjadi error
'''
ini bentuk contoh eror nya :

Traceback (most recent call last):
  File "D:\coding\python\python-web3\belajar-hari-keempat.py", line 40, in <module>
    print(VarStr + VarInt)
          ~~~~~~~^~~~~~~~
TypeError: can only concatenate str (not "int") to str
'''

# terus gimana bang biar kegabung? Nah kita bisa pakai koma

# Untuk tambahan, kita tidak usah buat variabel lagi, kita pakai variabel yang atas aja, kita tinggal print aja.
print(VarStr, VarInt) # ===> gimana bang outputnya? Kalian coba sendiri

# Nah si koma ini juga bisa ketika kita mau menggabungkan variable antara Ineteger dan Boolean :
x = 2
y = 2.3
print(x, y)

'''
Nah sekarang kalian sudah paham?

Jika kita memakai + untuk string, kata kata nya akan berdempetan,
Jika kita memakai , maka akan mempunyai spasi nya sendiri

Gituu cuy
'''

# NAH MUNGKIN SEKIAN MATERI NYA GAIS, LANJUT BESOKK