from asyncio import constants
from datetime import date, datetime
from functools import total_ordering
import imp
from locale import format_string
from tkinter import W, Variable


NAMA = ' FADLAN IMAN '
NIM = ' 220180084 '

print(" NAMA :", NAMA )
print(" NIM :", NIM )

print("="*40)
print("         PEMATANGSIANTAR CAFE        ")
print("="*40)

nama = input(" KETIK NAMA ANDA ")
print(" NAMA ANDA :",nama)

print("HALO SELAMAT DATANG DI PEMATANGSIANTAR CAFE:)",nama)

print("-"*20) 
print("     DAFTAR MENU     ")
print("-"*20) 

print("""          
            (MAKANAN)                               (MINUMAN)                
 1. Nasi Goreng     = Rp 10000    ><     1. Teh Dingin       = Rp 5000     
 2. Ayam Bakar      = Rp 15000    ><     2. Greentea         = Rp 7000     
 3. Ayam Geprek     = Rp 12000    ><     3. Coklat Panas     = Rp 10000    
 4. Mie Ayam        = Rp 8000     ><     4. Milo Dingin      = Rp 10000
 5. Mie Aceh        = Rp 9000     ><     5. Lemon Tea        = Rp 8000
 6. Mie Udang       = Rp 13000    ><     6. Macha Tea        = Rp 12000
 7. Mieso           = Rp 6000     ><     7. Red Velvet       = Rp 12000
 8. Ikan Bakar      = Rp 10000    ><     8. Brown Sugar      = Rp 15000
 9. FRENCH FRIES    = Rp 5000     ><     9. Espresso         = Rp 20000
10. SAUSAGE         = Rp 5000     ><     10. Americano       = Rp 18000                                 """) 


MAKANAN = int(input(" SILAHKAN KETIK PESANAN ANDA(MAKANAN)/MOHON KETIK ANGKA! "))
JUMLAH_MAKANAN = int(input(" JUMLAH MAKANAN "))

if MAKANAN == 1:
    totalmakan = JUMLAH_MAKANAN * 10000
    print( JUMLAH_MAKANAN,"  NASI GORENG = RP ", totalmakan )

elif  MAKANAN == 2:
    totalmakan = JUMLAH_MAKANAN * 15000
    print( JUMLAH_MAKANAN,"  AYAM BAKAR = RP ", totalmakan )

elif MAKANAN ==  3:
    totalmakan = JUMLAH_MAKANAN * 12000
    print( JUMLAH_MAKANAN,"  AYAM GEPREK = RP ", totalmakan )

elif MAKANAN == 4:
    totalmakan = JUMLAH_MAKANAN * 8000
    print( JUMLAH_MAKANAN,"  MIE AYAM = RP ", totalmakan )

elif MAKANAN == 5:
    totalmakan = JUMLAH_MAKANAN * 9000
    print( JUMLAH_MAKANAN,"  MIE ACEH = RP ", totalmakan )

elif MAKANAN == 6:
    totalmakan = JUMLAH_MAKANAN * 13000
    print( JUMLAH_MAKANAN,"  MIE UDANG = RP ", totalmakan )

elif MAKANAN == 7:
    totalmakan = JUMLAH_MAKANAN * 6000
    print( JUMLAH_MAKANAN,"  MIESO = RP ", totalmakan )

elif MAKANAN == 8:
    totalmakan = JUMLAH_MAKANAN * 10000
    print( JUMLAH_MAKANAN,"  IKAN BAKAR = RP ", totalmakan )

elif MAKANAN == 9:
    totalmakan = JUMLAH_MAKANAN * 5000
    print( JUMLAH_MAKANAN,"  FRENCH FRIES = RP ", totalmakan )

elif MAKANAN == 10:
    totalmakan = JUMLAH_MAKANAN * 5000
    print( JUMLAH_MAKANAN,"  SAUSAGE = RP ", totalmakan )


else:
    print(" MAAF, PESANAN ANDA TIDAK TERSEDIA ")

MINUMAN = int(input(" SILAHKAN KETIK PESANAN ANDA(MINUMAN)/MOHON KETIK ANGKA! "))
JUMLAH_MINUMAN = int(input(" JUMLAH MINUMAN "))

if MINUMAN == 1:
    totalminum = JUMLAH_MINUMAN * 5000
    print( JUMLAH_MINUMAN,"  TEH DINGIN = RP ", totalminum )
    
elif MINUMAN == 2:
    totalminum = JUMLAH_MINUMAN * 7000
    print( JUMLAH_MINUMAN,"  GREENTEA = RP ", totalminum )
    

elif MINUMAN == 3:
    totalminum = JUMLAH_MINUMAN * 10000
    print( JUMLAH_MINUMAN,"  COKLAT PANAS = RP ", totalminum )
    
    
elif MINUMAN == 4:
    totalminum = JUMLAH_MINUMAN * 10000
    print( JUMLAH_MINUMAN,"  MILO DINGIN = RP ", totalminum )

elif MINUMAN == 5:
    totalminum = JUMLAH_MINUMAN * 8000
    print( JUMLAH_MINUMAN,"  LEMON TEA = RP ", totalminum )

elif MINUMAN == 6:
    totalminum = JUMLAH_MINUMAN * 12000
    print( JUMLAH_MINUMAN,"  MATCHA TEA = RP ", totalminum )

elif MINUMAN == 7:
    totalminum = JUMLAH_MINUMAN * 12000
    print( JUMLAH_MINUMAN,"  RED VELVET = RP ", totalminum )

elif MINUMAN == 8:
    totalminum = JUMLAH_MINUMAN * 15000
    print( JUMLAH_MINUMAN,"  BROWN SUGAR = RP ", totalminum )

elif MINUMAN == 9:
    totalminum = JUMLAH_MINUMAN * 20000
    print( JUMLAH_MINUMAN,"  ESPRESSO = RP ", totalminum )

elif MINUMAN == 10:
    totalminum = JUMLAH_MINUMAN * 18000
    print( JUMLAH_MINUMAN,"  AMERICANO = RP ", totalminum )
    
else:
    print(" MAAF, PESANAN ANDA TIDAK TERSEDIA ")

print("="*40)
print(" STRUK PEMBAYARAN ")
print(date.today())
print("="*40)

TOTAL_PESANAN = totalmakan + totalminum
print(" PESANAN YANG HARUS DIBAYAR Rp =", TOTAL_PESANAN )
UANG_PEMBELI = int(input(" KETIK NOMINAL UANG ANDA "))

if UANG_PEMBELI < TOTAL_PESANAN:
    print(" MAAF UANG ANDA KURANG ")
    print(" SILAHKAN TAMBAH NOMINAL ANDA TERLEBIH DAHULU ")

elif UANG_PEMBELI > TOTAL_PESANAN:
    print(" KEMBALIAN ",UANG_PEMBELI - TOTAL_PESANAN )
    print(""" THANKS FOR YOUR ORDER:)
            I HOPE YOU'LL BACK""")

else:
    print(" MOHON MASUKKAN NOMINAL YANG BENAR ")

print("="*40)







    





