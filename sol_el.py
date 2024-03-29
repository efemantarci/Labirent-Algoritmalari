import numpy
import time
#simgeler
duvar = "#"
karakter = "A"

baslangic = [4,3]
bitis = [3,3]
karakterX = baslangic[1]
karakterY = baslangic[0]
bitisX = bitis[1]
bitisY = bitis[0]
yonelim = "Y" # Y yukarı A aşağı L sol R sağ
labirent = [["#","#","#","#","#","#","#"],
            ["#","/","/","/","/","/","#"],
            ["#","/","#","#","#","/","#"],
            ["#","/","#","/","#","/","#"],
            ["#","/","/","/","/","/","#"],
            ["#","#","#","/","#","#","#"],]
maxX = len(labirent[0])
maxY = len(labirent)
# Önce y sonra x kullanılıyor
def duvar_kontrol(labirent,y,x):
    global yonelim
    if yonelim == "Y":
        if x - 1 >= 0 and labirent[y][x-1] != duvar:        #sol duvar
            print("Sola dön")
            return 1
        elif y - 1 >= 0 and labirent[y - 1][x] != duvar: #ön duvar
            print("Öne git")
            return 2
        elif x + 1 < maxX and labirent[y][x + 1] != duvar: #sağ duvar
            print("Sağa dön")
            return 3
        else:
            print("180 dön")
            return 4
    elif yonelim == "L":
        if y + 1 < maxY and labirent[y + 1][x] != duvar: #sol duvar
            print("Sola dön")
            return 1
        elif x - 1 >= 0 and labirent[y][x-1] != duvar:#ön duvar
            print("Öne Git")
            return 2
        elif y - 1 >= 0 and labirent[y - 1][x] != duvar: #sağ duvar
            print("Sağa dön")
            return 3
        else:
            print("180 dön")
            return 4
    elif yonelim == "A":
        if x + 1 < maxX and labirent[y][x + 1] != duvar: #sol duvar
            print("Sola dön")
            return 1
        elif y + 1 < maxY and labirent[y + 1][x] != duvar: #ön duvar
            print("Düz git")
            return 2
        elif x - 1 >= 0 and labirent[y][x-1] != duvar:#sağ duvar
            print("sağa dön")
            return 3
        else:
            print("180 dön")
            return 4
    elif yonelim == "R":
        if y - 1 >= 0 and labirent[y - 1][x] != duvar: #sol duvar
            print("Sola dön")
            return 1
        elif x + 1 < maxX and labirent[y][x + 1] != duvar: #ön duvar
            print("Düz git")
            return 2
        elif y + 1 < maxY and labirent[y + 1][x] != duvar: #sağ duvar
            print("Sağa dön")
            return 3
        else:
            print("180 dön")
            return 4
            
def hareket(labirent,y,x,mod):
    global karakterX
    global karakterY
    global yonelim
    labirent[y][x] = 0
    if yonelim == "Y":
        if mod == 1:
            yeniX = x - 1
            yeniY = y
            yonelim = "L"
        if mod == 2:
            yeniX = x
            yeniY = y - 1
        if mod == 3:
            yeniX = x + 1
            yeniY = y
            yonelim = "R"
        if mod == 4:
            yeniX = x
            yeniY = y + 1
            yonelim = "R"
        labirent[yeniY][yeniX] = karakter
    elif yonelim == "A":
        if mod == 1:
            yeniX = x + 1
            yeniY = y
            yonelim = "R"
        if mod == 2:
            yeniX = x
            yeniY = y + 1
        if mod == 3:
            yeniX = x - 1
            yeniY = y
            yonelim = "L"
        if mod == 4:
            yeniX = x
            yeniY = y - 1
            yonelim = "Y"
        labirent[yeniY][yeniX] = karakter
    elif yonelim == "L":
        if mod == 1:
            yeniX = x
            yeniY = y + 1
            yonelim = "A"
        if mod == 2:
            yeniX = x - 1
            yeniY = y
        if mod == 3:
            yeniX = x
            yeniY = y - 1
            yonelim = "Y"
        if mod == 4:
            yeniX = x + 1
            yeniY = y
            yonelim = "R"
    elif yonelim == "R":
        if mod == 1:
            yeniX = x
            yeniY = y - 1
            yonelim = "Y"
        if mod == 2:
            yeniX = x + 1
            yeniY = y
        if mod == 3:
            yeniX = x
            yeniY = y + 1
            yonelim = "A"
        if mod == 4:
            yeniX = x - 1
            yeniY = y
            yonelim = "L"
    labirent[yeniY][yeniX] = karakter
    karakterX = yeniX
    karakterY = yeniY
def labirent_ciz(labirent):
    for y in range(maxY):
        for x in range(maxX):
            print(labirent[y][x],end = " ")
        print()
labirent_ciz(labirent)
while(labirent[bitisY][bitisX] != karakter):
    mod = duvar_kontrol(labirent,karakterY,karakterX)
    hareket(labirent,karakterY,karakterX,mod)
    labirent_ciz(labirent)
    time.sleep(0.5)
