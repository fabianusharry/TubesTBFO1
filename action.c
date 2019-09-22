/* MODUL Aksi USER */
/* Membuat aksi2 yang bisa digunakan user*/

#include <stdio.h>
#include "action.h"
#include <string.h>
#include "attribute.h"
/* *** KONSTRUKTOR *** */
char AssignAksiValid(){
    char W[MaxAksi][50] = {"","Tidur Siang", "Tidur Malam", //tidur siang + 10 energy, tidur malam + 15 energy 
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
    return W;
}

void BacaAksi(Word *X){
  scanf("%s",(*X).str);
}
/* Membaca input aksi dari user dan memasukannya ke Str.Word */

/* Operator True/false */
int IdxAksiValid(Word X,char c[MaxAksi][50]){
  int i = 1;
  boolean check = false;
  while(!check || i<=20){
    if(strcmp(X.str,c[i]) == 0){
      check = true;
      return i;
    }
    i++;
  }
  return 0;
}
/* Mereturn true bila Word.str ada dalam list aksivalid */

void EvalAksi(Word *X,Attribute *A,char c[MaxAksi][50]){
  int a = IdxAksiValid(*X,c);
    while (a == 0){
        PesanError();
        BacaAksi(X);
    }
    if(a == 1){
        ChangeEnergy(10,A);
    }
    else if(a == 2){
        ChangeEnergy(15,A);
    }
    else if(a == 3){
        ChangeEnergy(5,A);
    }
    else if(a == 4){
        ChangeEnergy(10,A);
    }
    else if(a == 5){
        ChangeEnergy(15,A);
    }
    else if(a == 6){
        ChangeHygiene(-5,A);
    }
    else if(a == 7){
        ChangeEnergy(5,A);
        ChangeHygiene(-10,A);
    }
    else if(a == 8){
        ChangeEnergy(10,A);
        ChangeHygiene(-5,A);
    }
    else if(a == 9){
        ChangeHygiene(5,A);
    }
    else if(a == 10){
        ChangeHygiene(10,A);
        ChangeEnergy(-5,A);
    }
    else if(a == 11){
        ChangeFun(15,A);
        ChangeEnergy(-10,A);
        ChangeHygiene(-5,A);
    }
    else if(a == 12){
        ChangeFun(10,A);
        ChangeEnergy(-10,A);
    }
    else if(a == 13){
        ChangeFun(10,A);
        ChangeEnergy(-10,A);
    }
    else if(a == 14){
        ChangeFun(15,A);
        ChangeEnergy(-10,A);
    }
    else if(a == 15){
        ChangeHygiene(15,A);
        ChangeEnergy(-5,A);
    }
    else if(a == 16){
        ChangeHygiene(5,A);
    }
    else if(a == 17){
        ChangeFun(10,A);
        ChangeEnergy(-5,A);
    }
    else if(a == 18){
        ChangeFun(5,A);
        ChangeEnergy(-5,A);
    }
    else if(a == 19){
        ChangeFun(10,A);
        ChangeEnergy(-5,A);
    }
    
}
/* Mengeval apakah aksi valid, bila tidak PesanError() dan mengulangi pemasukan aksi
bila iya dan attribute mencukupi , mengubah atribut */

