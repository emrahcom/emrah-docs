import math

def boyut_sec(eksen=0):
    while True:
        try:
            if eksen == 0:
                boyut = int(input("Satir sayisini giriniz: "))
            else:
                boyut = int(input("Sutun sayisini giriniz: "))

            if boyut < 2: raise
            if boyut > 40: raise

            return boyut
        except:
            print("Yanlis sayi girdiniz. Lutfen bir daha girin!")
            print()

def dik_ucgen_ciz():
    satir = boyut_sec()

    for i in range(1, satir + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

    print()

def eskenar_ucgen_ciz():
    satir = boyut_sec()

    for i in range(1, satir + 1):
        print(" " * (satir - i), end="")
        print("* " * i)

    print()

def kare_ciz():
    satir = boyut_sec()

    for i in range(satir):
        for j in range(satir):
            print("*", end=" ")
        print()

    print()

def dikdortgen_ciz():
    satir = boyut_sec()
    sutun = boyut_sec(1)

    for i in range(satir):
        for j in range(sutun):
            print("*", end=" ")
        print()

    print()

def daire_ciz():
    satir = boyut_sec()

    radius = satir // 2
    for y in range(-radius, radius+1):
        for x in range(-radius, radius+1):
            if math.sqrt(x**2 + y**2) <= radius + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

    print()

def sekil_sec():
    while True:
        try:
            print("1 - Dik ucgen")
            print("2 - Eskenar ucgen")
            print("3 - Kare")
            print("4 - Dikdortgen")
            print("5 - Daire")
            print()
            sekil = int(input("Sectiginiz seklin numarasini giriniz: "))

            if sekil not in [1, 2, 3, 4, 5]: raise
            return sekil
        except:
            print("Yanlis secim yaptiniz. Lutfen bir daha seciniz!")
            print()

while True:
    try:
        oyun_sayisi = int(input("Kac kere oyun oynamak istiyorsunuz: "))
        if oyun_sayisi < 0: raise
        if oyun_sayisi > 20: oyun_sayisi = 20

        for _ in range(oyun_sayisi):
            sekil = sekil_sec()

            if sekil == 1:
                dik_ucgen_ciz()
            elif sekil == 2:
                eskenar_ucgen_ciz()
            elif sekil == 3:
                kare_ciz()
            elif sekil == 4:
                dikdortgen_ciz()
            elif sekil == 5:
                daire_ciz()

        break;
    except:
        print("Yanlis sayi girdiniz. Lutfen bir daha girin!")
        print()
