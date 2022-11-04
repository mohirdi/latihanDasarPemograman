while True :
    print ("\n")
    print ("Menu")
    print ("1. Hitung luas segitiga")
    print ("2. Hitung luas persegi")
    print ("3. menentukan ganjil genap")
    print ("4. quit")
    list_menu = input ("Masukan pilihan : ")

    if list_menu == "1":
        print  ("Menghitung luas segitiga" "\n")
        alas = float (input ("Masukan alas segitiga : "))
        tinggi = float (input ("Masukan tinggi segitiga : "))
        luassegitiga =  alas * tinggi / 2
        print ("Luas segitiga : ", luassegitiga , "\n")
    elif list_menu == "2":
        print  ("Menghitung luas persegi" "\n")
        panjang = float (input ("Masukan panjang persegi : "))
        lebar = float (input ("Masukan lebar persegi : "))
        luaspersegi =  panjang * lebar
        print ("Luas persegi : ", luaspersegi, "\n")
    elif list_menu == "3" :
        print ("Menentukan ganjil genap")
        angka = int (input ("Masukan angka : "))
        if (angka %2 == 0):
            print ("Angka : ", angka , "Merupakan angka genap")
        else :
            print ("Angka : ", angka , "Merupakan angka ganjil")
        print ("\n")
    else :
        a = input ("Ingin keluar ? ")
        if a == "quit":
            break



    