# Perpusatakan_Juwantoro 
# Daftar Buku yang ada di Perpustakaan Juwantoro, User Silahkan Masukkan daftar buku

List_Daftar_Buku = [
    {
        "ID_Buku"       : "001",
        "Judul_Buku"    : "Hitler's Secrets",
        "Penulis"       : "Adam Lebor",
        "Penerbit"      : "Citadel Press",
        "Genre"         : "Historical",
        "stok_buku"     : 5,
    }
    ,{
        "ID_Buku"       : "002",
        "Judul_Buku"    : "The Middle Stories",
        "Penulis"       : "Sheila Heti",
        "Penerbit"      : "House of Anansi Press",
        "Genre"         : "Fiction",
        "stok_buku"     : 2,
    }
    ,{
        "ID_Buku"       : "003",
        "Judul_Buku"    : "Our Dumb",
        "Penulis"       : "The Onion",
        "Penerbit"      : "Three Rivers Press",
        "Genre"         : "Humoresque",
        "stok_buku"     : 3,
    }
    ,{
        "ID_Buku"       : "004",
        "Judul_Buku"    : "Tell Me Now",
        "Penulis"       : "Robynn Clairday",
        "Penerbit"      : "Scholastic",
        "Genre"         : "Fantasy",
        "stok_buku"     : 7,
    }
    ,{
        "ID_Buku"       : "005",
        "Judul_Buku"    : "Pigs in Heaven",
        "Penulis"       : "Barbara Kingsolver",
        "Penerbit"      : "Harpercollins",
        "Genre"         : "Non-Fiction",
        "stok_buku"     : 4,
    }
]


# 1A. Kerangka atau template untuk menampilkan tabel Daftar Buku di perpusatakaan Juwantoro  

# CARA otomatis membuat tabel utama menggunakan tabulate agar tabel rapi.
from tabulate import tabulate

def Tabel_Daftar_Buku(list_Data_Buku):
    headers = ["ID_Buku", "Judul_Buku", "Penulis", "Penerbit", "Genre", "stok_buku"]
    table_data = []

    for data in list_Data_Buku:
        baris = [data["ID_Buku"], data["Judul_Buku"], data["Penulis"], data["Penerbit"], data["Genre"], data["stok_buku"]]
        table_data.append(baris)

    print(tabulate(table_data, headers, tablefmt="grid"))


# CARA otomatis menggunakan tabulate untuk menunjukkan daftar sebelum di update 
from tabulate import tabulate

def Tabel_Daftar_Buku_Update(list_Data, x, Data_Baru):
    headers = ["ID_Buku", "Judul_Buku", "Penulis", "Penerbit", "Genre", "stok_buku"]
    table_data = []

    for data in list_Data:
        baris = [data["ID_Buku"], data["Judul_Buku"], data["Penulis"], data["Penerbit"], data["Genre"], data["stok_buku"]]
        table_data.append(baris)

    for baris in table_data:
        baris[x - 1] = Data_Baru

    print(tabulate(table_data, headers=headers, tablefmt="grid"))


# CARA otomatis menggunakan tabulate untuk menunjukkan tabel keranjang
from tabulate import tabulate

def Tabel_Daftar_Buku_Keranjang(list_Data):
    headers = ["ID_Buku", "Judul_Buku", "Qty","Tanggal_Pinjam"]
    table_data = []

    for data in list_Data:
        baris = [data["ID_Buku"], data["Judul_Buku"], data["Qty"], data["Tanggal_Pinjam"]]
        table_data.append(baris)

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

# 2A. Fungsi untuk mencari buku dalam DaftarBuku berdasarkan ID Buku yang diinputkan.

#Cara 1 menggunakan Reguler Function untuk memfilter berdasarkan ID Buku

def CariDaftar(Input):
    def Mencocokan(data):
        return data["ID_Buku"] == str(Input)
    DaftarCari = list(filter(Mencocokan, List_Daftar_Buku))
    return DaftarCari

# Cara 2 menggunakan Lambda Function untuk memfilter berdasarkan ID Buku

def CariDaftar(Input):
    DaftarCari = (list(filter(lambda data: data['ID_Buku'] == str(Input), List_Daftar_Buku)))
    return DaftarCari

# 3A. Fungsi Read atau Menampilkan 

