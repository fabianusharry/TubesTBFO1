
######################################## KAMUS #######################################

############ VALIDATOR #################
def isInputValid(a,b,c) :
    return ((0 <= a <= 15) and (0<=b<=15) and (0<=c<=15))

#Fungsi untuk mengecek apakah nilai atribut masih dalam range atau tidak

def check():        ### FINAL STATE ###
    global Hygiene
    global Energy
    global Fun
    global menang
    global kalah
    if(Hygiene == 15 and Energy == 15 and Fun == 15):
        menang = True

    if(Hygiene == 0 and Energy == 0 and Fun == 0):
        kalah = True

#Fungsi untuk mengecek apakah pemain sudah dalam kondisi menang atau kalah

############ VALUATOR/MODIFIER ###############

def ChangeHygiene(x):
    global Hygiene
    Hygiene += x

#Fungsi untuk mengubah nilai dari atribut Hygiene sebesar x

def ChangeEnergy(x):
    global Energy
    Energy += x

#Fungsi untuk mengubah nilai dari atribut Energy sebesar x

def ChangeFun(x):
    global Fun
    Fun += x

#Fungsi untuk mengubah nilai dari atribut Fun sebesar x

############## FUNGSI TULIS #################

def printattribute():
    print()
    print("Hygiene : " + str(Hygiene))
    print("Energy : " + str(Energy))
    print("Fun : " + str(Fun))

#Prosedur untuk mencetak atribut saat ini di layat

def pesanerror():
    print()
    print("Aksi tidak valid!")
    printattribute()

#Prosedur untuk mencetak apabila atribut melebihi batas nilai minimum atau maksimum

def deskripsiaksi():
    print()
    print("[< AKSI YANG BISA DILAKUKAN >]")
    print("1. Tidur")
    print("2. Makan")
    print("3. Minum")
    print("4. Buang Air")
    print("5. Bersosialisasi ke Kafe")
    print("6. Bermain Media Sosial")
    print("7. Bermain Komputer")
    print("8. Mandi")
    print("9. Cuci Tangan")
    print("10. Mendengarkan Musik di Radio")
    print("11. Membaca")
    print("Kamu mau ngapain?")

#Prosedur mencetak list aksi yang bisa dilakukan

def deskripsitidur():
    global perintah
    print()
    print("Mau Tidur apa nih?")
    print("1. Tidur Siang")
    print("2. Tidur Malam")
    perintah = input("> ")

#Prosedur untuk mencetak opsi tidur yang bisa dilakukan dan menerima input dari pemain

def deskripsimakan():
    global perintah
    print()
    print("Mau Makan Apa Nih?")
    print("[< MENU MAKANAN >]")
    print("1. Hamburger")
    print("2. Pizza")
    print("3. Steak and Beans")
    perintah = input("> ")

#Prosedur untuk mencetak opsi makanan apa yang bisa dimakan dan menerima input dari pemain

def deskripsiminum():
    global perintah
    print()
    print("Mau Minum Apa Nih?")
    print("[< MENU MINUMAN >]")
    print("1. Air")
    print("2. Kopi")
    print("3. Jus")
    perintah = input("> ")

#

def deskripsibuangair():
    global perintah
    print()
    print("Mau Kencing apa Berak??")
    print("1. Kencing")
    print("2. Berak")
    perintah = input("> ")

def deskripsimembaca():
    global perintah
    print()
    print("Mau Baca Apa Nih?")
    print("[< LIST BACAAN >]")
    print("1. Koran")
    print("2. Novel")
    perintah = input("> ")

############ START STATE #################
def startgame() : 
    global Hygiene
    global Energy
    global Fun
    global menang
    global kalah
    global perintah

    print("[[<<   THE SIMS JADIJADIAN   >>]]")
    nama = input("Masukkan Nama SIMS : ")
    print("Halo " + nama + "! Selamat Datang di Permainan SIMS, dan Selamat Pagi :) Berikut Kondisi Atributmu : ")
    Hygiene = 0
    Energy = 10
    Fun = 0
    menang = False
    kalah = False
    printattribute()
    print()
    print("Silahkan lakukan apapun yang kamu mau! Tapi ingat, tujuan kamu menang! Yaitu kalo kamu berhasil membuat semua atribut menjadi 15")
    print("Ingat!! Semua hal pasti ada konsekuensinya! Kamu juga bisa kalah kalo atribut kamu 0 semua!")
    print("Selamat Bermain!!")

    deskripsiaksi()
    perintah = input("> ")

# Fungsi digunakan saat game akan dimulai untuk mempersiapkan semua variabel sesuai dengan state awal game

################################### ALGORITMA MAIN PROGRAM #################################

