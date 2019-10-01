
######################################## KAMUS #######################################
import csv
csvData = [["Nama Aksi", "Hygiene","Energy","Fun"]]
#untuk memasukan dan mengedit file

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

def AddAksi(Action):
    global Hygiene
    global Energy
    global Fun
    global csvData
    row = [Action, str(Hygiene), str(Energy), str(Fun)]
    csvData.append(row)

#Fungsi untuk memasukan perintah kedalam list

def InputFile():
    global nama
    global fileName
    global cekFile
    isFile = input("Apakah kamu mau memasukan data game ini kedalam file? (Yes/No) : ")
    while(isFile.lower() != "no" and isFile.lower() != "yes"):
        isFile = input("Mohon ulangi pilihan anda (Yes/No) : ")
    
    nama = input("Masukkan Nama SIMS : ")
    if (isFile.lower() == "yes") :
        fileName = nama + ".csv"
        #fileName = input("Masukan nama file (gunakan .csv di akhir) : ")
        print("Silakan memainkan game, file akan disave di " + fileName)
        cekFile = True
    
    elif(isFile.lower() == "no") :
        cekFile = False
    
def TulisKeFile(): # $ Fungsi untuk menuliskan aksi dan perubahan attribute kedalam file
    global fileName
    global csvData
    with open(fileName, 'w') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(csvData)
    writeFile.close()

#Fungsi untuk memasukan sesuatu kedalam file

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

#Prosedur untuk mencetak atribut saat ini di layar

def pesanerror():
    global checkperintah
    print()
    print("Aksi tidak valid!")
    checkperintah = False
    printattribute()


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

#Prosedur untuk mengganti attribute secara compact

def deskripsiaksi():
    global perintah2
    perintah2 = ""
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
    global perintah2
    print()
    print("Mau tidur apa nih?")
    print("1. Siang")
    print("2. Malam")
    perintah2 = input("> ")

#Prosedur untuk mencetak opsi tidur yang bisa dilakukan dan menerima input dari pemain

def deskripsimakan():
    global perintah2
    print()
    print("Mau makan apa nih?")
    print("[< MENU MAKANAN >]")
    print("1. Hamburger")
    print("2. Pizza")
    print("3. Steak and Beans")
    perintah2 = input("> ")

#Prosedur untuk mencetak opsi makanan apa yang bisa dimakan dan menerima input dari pemain

def deskripsiminum():
    global perintah2
    print()
    print("Mau minum apa nih?")
    print("[< MENU MINUMAN >]")
    print("1. Air")
    print("2. Kopi")
    print("3. Jus")
    perintah2 = input("> ")

#Prosedur untuk mencetak opsi buang air pemain

def deskripsibuangair():
    global perintah2
    print()
    print("Mau Buang air kecil atau buang air besar??")
    print("1. Kecil")
    print("2. Besar")
    perintah2 = input("> ")

def deskripsimembaca():
    global perintah2
    print()
    print("Mau baca apa nih?")
    print("[< LIST BACAAN >]")
    print("1. Koran")
    print("2. Novel")
    perintah2 = input("> ")

############ START STATE #################
def StartGame() : 
    global Hygiene
    global Energy
    global Fun
    global menang
    global kalah
    global perintah
    global nama
    
    
    print("[[<<!!!!!!!!!!!!!!!!!!!!!!!!!!!   THE SIMS JADIJADIAN   !!!!!!!!!!!!!!!!!!!!!!!!!!!>>]]")
    print()
    print("        `-:/+++++++++/:-.`                                                                      ")
    print("     `:++++++++++++++++++++:                -:::::::                                            ")
    print("    -+oooooooooo++ooooooo+:` `........      +ooooooo-     .......`        `.-:///++///:-.`      ")
    print("   -oooooooo+-.`   `.-/o/`   /oooooooo`    .oooooooo+    .ooooooo+     `:+oooooooooooooooo+:    ")
    print("   +oooooooo:                /oooooooo`    +ooooooooo-   +oooooooo.   :ooooooooooooooooooo:`    ")
    print("   +sssssssso/-`             /ssssssss.   .ssssssssss+  -sssssssss+  /sssssssso/:::://oo/`      ")
    print("   .osssssssssssoo+/-.`      /ssssssss.   :sssssssssss. ossssssssss. ossssssso`        `        ")
    print("    `+ssssssssssssssssss+:`  +ssssssss.   osssssssssss+:sssssssssss+ osssssssss+/:.`            ")
    print("      `-/oyyyyyyyyyyyyyyyyy/ :yyyyyyyy.  -yyyyyyyyyyyyyyyyyyyyyyyyyy.`oyyyyyyyyyyyyyyo+-`       ")
    print("          ///:/osyyyyyyyyyyyo +yyyyyyy.  +yyyyyyyyyyyyyyyyyyyyyyyyyy:  -+yyyyyyyyyyyyyyyy+`     ")
    print("                 `.+yyyyyyyyy-.yyyyyyy. `yyyyyyyyyyyyyyyyyyyyyyyyyyyy     .-/+osyyyyyyyyyys`    ")
    print("                    yhhhhhhhh-.hhhhhhh. /hhhhhhhsyhhhhhhhhhhyshhhhhhh:          `-ohhhhhhhh-    ")
    print("     `+hy+:.`    .:shhhhhhhhy`/hhhhhhh. yhhhhhhh//hhhhhhhhhh/+hhhhhhhs           .+hhhhhhhh-    ")
    print("   `/hhhhhhhhhhhhhhhhhhhhhhy.-hhhhhhhh.:hhhhhhhh..hhhhhhhhhh..hhhhhhhhohhhhhhhhhhhhhhhhhhho     ")
    print("  `ohhhhhhhhhhhhhhhhhhhhhh+` ohhhhhhhh.shhhhhhhy  shhhhhhhho  yhhhhhhhhhhhhhhhhhhhhhhhhhy/      ")
    print("     -/oyhhhhhhhhhhhhys+-    ohhhhhhhh:hhhhhhhh/  -hhhhhhhh.  ohhhhhhhhooyhhhhhhhhhhys+-      ")
    print()
    print("Halo! Selamat Datang di Permainan SIMS, dan Selamat Pagi :)")
    Hygiene = 0
    Energy = 10
    Fun = 0
    menang = False
    kalah = False
    
    print("-------------------------------------------------------------------")
    print("Silahkan lakukan apapun yang kamu mau! Tapi ingat, tujuan kamu menang! Yaitu kalo kamu berhasil membuat semua atribut menjadi 15")
    print("Ingat!! Semua hal pasti ada konsekuensinya! Kamu juga bisa kalah kalo atribut kamu 0 semua!")
    print("Selamat Bermain!!")
    print("-------------------------------------------------------------------")
    InputFile()
    print("-------------------------------------------------------------------")
    print("Selamat datang "+nama+ " ke dalam permainan, berikut adalah statusmu : ")
    printattribute()
    deskripsiaksi()
    perintah = input("> ")

