#
#
# for döngüsü
#
#
# *

# for i in range(12):  # in değerinden sonra iterable vermemiz gerekiyor
#     print(i+123)
#     pass

bayrak = True
while bayrak:
    yas = input("yaşınızı giriniz: ")

    if (yas.lower() == "bitir"):
        bayrak = False
    elif yas == "":
        pass
    elif(int(yas) < 18):
        print("ehliyet alamazsın")
    else:
        print("ehliyet alabilirsin")
