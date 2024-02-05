#gerekli kütüphaneleri import ederiz
import cv2 as cv 
import numpy as np

#burada içi sıfır dolu bir dizi oluştururuz
blank = np.zeros((400,400), dtype='uint8')

#burada ise o diziyi görsele çevirip o görsele bir dörtgen çizeriz
rectangle= cv.rectangle(blank.copy(), (30,30), (370,370),255,-1)

#burada ise sadece dörtgendeki işlemden ayrı olarak daire çizeriz ve bunu dikdörtgendeki gibi bir değişkene atarız
circle = cv.circle(blank.copy(), (200,200) ,200, 255,-1)


cv.imshow('Circle',circle)
cv.imshow('rectangle',rectangle)

#burada oluşturduğumuz görsellerin kesişen görselleri ile yeni bir görsel oluşturduk
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise And', bitwise_and)

#burada ise şekillerin toplamını alır
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise or', bitwise_or)

#burada ise iki şeklin sadece kesiçen kısmını alır
bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('Bitwise XOR',bitwise_xor)

bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('Bitwise not',bitwise_not)

#yani toplamda olay şöyle;
#eğer ilk resimdeki pixel değeri ikini görselde de aynı değerse
#sonuç görsele bu pixel eklenir eğer değil ise sonuç pixel 0 olarak karşımıza çıkar
#bunlar and için di diğerleri ise temel logic işaretlerin olduğu mantık ile aynı





cv.waitKey(0)