#burada gerekli kütüphaneleri import ederiz
import cv2 as cv
import numpy as np
#burada eski örnekler gibi ana resimi gösteririz
img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Park',img)

#burada translate fonksiyonu ile alınan parametreler ile resimi istenildiği kadar taşır
def translate(img,x,y):
	transMat= np.float32([[1,0,x],[0,1,y]])#burada resimin ne kadar döndürüldüğünü belirtmek için bir matris yaparız
	dimnesions = (img.shape[1],img.shape[0]) #burada resimin kenar uzunlarını alırız
	return cv.warpAffine(img,transMat,dimnesions)# burada resimi istenildiği kadar taşır ve gerekli parametreleri gireriz


#bu fonksiyonda alınan parametreler ile görsel istenildiği kadar döndürülür
def rotate(img,angle,rotPoint=None):
	(height,width) = img.shape[:2] #burada görselin kenar uzunluklarını alırız

	if rotPoint is None: # burada döndürüldüğünde görselin merkeszinin neresi olduğunu belirleriz
		rotPoint =(width//2, height//2)

	rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)#burada nasıl döndürülaceğini belirten değerleri içeren bir matris yaparız
	dimensions= (width,height) # burada resimin boyutları bir değişkene aktarılır
	return cv.warpAffine(img,rotMat,dimensions) # bu fonksiyonla girilen parametreler neticeisnde resim istenilen derecede döndürülür


#burada rotate fonksiyonunun sonucu bir değişkene atanmış ve diğer fonksiyonlarda aynı şekilde birer değişkenlere atanmış
#rotate fonksiyonu ile istenilen derecede görsel döndürülür
#ardından görsel pencere şeklinde karşımıza çıkarılır diğer görsellerde aynı şekil yapılmıştır
rotated= rotate(img,45)
cv.imshow('Rotated', rotated)


#burada görseli saat yönünün tersine döndürürüz
rotated_rotated = rotate(rotated,-45)
cv.imshow('ROtated Rotated',rotated_rotated)

#burada resmi tekrar boyutlandırırız
#interpolation parametresi ile yeniden boyutlandırma metodunu seçeriz
resized = cv.resize(img,(500,500), interpolation= cv.INTER_CUBIC)
cv.imshow('Resized', resized)

#burada resimi istediğim pixel kadar kenar boşluğu bırakabiliyoruz
translated = translate(img, -100,100)
cv.imshow('translated', translated)

#bu fonksiyon ile resimi istediğimiz gibi takla attırabiliyoruz
flip= cv.flip(img, -1)
cv.imshow('Flip',flip)

#bu fonksiyon ile seçtiğimiz aralıkta görseli kesebiliyoruz
cropped = img[200:400,300:400]
cv.imshow('Cropper',cropped)

cv.waitKey(0)