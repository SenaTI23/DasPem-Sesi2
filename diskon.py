# Input
totalBelanja = float(input("Masukkan total belanja  : Rp "))
uangDibayar = float(input("Masukkan uang dibayar   : Rp "))

# Diskon
if totalBelanja > 70.000:
    diskon = totalBelanja * 10 / 100
    totalBelanja -= diskon
else:
    diskon = 0

# Proses
kembalian = uangDibayar - totalBelanja

# Output
print("Total diskon            : Rp%.3f" % diskon)
print("Uang kembalianya adalah : Rp%.3f" % kembalian)
