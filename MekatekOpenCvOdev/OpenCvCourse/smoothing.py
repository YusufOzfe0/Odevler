#burada gerekli kütüphaneler eklenir
import cv2 as cv

#burada görselimiz okunur
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

#burada çevredeki pixellerin renk ortalamasını alarak ortadaki resmin rengini belirleyen bir resim bulanıklaştırma fonksiyonu öğrendik
average= cv.blur(img,(3,3))
cv.imshow('Average Blur', average)

#burada daha farklı bir şekilde verilen katsayıya göre bulanıklaştırma uygulaması gördük
gauss= cv.GaussianBlur(img,(3,3), 0)
cv.imshow('GaussianBlur',gauss)

#burada çevredeki piksellerin medyanını alan bir bulanıklaştırma metodu gördük
median=cv.medianBlur(img,3)
cv.imshow('Median Blur',median)


#burada ise iki taraflı filtreleme adında başka bir metodu öğrendik 
bilateral = cv.bilateralFilter(img,10,80,65)
cv.imshow('bilateral',bilateral)
#verilen parametreler ile görüntünün ne kadar bozulacağı kenarların ne kadar korunacağı tarzı işlemlerin boyutunu ayarlarız







cv.waitKey(0)