def read():
     Input_Read=(int(input("""Menu Menampilkan Daftar Buku:
1. Tampilkan semua buku
2. Mencari buku
3. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan: """)))  

     if Input_Read == 1: 
        Tabel_Daftar_Buku(List_Daftar_Buku) 
     elif Input_Read == 2:
         while True:
            ID_Buku = (str(input("\n\tMasukkan ID Buku yang ingin Anda cari:")))
            hasil_pencarian = CariDaftar(ID_Buku)
            if hasil_pencarian: 
               Tabel_Daftar_Buku(hasil_pencarian)
               break
            else:
                print("\n\t Tidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
                
     elif Input_Read == 3: 
        Menu()
     else: 
        print("\n\t Tidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
     read()

# 1B. Fungsi ADD atau Menambah

def add(List_Daftar_Buku):
    input_add = (int(input("""Menu Menambah Daftar Buku:
1. Menambah daftar buku
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:""")))

    if input_add == 1:   
        add_ID_Buku_Baru    = str(input("\tMasukkan ID Buku yang ingin Anda tambahkan:"))
        list_value          = [str(value) for data_buku in List_Daftar_Buku for value in data_buku.values()] 
        if str(add_ID_Buku_Baru) in list_value:
            print("\n\tData yang Anda input sudah terdapat di sistem\n")
            return(add(List_Daftar_Buku))   
        else:
            add_Judul_Buku_Baru     = input("\tSilahkan masukkan judul:")
            add_Penulis_Baru        = input("\tSilahkan masukkan nama penulis:")
            add_Penerbit_Baru       = input("\tSilahkan masukkan penerbit:")
            add_Genre_Baru          = input("\tSilahkan masukkan genre:")
            add_stok_buku_Baru      = int(input("\tSilahkan masukkan stok:"))
            List_Daftar_buku_Baru   = [{
				"ID_Buku"       : add_ID_Buku_Baru,
				"Judul_Buku"    : add_Judul_Buku_Baru,
				"Penulis"       : add_Penulis_Baru,
				"Penerbit"      : add_Penerbit_Baru,
				"Genre"         : add_Genre_Baru,
				"stok_buku"     : add_stok_buku_Baru
			}]

            Tabel_Daftar_Buku(List_Daftar_buku_Baru)
            penyimpanan_data = (input("\n\t Apakah Anda ingin menyimpan Data ke sistem (ya/tidak)?")).lower()
            if penyimpanan_data == "ya":
                List_Daftar_Buku += (List_Daftar_buku_Baru)
                Tabel_Daftar_Buku(List_Daftar_Buku)
                print("\n\tData buku baru tersimpan!")
            else:
                print("\n\tData tidak tersimpan!")
    elif input_add == 2:
        Menu()
    else:
        print("\n\tTidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
    add(List_Daftar_Buku)


# 1C CARA 1: Fungsi untuk melakukan update buku sesuai kolomnya

def Update_Barang(Data, Kolom, Data_baru):
    Input_Update_Buku = (input("\t Apakah data yang diupdate sudah sesuai? (Ya/Tidak): "))
    if Input_Update_Buku == "ya":
        Data[0][Kolom] = Data_baru
        print("\tData yang Anda upload sudah diupdate!")
    elif Input_Update_Buku == "tidak":
        print("\t Data yang Anda upload tidak diupdate!")
    else:
        print("\tInput tidak valid. Harap masukkan 'Ya' atau 'Tidak'.")


# 3C Fungsi Update atau Mengubah
def update():
    input_update = (int(input('''Menu Mengubah Daftar Buku:
1. Mengubah daftar buku
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:''')))
    
    if input_update == 1:
        Update_Buku = str(input("\tMasukkan ID Buku yang ingin Anda ubah:"))
        list_value  = [str(value) for data_buku in List_Daftar_Buku for value in data_buku.values()]
        if Update_Buku not in list_value:
            print("\n\tData yang Anda input tidak terdapat di sistem silahkan masukkan kembali ID Buku yang benar\n")
        
        else:
            CariDaftar(Update_Buku)
            Tabel_Daftar_Buku(CariDaftar(Update_Buku))
            input_update = (input("\tApakah Anda yakin ingin melakukan update data berikut? (Ya/Tidak): ")).lower()
            if input_update== "ya":
                input_kategori = int(input("""\tKategori Database Buku: 
    1. ID Buku 
    2. Judul Buku
    3. Penulis
    4. Penerbit
    5. Genre
    6. Stok Buku
    Masukkan kategori yang ingin diubah: """))
                
                if input_kategori == 1:
                    Masukkan_Data = str(input("\tMasukkan data baru yang ingin diinput: ")).lower()
                    Tabel_Daftar_Buku_Update(CariDaftar(Update_Buku),1,Masukkan_Data)
                    Update_Barang(CariDaftar(Update_Buku), "ID_Buku",Masukkan_Data)

                elif input_kategori == 2:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Buku_Update(CariDaftar(Update_Buku),2,Masukkan_Data)
                    Update_Barang(CariDaftar(Update_Buku), "Judul_Buku",Masukkan_Data)
               

                elif input_kategori == 3:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Buku_Update(CariDaftar(Update_Buku),3,Masukkan_Data)
                    Update_Barang(CariDaftar(Update_Buku), "Penulis",Masukkan_Data)


                elif input_kategori == 4:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Buku_Update(CariDaftar(Update_Buku),4,Masukkan_Data)
                    Update_Barang(CariDaftar(Update_Buku), "Penerbit",Masukkan_Data)


                elif input_kategori == 5:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Buku_Update(CariDaftar(Update_Buku),5,Masukkan_Data)
                    Update_Barang(CariDaftar(Update_Buku), "Genre",Masukkan_Data)


                elif input_kategori == 6:
                    Masukkan_Data = input("\tMasukkan data baru yang ingin diinput: ").lower()
                    Tabel_Daftar_Buku_Update(CariDaftar(Update_Buku),6,Masukkan_Data)
                    Update_Barang(CariDaftar(Update_Buku), "stok_buku",Masukkan_Data)

                else: 
                    print("\tKategori tidak ada!")

    elif input_update == 2:
        Menu()
    else:
        print("\tInput yang Anda masukkan tidak valid. Harap masukkan angka yang tersedia.")
    update()

# Fungsi menghapus daftar buku

def delete():
    input_Delete = (int(input('''Menu Menghapus Daftar Buku:
1. Menghapus Daftar Buku
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:''')))
    
    
    if input_Delete == 1:
        Delete_Buku = str(input("\tMasukkan ID Buku yang ingin Anda ubah:"))
        list_value  = [str(value) for data_buku in List_Daftar_Buku for value in data_buku.values()]
        if Delete_Buku not in list_value:
            print("\n\t Maaf, Data yang ingin Anda hapus tidak ada. Silahkan menghapuskan data yang tersedia!")

        else:
            CariDaftar(Delete_Buku)
            Tabel_Daftar_Buku(CariDaftar(Delete_Buku))
            Menghapus = input("\n\t Hapus Data (Ya/Tidak)?").lower()
            if Menghapus == "ya":            
                for item in CariDaftar(Delete_Buku): 
                    List_Daftar_Buku.remove(item)
                print("\n\t Data yang ingin Anda hapus telah berhasil terhapus!")

            else: 
                print("\n\t Data tidak berhasil terhapus!")
    elif input_Delete == 2:
        Menu()
    else:
        print("\n\tTidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
    delete()

# Fungsi meminjam buku
Keranjang_Buku = []  # Keranjang Buku --> variabel sementara

from datetime import datetime

def borrow():
    input_borrow = int(input('''Menu Meminjam Buku:
1. Meminjam Buku
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan:'''))

    if input_borrow == 1:
        Tabel_Daftar_Buku(List_Daftar_Buku)
        while True:
            Borrow_Buku = str(input("\tMasukkan ID Buku yang ingin Anda pinjam:"))
            list_value = [str(value) for data_buku in List_Daftar_Buku for value in data_buku.values()]

            if Borrow_Buku not in list_value:
                print("\n\t Maaf, Data yang ingin Anda pinjam tidak ada. Silahkan meminjam Buku yang tersedia!")
            else:
                print("\n\t Data yang ingin Anda pinjam tersedia!")
                informasi_buku = CariDaftar(Borrow_Buku)
                Tabel_Daftar_Buku(informasi_buku)

                Menambahkan_keranjang = input("\n\t Tambahkan keranjang (Ya/Tidak)?").lower()
                if Menambahkan_keranjang == "ya":
                    Jumlah_Buku = int(input("\t Berapa buku yang ingin dipinjam?:"))
                    if Jumlah_Buku > informasi_buku[0]["stok_buku"]:
                        print("\n\t Mohon maaf stok buku tidak cukup")
                    else:
                        # Menggunakan "Qty" sebagai kunci untuk jumlah buku
                        buku_di_keranjang = {

                            "Judul_Buku": informasi_buku[0]["Judul_Buku"],
                            "Qty": Jumlah_Buku,
                            "ID_Buku": informasi_buku[0]["ID_Buku"],
                            "Tanggal_Pinjam": datetime.now() 
                        }

                        #keranjang buku sebagai variabel sementara saja
                        Keranjang_Buku.append(buku_di_keranjang)
                        print("\n\t Buku berhasil ditambahkan ke keranjang!")
                else:
                    print("\n\t Keranjang Buku tidak jadi diupdate")

                Tabel_Daftar_Buku_Keranjang(Keranjang_Buku)

                Mengonfirmasi_pinjaman = input("\n\t Konfirmasi pinjaman Buku yang ingin dipinjam (Ya/Tidak)?").lower()
                if Mengonfirmasi_pinjaman == "ya":
                    informasi_buku[0]["stok_buku"] -= Jumlah_Buku
                    print("\n\t Terima kasih telah meminjam buku!")
                elif Mengonfirmasi_pinjaman == "tidak":
                    print("\n\t Terima kasih!")
                else:
                    print("\n\t Tidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
                break 

    elif input_borrow == 2:
        Menu()
    else:
        print("\n\tTidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")

    borrow()

#Fungsi mengembalikan buku

def return_buku():
    input_return = int(input('''Menu Mengembalikan Buku:
1. Mengembalikan Buku
2. Kembali ke menu utama
Masukkan angka menu yang ingin Anda jalankan: '''))

    if input_return == 1:
        Tabel_Daftar_Buku_Keranjang(Keranjang_Buku)  #keranjang buku sebagai variabel sementara. 
        Mengembalikan_Buku = str(input("\tMasukkan ID Buku yang ingin Anda kembalikan: "))
        list_value = [str(value) for data_buku in Keranjang_Buku for value in data_buku.values()]

        if Mengembalikan_Buku not in list_value:
            print("\n\t Maaf, Data yang ingin Anda kembalikan tidak ada. Silahkan kembalikan Buku yang tersedia!")

        else:
            print("\n\t Data yang ingin Anda kembalikan tersedia!")
            informasi_buku = CariDaftar(Mengembalikan_Buku)
            Tabel_Daftar_Buku(informasi_buku)

            Jumlah_Kembali = int(input("\n\t Berapa buku yang ingin Anda kembalikan?: "))

            for buku in Keranjang_Buku:
                if buku["ID_Buku"] == Mengembalikan_Buku:
                    if Jumlah_Kembali > buku["Qty"]:
                        print("\n\t Jumlah buku yang ingin dikembalikan melebihi yang dipinjam.")
                    else:
                        buku["Qty"] -= Jumlah_Kembali
                        informasi_buku[0]["stok_buku"] += Jumlah_Kembali
                        print("\n\t Buku yang Anda pinjam berhasil dikembalikan!")
                        Tabel_Daftar_Buku_Keranjang(Keranjang_Buku)
                        

    elif input_return == 2:
        Menu()
    else:
        print("\n\t Tidak ada data yang tersedia, silahkan masukkan angka yang tersedia\n")
    return_buku()


# Fungsi menu utama

def Menu():
    while True:
        pilihanMenu = input('''
Selamat Datang di Perpustakaan Juwantoro

List Menu :
1. Menampilkan Daftar Buku
2. Menambah Daftar Buku
3. Mengubah Daftar Buku
4. Menghapus Daftar Buku
5. Meminjam Buku
6. Mengembalikan Buku
7. Exit Program

Masukkan angka Menu yang ingin Anda jalankan : ''')

        if(pilihanMenu == "1") :
            read()
        elif(pilihanMenu == "2") :
            add(List_Daftar_Buku)
        elif(pilihanMenu == "3") :
            update()
        elif(pilihanMenu == "4") :
            delete()
        elif(pilihanMenu == "5") :
            borrow()
        elif(pilihanMenu == "6") :
            return_buku()
        else:
            Menu()

# Memanggil Menu utama
Menu()
