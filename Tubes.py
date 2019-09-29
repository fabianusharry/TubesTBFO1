
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
    global nama
    print()
    print("Status " + nama + " :")
    print("Hygiene : " + str(Hygiene))
    print("Energy : " + str(Energy))
    print("Fun : " + str(Fun))

#Prosedur untuk mencetak atribut saat ini di layat

def pesanerror():
    print()
    print("Aksi tidak valid!")
    printattribute()

#Prosedur untuk mengganti attribute secara compact
def ChangeAttribute(H,E,F):
    global Hygiene
    global Energy
    global Fun
    if(isInputValid(Hygiene+H,Energy+E,Fun+F)):
        ChangeEnergy(E)
        ChangeHygiene(H)
        ChangeFun(F)
        printattribute()
    else:
        pesanerror()

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
    print("12. Cek Attribute")
    print("Kamu mau ngapain?")

#Prosedur mencetak list aksi yang bisa dilakukan

def deskripsitidur():
    global perintah
    print()
    print("Mau tidur apa nih?")
    print("1. Tidur Siang")
    print("2. Tidur Malam")
    perintah = input("> ")

#Prosedur untuk mencetak opsi tidur yang bisa dilakukan dan menerima input dari pemain

def deskripsimakan():
    global perintah
    print()
    print("Mau makan apa nih?")
    print("[< MENU MAKANAN >]")
    print("1. Hamburger")
    print("2. Pizza")
    print("3. Steak and Beans")
    perintah = input("> ")

#Prosedur untuk mencetak opsi makanan apa yang bisa dimakan dan menerima input dari pemain

def deskripsiminum():
    global perintah
    print()
    print("Mau minum apa nih?")
    print("[< MENU MINUMAN >]")
    print("1. Air")
    print("2. Kopi")
    print("3. Jus")
    perintah = input("> ")

#Prosedur untuk mencetak opsi buang air pemain

def deskripsibuangair():
    global perintah
    print()
    print("Mau Buang air kecil atau buang air besar??")
    print("1. Kencing")
    print("2. Berak")
    perintah = input("> ")

def deskripsimembaca():
    global perintah
    print()
    print("Mau baca apa nih?")
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
    global nama

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

############ END STATE #################
def EndGame():
    global nama
    if(menang):
        print("ALHAMDULILLAH IDUP MAKMUR EUY MENANGGGG IDUP AMAN TENTRAM ADIL MAKMUR")
        print("SELAMAT KEPADA PEMAIN " + nama + " KARENA TELAH MEMAINKAN GAME INI")

    elif(kalah):
        print("PEMAIN KAMU MATI WOI!! Belom beruntung :((((")
    
    print("Terima kasih sudah bermain The Sims Jadijadian ini hehe!! :)")

def Cheat():
    global menang
    menang = True
# Fungsi digunakan saat game akan dimulai untuk mempersiapkan semua variabel sesuai dengan state awal game

################################### ALGORITMA MAIN PROGRAM #################################

startgame()
while True:

    if((perintah == "Tidur")):
        deskripsitidur()

        if(perintah == "Siang"):
            ChangeAttribute(0,10,0)

        elif(perintah == "Malam"):
            ChangeAttribute(0,15,0)

    elif(perintah == "Makan"):
        deskripsimakan()
        if(perintah == "Hamburger"):
            ChangeAttribute(0,5,0)

        elif(perintah == "Pizza"):
            ChangeAttribute(0,10,0)
        
        elif(perintah == "Steak and Beans"):
            ChangeAttribute(0,15,0)

    elif(perintah == "Minum"):
        deskripsiminum()

        if(perintah == "Air"):
            ChangeAttribute(-5,0,0)

        elif(perintah == "Kopi"):
            ChangeAttribute(-10,5,0)
        
        elif(perintah == "Jus"):
            ChangeAttribute(-5,10,0)
        
    elif(perintah == "Buang Air"):
        deskripsibuangair()

        if(perintah == "Kencing"):
            ChangeAttribute(5,0,0)

        elif(perintah == "Berak"):
            ChangeAttribute(10,-5,0)
    
    elif(perintah == "Bersosialisasi ke Kafe"):
        ChangeAttribute(-5,-10,15)
    
    elif(perintah == "Bermain Media Sosial"):
        ChangeAttribute(0,-10,10)
    
    elif(perintah == "Bermain Komputer"):
        ChangeAttribute(0,-10,15)

    elif(perintah == "Mandi"):
        ChangeAttribute(15,-5,0)
    
    elif(perintah == "Cuci Tangan"):
        ChangeAttribute(5,0,0)
    
    elif(perintah == "Mendengarkan Musik di Radio"):
        ChangeAttribute(0,-10,10)
    
    elif((perintah == "Membaca")):
        deskripsimembaca()

        if(perintah == "Koran"):
            ChangeAttribute(0,-5,5)

        elif(perintah == "Novel"):
            ChangeAttribute(0,-5,10)

    elif(perintah == "Cek Attribute"):
        printattribute()
    
    elif(perintah == "HarryMario"):
        Cheat()
    
    else: print("Aksi tidak terdaftar, hayo dibaca lagi!")
    check()
    if(menang or kalah) : break
    deskripsiaksi()
    perintah = input("Masukkan aksi : ")

EndGame()

#################### E N D   O F   P R O G R A M ######################