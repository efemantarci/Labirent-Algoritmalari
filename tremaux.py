import time
#simgeler
bosluk = 0
duvar = 9
karakter = "A"

baslangic = [6,3]
bitis = [3,3]
karakterX = baslangic[1]
karakterY = baslangic[0]
bitisX = bitis[1]
bitisY = bitis[0]
oncekiX = baslangic[1]
oncekiY = baslangic[0]
onceki = 0

geriDonusNSayaci = 0
geriDonuluyor = 0
onceoncekiY ="B"
onceoncekiX = "D"
N = 2
X = 1
yonelim = "Y" # Y yukarı A aşağı L sol R sağ
labirent = [[9,9,9,9,9,9,9],
            [9,0,0,0,0,0,9],
            [9,0,9,9,9,0,9],
            [9,0,9,0,9,0,9],
            [9,0,9,0,9,0,9],
            [9,0,0,0,0,0,9],
            [9,9,9,0,9,9,9],]
kesisimNoktalari = []
maxX = len(labirent[0])
maxY = len(labirent)
# Önce y sonra x kullanılıyor     
def duvar_kontrol(labirent,y,x,emir = 0):
    global yonelim
    global geriDonuluyor
    global karakter
    if not geriDonuluyor:
        if yonelim == "Y":
            if labirent[y - 1][x] == N:
                print("AGAAAA")
                geriDonuluyor = 1
                karakter = "B"
                return 4
            elif x - 1 >= 0 and labirent[y][x-1] == bosluk:#sol duvar
                print("Sola dön")
                return 1
            elif y - 1 >= 0 and labirent[y - 1][x] == bosluk: #ön duvar
                print("Öne git")
                return 2       
            elif x + 1 < maxX and labirent[y][x + 1] == bosluk: #sağ duvar
                print("Sağa dön")
                return 3
            else: 
                print("180 dön")
                return 4
        elif yonelim == "L":
            if labirent[y][x - 1] == N:
                print("AGAAAA")
                geriDonuluyor = 1
                karakter = "B"
                return 4
            elif y + 1 < maxY and labirent[y + 1][x] == bosluk: #sol duvar
                print("Sola dön")
                return 1
            elif x - 1 >= 0 and labirent[y][x-1] == bosluk:#ön duvar
                print("Öne git")
                return 2       
            elif y - 1 >= 0 and labirent[y - 1][x] == bosluk: #sağ duvar
                print("Sağa dön")
                return 3
            else:
                print("180 dön")
                return 4
        elif yonelim == "A":
            if labirent[y + 1][x] == N:
                print("AGAAAA")
                geriDonuluyor = 1
                karakter = "B"
                return 4
            elif x + 1 < maxX and labirent[y][x + 1] == bosluk: #sol duvar
                print("Sola dön")
                return 1
            elif y + 1 < maxY and labirent[y + 1][x] == bosluk: #ön duvar
                print("Öne git")
                return 2       
            elif x - 1 >= 0 and labirent[y][x-1] == bosluk:#sağ duvar
                print("sağa dön")
                return 3
            else:
                print("180 dön")
                return 4
        elif yonelim == "R":
            if labirent[y][x + 1] == N:
                print("AGAAAA")
                geriDonuluyor = 1
                karakter = "B"
                return 4
            if y - 1 >= 0 and labirent[y - 1][x] == bosluk: #sol duvar
                print("Sola dön")
                return 1
            elif x + 1 < maxX and labirent[y][x + 1] == bosluk: #ön duvar
                print("Öne git")
                return 2       
            elif y + 1 < maxY and labirent[y + 1][x] == bosluk: #sağ duvar
                print("Sağa dön")
                return 3
            else:
                print("180 dön")
                return
    if geriDonuluyor:
        if not gezilmedik_kontrol(labirent,y,x):
            print("LA YER KALMADI LAAA")
            print(x_bul(labirent,y,x,yonelim))
            return x_bul(labirent,y,x,yonelim)
        elif yonelim == "Y":
            if x - 1 >= 0 and labirent[y][x-1] != duvar:#sol duvar
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
                print("Öne git")
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
                print("Öne git")
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
                print("Öne git")
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
    global karakter
    global yonelim
    global oncekiY
    global oncekiX
    global onceki
    global onceoncekiX
    global onceoncekiY
    global geriDonuluyor
    global geriDonusNSayaci
    birKez = 0
    labirent[y][x] = onceki
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
    #string gibi algıladığı için hardcodeladım
    if geriDonuluyor and labirent[yeniY][yeniX] == N: # geri dönerken N ye gelinirse
        yon = kesisimini_bul(labirent,yeniY,yeniX,yonelim)
        print("YÖNNNNNNNNNNNNNNNNNNNNNNNNNNNN")
        print(yon)
        birKez = 1 # bir kez çalışması için
    if kesisim_mi(labirent,y,x):
        #Kesişime girerken X at
        if labirent[y][x+ 1] != X and labirent[y][x- 1] != X and labirent[y- 1][x] != X and labirent[y + 1][x] != X:
            labirent[onceoncekiY][onceoncekiX] = X
    if kesisim_mi(labirent,oncekiY,oncekiX):
        labirent[yeniY][yeniX] = N
        # Düzgün isim koyamadım la
        if geriDonuluyor == 1:
            geriDonusNSayaci += 1
            if geriDonusNSayaci == 2:
                geriDonuluyor = 0
                geriDonusNSayaci = 0
                karakter = "A"
    #string gibi algıladığı için hardcodeladım
    onceki = labirent[yeniY][yeniX]
    if labirent[yeniY][yeniX] != N or labirent[yeniY][yeniX] != X:
        labirent[yeniY][yeniX] = karakter
        
    onceoncekiY = oncekiY
    onceoncekiX = oncekiX     
    oncekiY = yeniY
    oncekiX = yeniX
    karakterX = yeniX
    karakterY = yeniY
    if birKez:
        hareket(labirent,yeniY,yeniX,yon)
        birKez = 0
