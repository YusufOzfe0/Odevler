#burada gerekli kütüphaneleri ekleriz
import cv2 as cv
import numpy as np 

#burada resimimizi okuruz
img =cv.imread('Resources/Photos/park.jpg')
cv.imshow('Park',img)


#bura boş siyag bir görsel oluştururuz
blank = np.zeros(img.shape[:2], dtype='uint8')


#burada resimimizin renklerinin yoğunluğunu birer değişkenlere atarız
b,g,r= cv.split(img)

#burada o değişkenler ile blank görsellerini birleştirerek her rengin ana görselde ne kadar olduğunu görürüz
blue= cv.merge([b,blank,blank])
green= cv.merge([blank,g,blank])
red= cv.merge([blank,blank,r])


#burada bu görselleri çıktı olarak çıkarırız
cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)

#burada her görselin boyutlarını çıktı olarak alırız(mesela uzunluk genişlik , renk çeşitliliği)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

#burada yukarıda ki gibi bir renk birleştirme yaparak üç ana görseli tekrardan ilk haline getiririz ve çıktısını alırız
merged = cv.merge([b,g,r])
cv.imshow('Merged image',merged)

cv.waitKey(0)