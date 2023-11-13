# Aplikasi CRUD Perpusatakaan Purwadhika
    Aplikasi ini dirancang untuk mempermudah pengelolaan daftar buku di perpustakaan. 
    Dengan fitur-fitur yang disediakan, Anda dapat dengan mudah menambahkan, mengubah, menghapus buku, serta melakukan peminjaman dan pengembalian buku.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

## Fitur Aplikasi Perpusatakaan
1. Menampilkan Daftar Buku
2. Menambah Daftar Buku
3. Mengubah Daftar Buku
4. Menghapus Daftar Buku
5. Meminjam Buku
6. Mengembalikan Buku
7. Exit Program

# 1. Menampilkan Daftar Buku 

    Pada menu ini, dengan memilih menu nomor 1 (Tampilkan semua buku), user dapat menampilkan daftar buku.
    Daftar buku dapat ditampilkan secara keseluruhan atau dapat memilih daftar buku menurut ID Buku yang diinginkan melalui menu 2 (Mencari Buku).
  

# 2. Menambah Aplikasi Perpustakaan 

    Pada menu ini, dengan menu nomor 2 (menambah daftar buku), user akan diminta untuk memasukkan informasi seperti ID Buku, Judul Buku, Penulis, Penerbit, Genre, dan Stok Buku jika memenuhi           syarat dan ketentuan. 
    Dimana ID Buku tidak boleh sama dengan ID Buku yang sudah tersedia di Perpusatakaan agar tidak terjadinya kode ID Buku yang duplikat. 
    Setelah memenuhi syarat, User dapat menambahkan Buku yang diinginkan ke dalam Aplikasi. 
    Setelah itu, User diminta untuk apakah Anda ingin untuk menyimpan ke dalam sistem jika User menekan Iya maka akans secara otomatis tersimpan ke dalam sistem.
    
# 3. Mengubah Aplikasi Perpusatakaan 
    
    Pada menu ini, dengan menu nomor 3 (mengubah daftar buku), user akan diminta untuk memasukkan ID Buku yang terdapat di sistem jika ingin melakukan update ke sistem. 
    Jika sudah memenuhi syarat maka akan muncul sebuah pesan yang menanyakan kepada User kategori apa yang ingin diubah;
    1. ID Buku 
    2. Judul Buku
    3. Penulis
    4. Penerbit
    5. Genre
    6. Stok Buku
    Jika sudah menentukan kategori yang ingin diubah maka akan secara otomatis data yang sudah diupload akan terupdate. 
    
# 4. Menghapus Aplikasi Perpusatakaan  

    Pada menu ini, dengan menu nomor 4(menghapus daftar buku), user akan diminta untuk memasukkan ID Buku yang ingin dihapus sesuai atau yang terdapat di sistem. 
    Apabila ID Buku tidak terdeteksi di sistem maka akan muncul tulisan " Maaf, Data yang ingin Anda hapus tidak ada. Silahkan menghapuskan data yang tersedia!". 
    Dengan demikian, apabila User telah memasukkan ID Buku yang sesuai maka data akan terhapus di sistem.
    
# 5. Meminjam Aplikasi Perpustakaan 
    Pada menu ini, dengan menu nomor 5(meminjam buku), user akan diminta untuk memasukkan ID Buku yang ingin dipinjam sesuai atau yang terdapat di sistem. 
    Setelah menambah buku yang ingin dipinjam ke dalam keranjang maka akan ditanya berapa jumlah buku yang ingin dipinjam dimana apabila jumlah yang dipinjam lebih banyak dari stok yang ada maka       tentu tidak akan bisa karena melebihi batas stok. 
    Sedangkan apabila jumlah yang dipinjam lebih sedikit dari stok buku yang tersedia maka akan muncul pesan untuk melakukan konfirmasi pinjaman buku yang ingin dipinjam.

# 6. Mengembalikkan Aplikasi Perpusatakaan
    pada menu ini, dengan menu nomor 6(mengembalikkan buku), user akan diminta untuk memasukkan ID Buku yang telah dipinjam sebelumnya. 
    Setelah memasukkan ID Buku yang sesuai maka akan terdapat sebuah pesan untuk berapa jumlah buku yang ingin dikembalikkan. 
    Setelah, user mengembalikkan jumlah buku yang sesuai tidak melebihi dari stok buku maka akan muncul pesan Buku yang Anda pinjam berhasil dikembalikan!

# 7. Menu Keluar Aplikasi Perpustakaan
    Pada navigasi yang terakhir ini, apabila user memasukan input 7, maka pengguna akan keluar dari program. 
    Pada aplikasi ini kita dapat menggunakan fungsi untuk menjalankan fitur CRUD (Create, Read, Update dan Delete) untuk mengelola daftar buku di perpusatakaan.

