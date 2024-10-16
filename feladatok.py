import random

def feladat1(szam1:int):
    while (szam1 % 2) == 0:
        szam1 = int(input("Ez páros, kérek egy páratlant: "))
    print(szam1)

def feladat2():
    oszthatok = 0
    for i in range(0,7,1):
        szam1 = int(random.random()*96)+5
        if (szam1 % 5) == 0:
            oszthatok += 1
    return oszthatok

def feladat3(text:str,betu:str):
    i = 0
    for a in range(len(text)):
        if text[a] == betu:
            i += 1
        a += 1
    print(f"a szövegben {i}db {betu} betű van")

def feladat4(szoveg):
    nevek = []
    nevek.append(szoveg)
    while szoveg != "@":
        nevek.append(szoveg)
        szoveg = str(input("még egyet:"))
    nevekdb = len(nevek)
    return nevekdb

def feladat5(felhasznalo_tippje):
    felhasznalo_tippje.lower
    tipp1 = 0
    tipp2 = 0
    mikrobi = int(random.random()*4)+1

    if felhasznalo_tippje == "kő":
        tipp1 == str("kő")
    elif felhasznalo_tippje == "papír":
        tipp1 == str("papír")
    else:
        tipp1 == str("olló")

    if mikrobi == 1:
        tipp2 == str("kő")
    elif mikrobi == 2:
        tipp2 == str("papír")
    else:
        tipp2 == str("olló")

    if tipp1 == tipp2:
        print("Döntetlen!")
    elif tipp1 == "kő" and tipp2 == "papír":
        print("")