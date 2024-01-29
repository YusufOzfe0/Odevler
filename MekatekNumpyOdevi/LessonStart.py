import numpy as np
a = np.array([1,2,3])
print(np.__version__) #numpy versiyonunu verir
print(a)
print(a.shape) #dizinin şeklini verir
print(a.dtype) # dizinin tipini verir
print(a.ndim) # dizinin boyutunu verir
print(a.size) # dizinin toplam içerik sayısını verir
print(a.itemsize) # her bir elemana düşen byte'ı verir
print("**********")

print(a[0])
a[0] = 10
print(a)

b = a * np.array([2,0,2]) # her bir elemanı kendi index sırasında olan ile çarpar
print(b)

print("************")

l= [1,2,3]
a = np.array([1,2,3])

l.append(4)
l=l + [5]
print(l)
l = l * 2
print(l)
a = a + np.array([4]) #sadece her bir üyeye 4 ekler
#a.append(4) listeler aynı gözükür ama aynı değildir
print(a)
a = a *2
print (a)
#Çıktılardan görüldüğü üzere numpy daha akıllıdır

a = np.sqrt(a)
print(a)

l1 = [1,2,3]
l2 = [4,5,6]

a1 = np.array(l1)
a2 = np.array(l2)
dot = 0
for i in range(len(l1)):
    dot += l1[i] * l2[i]
print(dot)

dot = np.dot(a1,a2) # burada tek komut ile çok daha hızlı bir şekilde sonuç alabiliriz
print(dot)

sum1 = a1 * a2

dot = (a1 * a2).sum() # basit bir operator kullanarak bile bu işlemler yapılabiliri
print(dot)

dot = a1 @ a2 # burada da aynı şekil basit bir operator ile işlemi çok kısaltır
print(dot)










