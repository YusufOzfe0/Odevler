#burada gerekli kütüphaneleri ekleriz
import cv2 as cv 
#burada resimimizi okuruz
img = cv.imread('Resources/Photos/group 1.jpg')
cv.imshow('Person',img)

#burada rengimizi griye çeviririz
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person',gray)

#burada opencv nin bir sınıflandırma fonksiyonunu kullanırız
#verdiğimiz değer ise opencv nin kendi githubından aldığımız bir verisetinin dosya yoludur
#burada haar_cascade değişkenini bir sınıflandırı olarak ayarlarınz
haar_cascade= cv.CascadeClassifier('haar_face.xml')

#burada haar_cacade in bir fonksiyonu ile gray olarak verdiğimiz resimin
#olası haar_face.xml dosyasıyla uyuşan verileri veren bir fonksiyondur
#scaleFactor ile aranan bölgenin ölçeğini verir
#minNeighbors ise güvenilirlik derecesidir
faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=1)

#burada ise resimdeki yüz sayısını yazdıran print fonksiyonu vardır
#faces_react ifadesindeki herbir box konumunu 1 yüz olarak alabiliriz
print(f'Number of faces found = {len(faces_rect)}')

#burada faces_react dizisindeki her bir değer dolaşılarak verilen kutulara birer dikdörtgen koyulur
for (x,y,w,h) in faces_rect:
	cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0), thickness=2)


cv.imshow('Yeni Goruntu', img)










cv.waitKey(0)


