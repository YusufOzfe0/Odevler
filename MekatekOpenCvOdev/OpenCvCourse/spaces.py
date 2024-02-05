#burada gerekli kütüphaneler kullanılır
import cv2 as cv
import matplotlib.pyplot as plt 

#görselimizi okuruz
img = cv.imread('Resources/Photos/park.jpg')
cv.imshow('park',img)


#burada görselimizi Gray formatına çeviririz
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#burada görselimizi BGR formatından hsv formatına geçiririz
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

#burada görselimizi bgr formatından lab formatına geçiririz
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('Lab',lab)

#burada görselimizi bgr formatından rgb formatına geçiririz
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('Rgb',rgb)

#burada ise lab formatından bgr formatına geçiririz
LAB_bgr = cv.cvtColor(hsv, cv.COLOR_LAB2BGR)
cv.imshow('LAB----->BGR',LAB_bgr)

# genel olarak formatlar arası geçiş yapmak için cv.COLOR_ den sonra önce ilk formatımız, 2 'den sonra ise geçmek istediğimiz formatı koyarız

#matplotlib kütüphanesi resimi RGB formatında getiriri yani bu format 
#normal insan gördüğü formatın tam ters resim şeklidir
# biz görselimizin renklerini ters çevirip plota verir isek tam tersi bir görüntü alırız
plt.imshow(rgb)
plt.show()

cv.waitKey(0)



