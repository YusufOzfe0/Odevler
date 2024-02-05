#önce gerekli kütüphanelerimizi import ederiz
import cv2 as cv
import numpy as np

#ardından görüntümüzü bir değişkene atarız
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)


# ardından boş bir siyah görüntü oluştururuz
blank = np.zeros ( img.shape, dtype='uint8')
cv.imshow('blank',blank)

#bu baştaki görüntümüzü gri yapmamızı sağlar
gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


#ardından bu fonksiyon ile gri görüntümüzü bulanıklaştırırız
#bulanıklaştırınca karşımıza gelecek olan kenarlar daha net çıktığı için bulanıklaştırırız
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

#canny yöntemi ile üst alt pixel yoğunluğu ile kenar tespit edilir
canny = cv.Canny(blur, 125,175)
cv.imshow('Canny Edges', canny)

#burada threshhold fonksiyonu yöntemiile kenar tespit etme gerçekleştirilir
ret , thresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)

#burada tespit edilen kenarlar bulunur ve sayılır
#findCOntours fonksiyonuna verilen iki parametre ile de köşe/kenar bulma yöntemleri belirlenir
contours , hierarchies = cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#bulunan kenar sayısı çıktı olarak yazdırılır
print(f'{len(contours)} contours(s) found!')

#burada bulunan kenarlar boş bir siyah görselin üzerine kırmızı bir şekilde yazılır
cv.drawContours(blank, contours, -1, (0,0,255),1)
#ve diğerlerinde olduğu gibi bu görselde çıkarılır bu fonksiyon ile
cv.imshow('Countours Drawn',blank)
cv.waitKey(0)