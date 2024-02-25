#input
print("=" * 12, "SELAMAT DATANG TOKO BUAH UHUYYYY", "=" * 13)
salam2 = input("LAGI CARI BUAH FRESH DAN SEGAR ?")
salam5 = input("HARGA ECERAN DAN BORONGAN ?")
salam0 = input("YAHH BENAR , ANDA DITOKO YANG TEPAT")
salam3 = input("KAMI MENYEDIAKAN BERBAGAI MACAN BUAH FRESH DAN SEGAR")
salam4 = input("MULAI DARI JERUK,APEL,MANGGAH,MANGGIS,DAN DURIAN")
hargajeruk = 15.000 
hargaapel = 30.000
hargamanggah =20.000 
hargamanggis = 7.000 
hargadurian = 50.000 
print("=" * 60)
buahjeruk = float(input("Berapa kilo jeruk yang ingin dibeli ?   :"))
buahapel = float(input("Berapa kilo apel yang ingin dibeli ?    :"))
buahmanggah = float(input("Berapa kilo manggah yang ingin dibeli ? :"))
buahmanggis = float(input("Berapa kilo manggis yang ingin dibeli ? :"))
buahdurian = float(input("Berapa kilo durian yang ingin dibeli ?  :"))

#proses
uangjeruk = buahjeruk * hargajeruk
uangapel = buahapel * hargaapel
uangmanggah = buahmanggah * hargamanggah
uangmanggis = buahmanggis * hargamanggis
uangdurian = buahdurian * hargadurian
total = uangjeruk + uangapel + uangmanggah + uangmanggis + uangdurian


#output
print("=" * 60)
print("uang yang harus dibayar untuk buah jeruk adalah   Rp: %.3f"%uangjeruk)
print("uang yang harus dibayar untuk buah apel adalah    Rp: %.3f"%uangapel)
print("uang yang harus dibayar untuk buah mangga adalah  Rp: %.3f"%uangmanggah)
print("uang yang harus dibayar untuk buah manggis adalah Rp: %.3f"%uangmanggis)
print("uang yang harus dibayar untuk buah durian adalah  Rp: %.3f"%uangdurian)
print("=" * 60)
print("total yang harus dibayar adalah Rp: %.3f"%total)
print("=" * 60)
print("")
print("pembayaran bisa menggunakan tf bank,qris,ovo,dana,dan COD")
print("MENYEDIAKAN JUGA DELIVERY,GRATIS TANPA ONGKIR")