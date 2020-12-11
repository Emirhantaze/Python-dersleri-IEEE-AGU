"""

ilk olarak hello world uygulamsı yapılacaktır

"""

# print(hello world)  # <<<< hatalı kullanım

print("hello world")  # <<<< doğru kullanım

h = "hello world"

print(h)  # farklı bir kullnım tarzı


"""

bu kullanımda print edilen dğerein sonuna mutalaka "\n"  "\n\r" gibi satır sonu byteları eklenir bunu değiştirmek için
end parametresini "" değerine eşitleyebiliriz

"""

print("hello")
print("world")
# satır atladı
print("hello", end=" ")
print("world")
# satır atlamadı
