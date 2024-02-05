#burada gerekli kütüphanelerimizi ekleriz
import cv2 as cv
import numpy as np 


#burada resimimizi okuruz
img = cv.imread('Resources/Photos/cats 2.jpg')
cv.imshow('Cats',img)

#burada resimimiz ile aynı boyuta sahip bir boş siyah görsel oluştururuz(sadece içi sıfır dolu bir dizi oluştururuz yani)
blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

#burada o boş görseli referans alarak içinde çember olara bir görsel daha oluştururuz
circle = cv.circle(blank.copy() ,(img.shape[1]//2 +45,img.shape [0]//2),100, 255,-1)
#cv.imshow('Mask', mask)

#burada aynı çember gibi ,bir diktörtgen daha oluştururuz
rectangle= cv.rectangle(blank.copy(), (30,30), (370,370),255,-1)

#burada o iki şeklin kesiştiği yeri alırız
weird_shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Wird Shape',weird_shape)

#burada o kesişen yer ile bizim görselimizin kesiştiği yeri alır ve çıktı olarak çıkarırız
masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('Masked Image', masked)


cv.waitKey(0)