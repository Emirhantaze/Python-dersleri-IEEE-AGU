import numpy as np
# numpy yukarıda görülfüğü gibi importlanıyor
#
# içerisinde çağrılabilen şeylere bakmak iistersek
# print(dir(np))
# burada fonksiyon bize numpyın çağrılabilen özelliklerini gösteriyor
# bir numpy arrayi oluştumak ise çok kolay
nparr = np.array([1, 2, 3])
# fonksiyon içerisine list veriyoruz ve direk bu liste üzeinden yeni bir numpy arrayi dönüyor
# numpy arrayleri tam olarak listler gibi değildir sizeları predefined'dır javadaki gibi yani bir kısımını silme veya yeni değer ekleme yaoamayız
# ancak numpy fonksiyonları kullnılarak bu işlemler yeni array üretilerek yapılabilri
#
# elimize bir a arrayi alalım
a = np.array([1, 2, 3])
# ben bu arrayin sahip olduğu fonksiyonları görmek istiyorsam yukarıda yaptığımız gibi dir komutunu kullanabilriz
# print(dir(a))
# veya derste de göstericeğimiz vscode'un özelliklerini kullnabilrisiniz
# burada gördüğümüz komutlar normal listlerder daha farklıldır
#
# başka bri örne olarak yukarıda verdiğim a arrayine değer eklemeye çalışalım
a = np.append(a, 1)
print(a)
# göründüğü üzere
# aynı zamanda array üretirken bu elemanların türlerini de programa söyleyebiliriz
a = np.array(a, dtype=np.int)
# burada artık a arrayiin elemanları int olmak zorunluğu taşır ve inte castlenmeye çalısşır
a[1] = 0.1
print(a)
a[1] = "qwe1"
print(a)
# yukarı satırda int içerisine yazıldığında hata veren yani integera dönüştürlemeyen bir öğe görüyoruz bu size aslında elimizde kş data özgürlüğünü alıyor gibi
# bir çıkarım sunabiliri ama bazı durumlarda bu type checklerin ve dönüştürmelerin kullanılması işleri tahmin ettiğinizden çok kolaylaştırıyor.
#  *
