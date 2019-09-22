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
#define String(W)  (W).str
/* Definisi elemen dan koleksi objek */
typedef struct { 
  char str[30]; /* String */
} Word;

/* *** KONSTRUKTOR *** */
char AssignAksiValid();
/* Mengassign array of string aksi valid */

void BacaAksi(Word *X);
/* Membaca input aksi dari user dan memasukannya ke Str.Word */

/* Operator True/false */
int IdxAksiValid(Word X,char c[MaxAksi][50]);
/* Mereturn true bila Word.str ada dalam list aksivalid */

void EvalAksi(Word *X,Attribute *A, char c[MaxAksi][50]);
/* Mengeval apakah aksi valid, bila tidak PesanError() dan mengulangi pemasukan aksi
bila iya dan attribute mencukupi , mengubah atribut */

#endif