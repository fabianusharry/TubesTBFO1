/* MODUL ATRIBUTE USER */
/* Membuat type atribute dengan 3 part : hygiene,energy, dan fun */

#ifndef ATTRIBUTE_H
#define ATTRIBUTE_H

#include "boolean.h"

/*  Kamus Umum */
#define AttMax 15
/* Atribut maksimum untuk semua part */
#define AttMin 0
/* Atribut minimum */

/* Definisi elemen dan koleksi objek */
typedef int Atr;
typedef struct { 
  Atr Hygiene; //hygiene
  Atr Energy; //energy
  Atr Fun; //fun
} Attribute;

/* *** SELEKTOR *** */
#define H(A)  (A).Hygiene
#define E(A)  (A).Energy
#define F(A)  (A).Fun

/* *** KONSTRUKTOR *** */
boolean IsAtrValid(Atr i);
/* Mengecek apakah i >=0 dan <=15 */

void PesanError();
/* Mengoutput pesan error yaitu: Aksi Tidak Valid */

void TulisAttribute(Attribute A);
/* Menuliskan Attribute karakter dengan format:
Hygiene = <Total_Hygiene>
Energy = <Total_Energy>
Fun = <Total_Fun> */

Attribute NewChar();
/* Mengassign  Kondisi awal pemain dengan atribut Hygiene bernilai 0, Energy
bernilai 10, dan Fun bernilai 0. Permainan dinyatakan selesai jika semua atribut bernilai 0 atau
semua atribut bernilai 15.*/

/* Operator Menambahkan/ mengurangi attribut
   Attribute harus valid, bila tidak gunakan pesanerror*/
void AddHygiene(Atr i,Attribute *A);
/* Menambahkan Hygiene sebesar i*/

void AddEnergy(Atr i,Attribute *A);
/* Menambahkan Energy sebesar i*/

void AddFun(Atr i,Attribute *A);
/* Menambahkan Fun sebesar i*/

void RedHygiene(Atr i,Attribute *A);
/* Mengurangi Fun sebanyak i*/

void RedEnergy(Atr i,Attribute *A);
/* Mengurangi Fun sebanyak i*/

void RedFun(Atr i,Attribute *A);
/* Mengurangi Fun sebanyak i*/

/* Operator End Game */
boolean IsGameOver(Attribute A);
/* Mereturn true bila semua atribut 15 atau 0 */

#endif