def labirent_ciz(labirent):
    for i in range(maxY):
        print(labirent[i])
def kesisimini_bul(labirent,y,x,yonelim):
    if yonelim == "Y":
        if kesisim_mi(labirent,y - 1,x): # ön
            return 2
        elif kesisim_mi(labirent,y + 1,x): # arka
            return 4
        elif kesisim_mi(labirent,y,x - 1): # sol
            return 1
        elif kesisim_mi(labirent,y,x + 1): # sağ
            return 3
    if yonelim == "A":
        if kesisim_mi(labirent,y + 1,x): # ön
            return 2
        elif kesisim_mi(labirent,y - 1,x): # arka
            return 4
        elif kesisim_mi(labirent,y,x + 1): # sol
            return 1
        elif kesisim_mi(labirent,y,x - 1): # sağ
            return 3
    if yonelim == "L":
        if kesisim_mi(labirent,y,x - 1): # ön
            return 2
        elif kesisim_mi(labirent,y,x + 1): # arka
            return 4
        elif kesisim_mi(labirent,y + 1,x): # sol
            return 1
        elif kesisim_mi(labirent,y - 1,x): # sağ
            return 3
    if yonelim == "R":
        if kesisim_mi(labirent,y,x + 1): # ön
            return 2
        elif kesisim_mi(labirent,y,x - 1): # arka
            return 4
        elif kesisim_mi(labirent,y - 1,x): # sol
            return 1
        elif kesisim_mi(labirent,y + 1,x): # sağ
            return 3
    
def kesisim_mi(labirent,y,x):
    if x + 1 < maxX and x - 1 >= 0 and y + 1 < maxY and y - 1 >=0:
        if labirent[y][x - 1] + labirent[y][x + 1] + labirent[y - 1][x] + labirent[y + 1][x] <= 7:
            return 1
        else:
            return 0
def gezilmedik_kontrol(labirent,y,x):
    if labirent[y][x - 1] + labirent[y][x + 1] + labirent[y - 1][x] + labirent[y + 1][x] == 7:
        return 0
    else:
        return 1
def x_bul(labirent,y,x,yonelim):
    global X
    if yonelim == "Y":
        if labirent[y - 1][x] == X: # ön
            return 2
        elif labirent[y + 1][x] == X: # arka
            return 4
        elif labirent[y][x - 1] == X: # sol
            return 1
        elif labirent[y][x + 1] == X: # sağ
            return 3
    if yonelim == "A":
        if labirent[y + 1][x] == X: # ön
            return 2
        elif labirent[y - 1][x] == X: # arka
            return 4
        elif labirent[y][x + 1] == X: # sol
            return 1
        elif labirent[y][x - 1] == X: # sağ
            return 3
    if yonelim == "L":
        if labirent[y][x - 1] == X: # ön
            return 2
        elif labirent[y][x + 1] == X: # arka
            return 4
        elif labirent[y + 1][x] == X: # sol
            return 1
        elif labirent[y - 1][x] == X: # sağ
            return 3
    if yonelim == "R":
        if labirent[y][x + 1] == X: # ön
            return 2
        elif labirent[y][x - 1] == X: # arka
            return 4
        elif labirent[y - 1][x] == X: # sol
            return 1
        elif labirent[y + 1][x] == X: # sağ
            return 3
labirent_ciz(labirent)
while(labirent[bitisY][bitisX] != karakter):
    mod = duvar_kontrol(labirent,karakterY,karakterX)
    hareket(labirent,karakterY,karakterX,mod)
    labirent_ciz(labirent)
    time.sleep(0.5)
    print("Önceki =")
    print(onceki)    