startgame()
while True:

    if((perintah == "Tidur")):
        deskripsitidur()

        if(perintah == "Tidur Siang"):
            if(isInputValid(Hygiene, Energy + 10, Fun)):
                ChangeEnergy(10)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

        elif(perintah == "Tidur Malam"):
            if(isInputValid(Hygiene, Energy + 15, Fun)):
                ChangeEnergy(15)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

    elif(perintah == "Makan"):
        deskripsimakan()
        if(perintah == "Hamburger"):
            if(isInputValid(Hygiene, Energy + 5, Fun)):
                ChangeEnergy(5)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

        elif(perintah == "Pizza"):
            if(isInputValid(Hygiene, Energy + 10, Fun)):
                ChangeEnergy(10)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()
        
        elif(perintah == "Steak and Beans"):
            if(isInputValid(Hygiene, Energy + 15, Fun)):
                ChangeEnergy(15)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

    elif(perintah == "Minum"):
        deskripsiminum()

        if(perintah == "Air"):
            if(isInputValid(Hygiene - 5, Energy, Fun)):
                ChangeHygiene(-5)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

        elif(perintah == "Kopi"):
            if(isInputValid(Hygiene - 10, Energy + 5, Fun)):
                ChangeEnergy(5)
                ChangeHygiene(-10)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()
        
        elif(perintah == "Jus"):
            if(isInputValid(Hygiene - 5, Energy + 10, Fun)):
                ChangeEnergy(10)
                ChangeHygiene(-5)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()
        
    elif(perintah == "Buang Air"):
        deskripsibuangair()

        if(perintah == "Kencing"):
            if(isInputValid(Hygiene + 5, Energy, Fun)):
                ChangeHygiene(5)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

        elif(perintah == "Berak"):
            if(isInputValid(Hygiene + 10, Energy - 5, Fun)):
                ChangeEnergy(-5)
                ChangeHygiene(10)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()
    
    elif(perintah == "Bersosialisasi Ke Kafe"):
        if(isInputValid(Hygiene - 5, Energy - 10, Fun + 15)):
            ChangeEnergy(-10)
            ChangeHygiene(-5)
            ChangeFun(15)
            printattribute()
            check()
            if(menang or kalah) : break
        else:
            pesanerror()
    
    elif(perintah == "Bermain Media Sosial"):
        if(isInputValid(Hygiene, Energy - 10, Fun + 10)):
            ChangeEnergy(-10)
            ChangeFun(10)
            printattribute()
            check()
            if(menang or kalah) : break
        else:
            pesanerror()
    
    elif(perintah == "Bermain Komputer"):
        if(isInputValid(Hygiene, Energy - 10, Fun + 15)):
            ChangeEnergy(-10)
            ChangeFun(15)
            printattribute()
            check()
            if(menang or kalah) : break
        else:
            pesanerror()

    elif(perintah == "Mandi"):
        if(isInputValid(Hygiene + 15, Energy - 5, Fun)):
            ChangeEnergy(-5)
            ChangeHygiene(15)
            printattribute()
            check()
            if(menang or kalah) : break
        else:
            pesanerror()
    
    elif(perintah == "Cuci Tangan"):
        if(isInputValid(Hygiene + 5, Energy, Fun)):
            ChangeHygiene(5)
            printattribute()
            check()
            if(menang or kalah) : break
        else:
            pesanerror()
    
    elif(perintah == "Mendengarkan Musik di Radio"):
        if(isInputValid(Hygiene, Energy - 10, Fun + 10)):
            ChangeEnergy(-10)
            ChangeFun(10)
            printattribute()
            check()
            if(menang or kalah) : break
        else:
            pesanerror()
    
    elif((perintah == "Membaca")):
        deskripsimembaca()

        if(perintah == "Koran"):
            if(isInputValid(Hygiene, Energy -5, Fun + 5)):
                ChangeEnergy(-5)
                ChangeFun(5)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()

        elif(perintah == "Novel"):
            if(isInputValid(Hygiene, Energy - 5, Fun + 10)):
                ChangeEnergy(-5)
                ChangeFun(10)
                printattribute()
                check()
                if(menang or kalah) : break
            else:
                pesanerror()
    
    else: print("Aksi tidak terdaftar, hayo dibaca lagi!")

    deskripsiaksi()
    perintah = input("Masukkan aksi : ")

if(menang):
    print("ALHAMDULILLAH IDUP MAKMUR EUY MENANGGGG IDUP AMAN TENTRAM ADIL MAKMUR")

elif(kalah):
    print("PEMAIN KAMU MATI WOI!! Belom beruntung :((((")

print("Terima kasih sudah bermain The Sims Jadijadian ini hehe!! :)")

#################### E N D   O F   P R O G R A M ######################