############ END STATE #################
def EndGame():
    global cekFile
    global nama
    global terakhir

    if(menang):
        print("            ``             ")
        print("           os+            ")
        print("        ./oo/`            ")
        print("     `:+oooo:             ")
        print("   `:ooooooo:             ALHAMDULILLAH IDUP MAKMUR EUY MENANGGGG IDUP AMAN TENTRAM ADIL MAKMUR")
        print(" .:ooooooooo:             ")
        print(" `..---:///+:             ")
        print("            :             SELAMAT KEPADA PEMAIN " + nama + " KARENA TELAH MEMAINKAN GAME INI")
        print("            :             ")
        print("            :             JANGAN LUPA FOLLOW IG KAMI @fabianusharry")
        print("            :                                        @mariogunawan1")
        print("            :                .::           ")
        print("            :                +-:/          ")
        print("            :                :+-/+.        ")
        print("            :                -o+--//- ``   ")
        print("            :             -/-//+/---:shd:  ")
        print("            :             .o///oo----+hy+  ")
        print("            :              o////s+-//+hh.  ")
        print("         ```/ `             /o//o/-:+ysd`  ")
        print("         :hhdhh.             `..`.-.`:/-   ")
        print("          yhhho                             ")
        print()

    elif(kalah):
        print("PEMAIN KAMU MATI WOI!! Belom beruntung :((((")
    
    if(cekFile):
        print("Jangan lupa, file akan disave ke : " + fileName)
        TulisKeFile()

    print("Terima kasih sudah bermain The Sims Jadijadian ini hehe!! :)")
    terakhir = input("(Tekan enter)")
    

def Cheat():
    global menang
    menang = True

# Fungsi digunakan saat game akan dimulai untuk mempersiapkan semua variabel sesuai dengan state awal game

################################### ALGORITMA MAIN PROGRAM #################################
StartGame()
while True:
    checkperintah = True
    if((perintah == "Tidur")):
        deskripsitidur()

        if(perintah2 == "Siang"):
            ChangeAttribute(0,10,0)

        elif(perintah2 == "Malam"):
            ChangeAttribute(0,15,0)
        else : pesanerror()

    elif(perintah == "Makan"):
        deskripsimakan()

        if(perintah2 == "Hamburger"):
            ChangeAttribute(0,5,0)

        elif(perintah2 == "Pizza"):
            ChangeAttribute(0,10,0)
        
        elif(perintah2 == "Steak and Beans"):
            ChangeAttribute(0,15,0)
        else : pesanerror()

    elif(perintah == "Minum"):
        deskripsiminum()

        if(perintah2 == "Air"):
            ChangeAttribute(-5,0,0)

        elif(perintah2 == "Kopi"):
            ChangeAttribute(-10,5,0)
        
        elif(perintah2 == "Jus"):
            ChangeAttribute(-5,10,0)
        else : pesanerror()
        
    elif(perintah == "Buang Air"):
        deskripsibuangair()

        if(perintah2 == "Kecil"):
            ChangeAttribute(5,0,0)

        elif(perintah2 == "Besar"):
            ChangeAttribute(10,-5,0)
        else : pesanerror()
    
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

        if(perintah2 == "Koran"):
            ChangeAttribute(0,-5,5)

        elif(perintah2 == "Novel"):
            ChangeAttribute(0,-5,10)

        else : pesanerror()

    elif(perintah == "Cek Attribute"):
        printattribute()
    
    elif(perintah == "HarryMario"):
        Cheat()
    
    else: 
        print("Aksi tidak terdaftar, hayo dibaca lagi!")
        checkperintah = False

    check()
    if(checkperintah):
        AddAksi(perintah+" "+perintah2)
    if(menang or kalah) : break
    deskripsiaksi()
    perintah = input("Masukkan aksi : ")

EndGame()
#################### E N D   O F   P R O G R A M ######################