/* MODUL Aksi USER */
/* Membuat aksi2 yang bisa digunakan user*/

#ifndef ACTION_H
#define ACTION_H

#include "attribute.h"
#include "boolean.h"
#include <string.h>

/* *** HAL PENTING TTG STRING : *** */
//cara mencompare string di if dengan strcmp(a,b) == 0 -> str a dan b sama
// declaring string 
//char str[50]
// reading string 
//scanf("%s",str);     
// print string 
//printf("%s",str); 
//untungnya tiap di scan, array char kosong dengan otomatis
//if(strcmp(str,"hallo") == 0){
//        printf(" world")};

/* Kamus umum */
#define MaxAksi 20

/* Definisi elemen dan koleksi objek */
typedef struct { 
  char str[30]; /* String */
  char aksivalid[MaxAksi][50] = { //Indeks aksi dimulai dari 1 yaitu tidur siang
    "","Tidur Siang", "Tidur Malam", //tidur siang + 10 energy, tidur malam + 15 energy 
    "Makan Hamburger", "Makan Pizza", "Makan Steak and Beans", //hamburger +5 energy, pizza +10 energy, steak +15 energy
    "Minum Air", "Minum Kopi", "Minum Jus", //air -5 hygiene, kopi +5 energy -10 hygiene, jus +10 energy -5 hygiene
    "Buang Air Kecil", "Buang Air Besar" //BAK +5 hygiene, BAB +10 hygiene -5 energy
    "Bersosialisasi ke Kafe", //+15 fun -10 energy -5 hygiene
    "Bermain Medsos", //+10 fun -10 energy
    "Bermain Media Sosial", //+10 fun -10 energy
    "Bermain Komputer", //+15 fun -10 energy
    "Mandi", //+15 hygiene -5 energy
    "Cuci Tangan", //+5 hygiene
    "Mendengarkan Musik di Radio", //+10 fun -5 energy
    "Membaca Koran", "Membaca Novel" //Koran +5 fun -5 energy, Novel +10 fun -5 energy
    };
} Word;

/* *** KONSTRUKTOR *** */
void BacaAksi(Word *X);
/* Membaca input aksi dari user dan memasukannya ke Str.Word */

/* Operator True/false */
boolean IsAksiValid(Word X);
/* Mereturn true bila Word.str ada dalam list aksivalid */

void EvalAksi(Word X,Attribute *A);
/* Mengeval apakah aksi valid, bila tidak PesanError() dan mengulangi pemasukan aksi
bila iya dan attribute mencukupi , mengubah atribut */

#endif