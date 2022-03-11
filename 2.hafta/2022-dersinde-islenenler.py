"""
Önce Nasıl Input aldğımızı hatılayalım.
"""

# yas = int(input("Yaşınızı girin: "))

"""
yas = int(input("Yaşınızı girin: "))

if (yas>= 18):
    print("Reşitsin.")
elif yas>=16:
    print("16 yaşından büyüksün.")
else:
    print("sağlana durumlara uygun değilsin")
"""

"""
a = [1 ,3 ,4]
a[1]
for i in range(5):
    eksi = "*" * i*2
    print(eksi.center(15))
"""
"""
i = 100
while i > 5:
    print("xxxxxx")
    i = i /5
yas = int(input("Yaşınızı girin: "))

tablo[0][0] +=1
print("test",end = " ")
"""
tablo = [[0,0,0],[0,0,0],[0,0,0]]
cevap = "evet"
while cevap == "evet":
    a = int(input("birinci değer "))
    b = int(input("ikinci değer "))
    tablo[a][b] +=1
    for i in range(len(tablo)):
        for j in range(len(tablo[0])):
            print(tablo[i][j],end = " ")
        print()
    cevap = input( "Devam etsin mi? ")