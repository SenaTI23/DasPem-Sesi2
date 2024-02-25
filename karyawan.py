#input
print("=" * 19, "PT.MENCARI CINTA SEJATI", "=" * 15)
print("PROSES PENGHITUNGAN GAJI")
print("=" * 40)
nama = input("SILAHKAN MASUKAN NAMA ANDA            :")
waktulembur = int(input("berapa jam anda lembur selama sebulan :"))
harikerja = int(input("berapa hari anda masuk selama sebulan :"))

#proses
gajipokok = 115500 * harikerja
tunjangan = 1000000
transportasi = 11577 * harikerja
makan = 9650 * harikerja
lembur = 13000 * waktulembur 
totalgaji = gajipokok + tunjangan + transportasi + makan + lembur 

#output
print("")
print("=" * 19, "PT.MENCARI CINTA SEJATI", "=" * 15)
print("NAMA:",nama)
print("=" * 40)
print("GAJI POKOK   : %.0f"%gajipokok)
print("TUNJANGAN    : %.0f"%tunjangan)
print("TRANSPORTASI : %.0f"%transportasi)
print("MAKAN        : %.0f"%makan)
print("LEMBUR       : %.0f"%lembur)
print("=" * 40)
print("TOTAL GAJI   : %.0f"%totalgaji)
print("=" * 40)