import numpy as np

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape) #ilk sayı satır sayısını ikinci eleman ise sütun sayısını verir

print(a[0][0]) #Bu syntax bize iki boyutlu dizimizin içindeki elemanlara erişmemizi sağlar
print(a[:,1]) #Bu arama yönetemi ile istediğimiz satırı veya sütunu seçebiliyoruz

print(a.T) # Matrisimizin transpozunu alır

print(np.linalg.inv(a)) # bu komut verilen matrisin tersini alır eğer kare matris ise

print(np.linalg.det(a)) # bu komut ise determinantı hesaplar

print(np.diag(a)) # bu komut kçşegen elemanlarını verir

c= np.diag(a)

print(np.diag(c)) #bu da köşe hariç sıfır matris haline getirme formatıdır, burada bir oveerload fonksiyon kullanımı vardır


print("*************")

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)

b = a[0,1] # tek bir köşeli parantez ile de elemanları çekebiliriz

print(b)

b= a[0,1:4]
print (b)

b= a[-1,-2]
print (b)



a = np.array([[1,2],[3,4],[5,6]])

print(a)

bool_idx= a>2
print(bool_idx) #matrisde sıfırdan büyük yerleri true çevirdi tersini False

print(a[bool_idx]) #böylece a matrsinde 2'de büyük elemanları alabiliyoruz

print (a[a>2]) # Bu da basitleşmiş hali

b = np.where(a>2, a, -1)# verilen koşulda False olanlara -1 koydurduk
print(b)

print("************")
a = np.array([10,19,30,41,50,61])

print(a)

b = [1,3,5]

print(a[b]) # pythondaki listeyi kullanarak istediğimi elemanı alabiliyoruz

even = np.argwhere(a%2==0).flatten() # burada çift sayıları buldu ve ardından flatten fonksiyonu ile bunu tek boyutlu diziye çevirdi
print(a[even])

print("************")
a = np.arange(1,7)

print (a)
print (a.shape)

b = a.reshape((2,3)) # matrisi istediğin satır ve sütuna indirgiyor
print(b)
print("***********")

b = a[np.newaxis, : ] # matrisi tek satıra getirir sütunlara böler
print(b.shape)
print(b)


b = a[:, np.newaxis] # matrisi tek sütuna çevirir satırlara böler
print(b.shape)
print(b)

print("**********Birleştirme*********")


a = np.array([[1,2], [3,4]])

print(a)
b= np.array([[5,6]])
c = np.concatenate((a,b), axis=None)# Bu formatta tek boyut haline getirir
c = np.concatenate((a,b), axis=0)# Bu formatta ekler
c = np.concatenate((a,b.T), axis=1)# Bu format ile de yeterli sütun varsa her sütunun sonuna ekler
print(c)

print("**********************")

a= np.array([1,2,3,4,5,6])
b= np.array([7,8,10,11,12,13])

c= np.hstack((a,b)) # formatı ile sıralı ekleriz
c= np.vstack((a,b)) # ile sütun sütun ekleriz
print (c)

print("**********Broadcasting************")



x = np.array([[1,2,3],[4,5,6],[4,5,6],[1,2,3]])


a= np.array([1,0,1])

y= x + a
print(y) # böylece her x satırına a matrisini eklemiş olduk
# bu olay numpy'ın zekasını gösterir


print("*****************")

a = np.array([[7,8,9,10,11,12,13],[17,18,19,20,21,22,23]])


print(a)
print(a.sum(axis=None))# tüm elemanların toplamını verir
print(a.sum(axis=0))# tüm sütunları toplar
print(a.sum(axis=1))# tüm satırları toplar
print(a.mean(axis=1))# bu her sütundaki ortalamayı hesaplar
print(a.mean(axis=0))# her sütundkai ortalamayı verir
print(a.mean(axis=None))# tüm elemanların ortalamsını verir


print(a.var(axis=None)) # varyans hesaplar

print(a.std(axis=None)) # standart sapmasını hesaplar
print(np.std(a, axis= None)) # bu bir üstteki ifadeyle aynıdır


print(np.max(a, axis= None)) # bu ifade en büyük ifadayi döndürür
print(np.min(a, axis= None)) # bu ifade minumummu döndürür


print("*************")

x= np.array([1.0,2.0], dtype=np.int64) # bu kod yardımıyla numpy listemizin türünü değiştirebiliriz
print(x)
print(x.dtype)


print("*************")


a = np.array([1,2,3])

b = a

b[0]=42

print(b)
print(a)# numpy arrayları c++'taki gibi bellekte yer değişir


a = np.zeros((2,3)) # 2'ye 3 lük bir içi sıfır dolu bir matris oluşturur
print(a)

a = np.ones((2,3)) # 2'ye 3 lük bir içi 1 dolu bir matris oluşturur 
print(a.dtype)

a = np.full((2,3), 5.0) # 2'ye 3 lük bir içi istediğin eleman dolu bir matris oluşturur 
print(a.dtype)

a = np.eye(3)# köşegeni 1 olan bir sıfır matris oluşturur
print(a)

a = np.arange(20)# verilen sayıya kadar giden tek boyutlu dizi oluşturur
print(a)

a = np.linspace(0,10,5)# eşit aralıklı bir dizi oluşturur(eşit bölerek)
print(a)




print("*************")


a = np.random.random((1,2))#0-1 arasında rastgale değerli matris oluşturur(verdiğin değerler matrisin boyutunu belirler)
print(a)


a = np.random.randn(100)# 3 tane rastgele sayı verir tek boyuta
print(a.mean(), a.var())


a = np.random.randint(3,10,size=(3,3))# verilen aralıkta rastgale ve verilen boyutta sütun sayısı ve satır sayısınca bir matris üretir
print(a)

a = np.random.choice(5, size=10)# ilk verilen sayıya kadar olan sayılardan sonda verilen sayı kadar seçer 

a = np.random.choice([-8,-7,-6], size=10)# ilk üçündne rastgele bir tane seçer


