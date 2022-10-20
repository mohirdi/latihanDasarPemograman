modal = 0
laba = 0

while (True):
    namabarang = input("Masukan nama barang : ")
    hargabarang = int (input ("Masukan harga barang :"))
    persen = int (input ("Masukan persen : "))
    totalbarang = int (input ("Masukan jumlah barang : "))

    print ("==============================")

    keuntungan =  hargabarang * persen / 100
    jual = keuntungan + hargabarang
    totalkeuntungan = keuntungan * totalbarang
    totalhargabeli = hargabarang * totalbarang

    modal = totalhargabeli + modal
    laba = totalkeuntungan + laba

    print ("Nama barang : ", namabarang)
    print ("Harga barang : Rp.", hargabarang)
    print ("keuntungan : Rp.", keuntungan)
    print ("Dijual dengan harga : Rp.", jual)
    print ("Total keuntungan : Rp. ", totalkeuntungan) 
    print ("Modal awal Rp. ", totalhargabeli)   
    
    apakahlanjut = input ("Apakah ingin input barang lain ? Y lanjut N")
    if (apakahlanjut !="Y"):
        break    
print ("==============================")
print ("Modal keseluruhan: Rp. ", modal)
print ("Laba keseluruhan : Rp.", laba)
