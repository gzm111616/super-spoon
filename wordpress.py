#!/usr/bin/env python

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet WORDPRESS TARAMA")
print("""            

Wordpress Tarama Araci...

1) Hizli Tarama
2) Eklenti Tarama
3) Tema Tarama
4) Yönetici Kullanici Adi Tarama

""")

islemno = input("Islem Numarisini Girin: ")

if(islemno=="1"):
      site = input("Site Adresi Girin: ")
      os.system("wpscan --url " + site)
elif(islemno=="2"):
      site = input("Site Adresi Girin: ")  
      os.system("wpscan --url " + site + " --enumerate p" )
elif(islemno=="3"):
      site = input("Site Adresi Girin: ")
      os.system("wpscan --url " + site + " --enumerate t" )      
elif(islemno=="4"):
      site = input("Site Adresi Girin: ")
      os.system("wpscan --url " + site + "--enumerate  u" )
else:
      print("Hatali secim yaptiniz...Program Kapatiliyor:(")
