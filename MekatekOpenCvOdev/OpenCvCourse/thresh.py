#burada gerekli kütüphaneleri import ederiz
import cv2 as cv 

#burada görselimizi okuruz
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats', img)


#burada görselimizi griye çeviririz
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#burada threshold fonksiyonu belirli bir eşik değerinden az olan gri tonlarını direkt siyaha çevirmeye yarar
threshold, thresh = cv.threshold(gray,175, 255,cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

#burada ise sadece threshold fonksiyonunun siyah yerine beyaz hali
threshold, thresh_inv = cv.threshold(gray,175, 255,cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inv', thresh_inv)

#burada belirli metotlar ve yöntemler kullanarak lokal olarak grinin yüksek olduğu bölgelerde 
#rengi beyazlatma gibi metotlar ile farklı bir eşik sınıflandırması yapıyoruz
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,9,5)
cv.imshow('Adaptive Thresholded', adaptive_thresh)




cv.waitKey(0)