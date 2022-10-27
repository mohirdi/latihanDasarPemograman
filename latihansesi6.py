while (True):
    nilai = input ("Masukan nilai : ")
    nama = input ("Masukan nama : ")
    if (nilai.isnumeric () == True) :
        nilaiint =int(nilai)
        if nilaiint >= 101:
            predikat = "Nilai tidak dapat diinput"
            Grade = "Mohon masukan ulang nilai"

        elif nilaiint >= 90 :
            Grade = "A"
            predikat = "Dengan pujian"

        elif nilaiint >= 80:
            Grade = "B"
            predikat = "Sangat memuaskan"

        elif  nilaiint >= 70 :
            Grade = "C"
            predikat = "Memuaskan"

        elif  nilaiint >= 60 :
            Grade = "D"
            predikat = "Tidak memuaskan"

        elif  nilaiint >= 0 :
            predikat = "Tidak LULUS"
            Grade = "E"
        
        print ("\n")
        print ("Nama :", nama)
        print ("Nilai kamu: ", nilaiint) 
        print ("Dengan grade : ", Grade)
        print (predikat)
        print ("\n")
        
    else :
        print ("\n")
        print ("Inputan anda salah")
        print ("Mohon masukan ulang") 
        print ("\n")

    apakahlanjut = input ("Apakakah ingin input nilai lain ? y/n ")
    if (apakahlanjut !="y"):
        print ("\n")

        break