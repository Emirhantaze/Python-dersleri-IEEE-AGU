#       To int
b = int(3.45)
c = int("26")
d = int.from_bytes(bver, "big")

#       To float
b = float(35)
c = float("145.32")

#       To complex
b = complex("3+5j")

#       To string
", ".join(("Ali", "Ahmet", "Murat", "Hasan", "İbrahim", "Haydar"))
"{} ile {}".format("Ali", "Veli")
f"{9}+{8}={9+8}"
s = str(15)
str(someList) # [5, 3, 5, 1]
str(True) # True
str(someTuple) # (5, 3, 5, 1)
...
...

#       To bool
numbers -> 0 dan farklı
str     -> boş değil
bool    -> True
list    -> boş değil
tuple   -> boş değil
set     -> boş değil
dict    -> boş değil
bytes   -> 0 değil

int


#       To list
list(AnyIterable)
"Ahmet Ali Mehmet Murat".split(" ") # (seperator, maxSeprate)


#       To tuple
tuple(AnyIterable)


#       To set
set(AnyIterable)


#       To byte
someInt.to_bytes(5, "big") # little


