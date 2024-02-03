print("\t\tTIKET BUS\t\t")
print("-"*30)
print("Kode kota:")
print("1. Prabumulih")
print("2. Muara Enim")
print("3. Lubuklinggau")
x = int(input("Pilihan kota (1/2/3)\t\t: "))
print("kode kelas :")
print("1. ekonomi")
print("2. bisnis")
print("3. eksekutif")
y = int(input("Pilihan kelas (1/2/3)\t\t: "))
z = int(input("Banyak tiket\t\t\t: "))

if (x == 1):
    if (y == 1):
        a = 100000
    elif (y ==2):
        a = 400000
    elif (y == 3):
        a = 700000
elif (x == 2):
    if (y == 1):
        a = 200000
    elif (y ==2):
        a = 500000
    elif (y == 3):
        a = 800000
if (x ==3 ):
    if (y == 1):
        a = 300000
    elif (y ==2):
        a = 600000
    elif (y == 3):
        a = 900000
subtotal = a*z
harga_diskon = 0
if (x == 2 and y ==1):
    promo = str(input("Kode promo\t\t\t: "))
    if (promo == "igs"):
        diskon = 0.1
        harga_diskon = subtotal*diskon

elif(x == 3 and y == 3):
    promo = str(input("Kode promo\t\t\t: "))
    if (promo == "igs"):
        diskon = 0.1
        harga_diskon = subtotal*diskon
        

print("-"*30)


harga_tiket = a
print ("Harga tiket\t\t\t: RP", a)
print ("Sub-total\t\t\t: RP", subtotal)
print ("Diskon\t\t\t\t: RP", int(harga_diskon))
print ("Total-Bayar\t\t\t: RP", int(subtotal - harga_diskon))

