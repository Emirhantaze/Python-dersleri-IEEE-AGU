import numpy as np
plate = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

firstplayercount = 0
secondplayercount = 0


def printboard(array):
    print("* 1  2  3 ")
    print(f"1 {array[0][0]}  {array[0][1]}  {array[0][2]} ")
    print(f"2 {array[1][0]}  {array[1][1]}  {array[1][2]} ")
    print(f"3 {array[2][0]}  {array[2][1]}  {array[2][2]} ")
    print()


for gametour in range(9):
    print(f"{gametour+1}.tur", end="\n")
    print(
        f"Puanlar \n1.oyuncu: {firstplayercount}\n2.oyuncu: {secondplayercount}")
    print()
    print(f"sıra {(gametour%2)+1}. oyuncuda\n")
    printboard(plate)
    secchar = input(">> Hangi harfi koymak istiyorsanız onu seçin lütfen\n>> ")
    while(secchar.lower() not in ["x", "o"]):
        secchar = input(
            ">> Hatalı seçim Hangi harfi koymak istiyorsanız onu seçin lütfen")
    secplace = input(
        "Lütfen koymak istediğiniz noktayı seçin (satırdaki sayıyı 10 ile çarpıp sütuna ekleyiniz)\n>> ")
    secsatır = (int(secplace)//10)-1
    secsutun = (int(secplace) % 10)-1
    while(plate[secsatır][secsutun] in ["x", "o"]):
        secplace = input(
            "Lütfen koymak istediğiniz noktayı seçin (satırdaki sayıyı 10 ile çarpıp sütuna ekleyiniz) eski seçilmiş bir noktayı seçemezsiniz!!!\n>> ")
        secsatır = (int(secplace)//10)-1
        secsutun = (int(secplace) % 10)-1
    plate[secsatır][secsutun] = secchar.lower()

    if (((np.array(plate)[secsatır] == np.array(["x", "o", "x"])).all() or (
            np.array(plate)[secsatır] == np.array(["o", "x", "o"])).all())):
        if gametour % 2 == 1:
            secondplayercount += 1
        else:
            firstplayercount += 1
        pass
    if (((np.array(plate)[::, secsutun] == np.array(["x", "o", "x"])).all() or (
            np.array(plate)[::, secsutun] == np.array(["o", "x", "o"])).all())):
        if gametour % 2 == 1:
            secondplayercount += 1
        else:
            firstplayercount += 1
        pass
    if (secsatır == secsatır):
        if(((plate[0][0] == "x") and (plate[1][1] == "o") and (plate[2][2] == "x")) or (((plate[0][0] == "o")) and (plate[1][1] == "x") and (plate[2][2] == "o"))):
            if gametour % 2 == 1:
                secondplayercount += 1
            else:
                firstplayercount += 1
            pass
    if(secsutun+secsatır) == 2:
        if((plate[0][2] == "x") and (plate[1][1] == "o") and (plate[2][0] == "x")) or ((plate[0][2] == "o") and (plate[1][1] == "x") and (plate[2][0] == "o")):
            if gametour % 2 == 1:
                secondplayercount += 1
            else:
                firstplayercount += 1
            pass
    printboard(plate)
