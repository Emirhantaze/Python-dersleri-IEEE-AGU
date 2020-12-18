import numpy as np
a = np.array([[1, 2], [3, 4], [4, 5]])

# yuarıda yazdığom kullanım normal listlerde kullanılmaz
print(a[:, 1])
#  burada yaptığım aslında stütun olarak seçmek oluyor ve seçim normal listlerde olanın aksine çok daha kolay bir şekilde oluyor bunun bir
# sebebi aslında pythonda dediğim gibi listlre ratgele objelerin arka arkya eklenmesi oluyor bu durumda elemanların şekli bilinmediği için erişemmiyoruz
# örneğin

a = [[1, 2], [1, 2]]
# şimdi diyelim ki a listesininde ki [1,1] kısmına ulaşmaya çalışıyorum burada herhangi bir özel komut kullanmazsak yani ilk derse gösterdiğimiz zip olsun vesaire
# ulaşmak için elindeki eleman sayısı kadarlık bir for yapıp tüm elemanları nir arraye koymmız gerek
out = []
for i in range(len(a)):
    out.append(a[i][0])
print(out)
# bu şekilde olabilir yada tek saatır kısaltması da kullanbiliriz
print([a[i][0] for i in range(len(a))])
# burada yaptığım gibi bu imkansız bir şey değil ancak numpy burada bize kolay erişim imkanı sağlıyor
# aynı zamanda bu değerler asılnda birer tuple olduğunu düşünecek olursak bir arrayden list kullanarak seçim yapabiliyoruz mesela
a = np.array([1, 2, 3, 4, 5])
k = [0, 2, 3]  # burada istediğimiz tarzı kullanbiliyoruz yani np arrayi de olabilir
print(a[k])
print(list(a)[k])
# gördüğümüz gibi yukarıdaki satır hata verirken elimizdeki arraye çok kolay bir şekilde ulaşmış oluduk
# normal şartlarda listelrin de birden çok öğesi geri döndğrebilri ancak bunlar belli bir formatta olma zoruluğu vardır
# ancak bizim verdiğimiz kısım herhangi bir sırası olmadan verilen rastgele seçilen indexler
