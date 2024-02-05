#burada gerekli kütüphaneleri ekleriz
import cv2 as cv 
import numpy as np

#burada resmimizi okuruz
img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Cats', img)

#burada resmimizi griye çeviririz
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)


#burada gri görselimize kenar tespiti fonksiyonu ile kenar tespiti yapılır
lap = cv.Laplacian(gray,cv.CV_64F)
#ardından burada ise numpy kullanılarak lap'ın değerlerinin mutlak değeri alınıp uint8 formatına çevrilir
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

#burada ise farklı bir kenar bulma fonksiyonu kullanırız bu fonksiyonda yatay ve dikey olarak kenarlar bulunur
#ardından CV_64F formatı ile değerler 64 formatına dönüştürülür 
sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

#ardından bu yapılan kenar bulmalar bitwise ile or mantık işlemi kullanılarak yeni bir kenar bulma yöntemi elde ediyoruz
combined_sobel= cv.bitwise_or(sobelx,sobely)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('soblex or sobley',combined_sobel)

#burada ise bir diğer kenar bulma yöntemi kullanılıyor
canny= cv.Canny(gray,150,175)
cv.imshow('Canny',canny)

#sonuç olarak bir nesne tespit edilme gibi konularda bu kenar bulma konularında hangisinin nerede daha iyi 
#iş göreceğini öğreneceğiz

cv.waitKey(0)