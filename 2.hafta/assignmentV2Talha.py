# hangi hücre birleşimleri oyunu kazandırıyor
winConditions = ({"11","21","31"}, {"12", "22", "32"}, {"13","23","33"}, {"11","12","13"}, {"21","22","23"}, {"31","32","33"}, {"11","22","33"}, {"13","22","31"})
# oyuncular ve oyuncuların seçtiği hücreler
playerCells = {"x": set(), "y": set()}
# hangi hücrede ne olduğu
gameBoard = {"11":" ", "12":" ", "13":" ", "21":" ", "22":" ", "23":" ", "31":" ", "32":" ", "33":" "}
# hangi oyuncudan sonra hangi oyuncunun geldiği
nextPlayer = {"x":"y", "y":"x"}

# fonksiyon tanımlaması sonra gösterilecek
def printGameTable():
    # üst kısmı yaz
    print("  1 2 3")
    # 1, 2 ve 3 satırları için
    for y in "123":
        # hangi satırda olduğunu yaz
        print(y,end=" ")
        # 1, 2, 3 sütunları için
        for x in "123":
            # o sütunda ne varsa yaz boşluk bırak
            print(gameBoard[y+x], end=" ")
        # sonraki satıra geç
        print()

# ilk başlayan oyuncu
player = "x"
# tahtadaki hücre kadar tur oynanabilir
turn = len(gameBoard)

# oynanacak tur oldukça
while turn>0:
    # tahtayı yazdır
    printGameTable()
    # kimin sırası olduğunu yaz
    print(f"It is {player}'s turn")
    # nereye koymak istediğini al
    targetCell = input(">> ").strip()
    # eğer girilen input oyun hücrelerinden birini temsil etmiyorsa 
    if targetCell not in gameBoard:
        print("Böyle bir hücre yok")
    # eğer o hücre boşluk değil başka bir değer is
    elif gameBoard[targetCell] != " ":
        print("Hücrede başka bir taş var")
    # iki koşulu da sağlamıyorsa düzgün bir girdidir
    else:
        # tahtada o hücreyi player yapıyoruz
        gameBoard[targetCell] = player
        # o oyuncunun oynadığı hücrelere aldığımız inputu ekliyoruz
        playerCells[player].add(targetCell)
        # eğer kazanmak koşullarından herhangi biri o oyuncunun oynadığı yerin alt kümesi ise
        if any(condition.issubset(playerCells[player]) for condition in winConditions):
            print(f"Oyuncu {player} oyunu kazandı")
            break
        # değilse sonraki oyuncuya geç
        player = nextPlayer[player]
        # oynanabilecek tur sayısını bir azalt
        turn -= 1

# eğer oynanacak tur kalmamışsa
if turn==0:
    print("Oyun berabere bitti")