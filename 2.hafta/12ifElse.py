
"""
toplam = 0
n = int(input())
while n>0:
    toplam += n
    n = int(input())
print(f"toplam = {toplam}")
"""

"""
age = int(input("yaş: "))
if age > 18:
    print(f"yaşın {age}. araba ehliyeti alabilirsin")
    print(f"yaşın {age}. araba ehliyeti alabilirsin")

toplam = 0
while True:
    n = int(input(">>"))
    if n == -5:
        continue
    if n <= 0:
        break
    toplam += n
print(f"toplam = {toplam}")
"""
"""
isimler = ["Ahmet", "Emirhan", "Mehmet ali", "Poyraz"]

for isim in isimler:
    print(f"Hoşgeldin {isim}")
"""

ages = [19, 25, 7, 27, 20, 36, 35, 5]


for i in ages:
    print(f"Yaş = {i}", end="")
    if i < 18:
        print(" !!  18 yaşından küçük biri var", end="")
    print()




"""ad = input("Adınızı girin: ")
age = int(input("Yaşınızı girin: "))


print(f"adı: {ad}, yaşı: {age}")

5
10
15
-2"""



