while (True) :
    namabarang = input ("Masukan nama barang : ")
    hargabarang = int (input ("Masukan harga barang :") )
    persen = input ("Masukan persen: ")
    keuntungan = int (hargabarang) * int (persen)/100
    hargajual = int (hargabarang + keuntungan)
    print ("Nama barang =",namabarang)
    print ("Harga barang =", hargabarang)
    print ("Keuntungan = ", keuntungan)
    print ( namabarang, "Dijual dengan harga Rp.", hargajual )
    apakahlanjut = input ("Apakah ingin input barang lain ? Y lanjut N Tidak ? ")
    if (apakahlanjut !="Y"):
        break
print ("\n")