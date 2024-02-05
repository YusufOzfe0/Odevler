import cv2 as cv



img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Cat',img)

#bu fonksiyon resmimizi grinin katlarına çevirir
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#bu fonksiyon resimi bulanıklaştırır
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('glur',blur)

#bu fonksiyon kenar tespiti yapar
canny= cv.Canny(blur,125,175)
cv.imshow('Canny Edges', canny)

#görsellerin görüntülerini büyütür
dilated= cv.dilate(canny,(7,7),iterations=5)
cv.imshow('Dilated', dilated)

#burada erode fonksiyonu ile görseldeki çizgileri daha daraltmak için kullanılır
eroded= cv.erode(dilated,(3,3),iterations=3)
cv.imshow('Eroded', eroded)

#bu fonksiyon görselimizi yeniden boyutlandırır
resized = cv.resize(img,(500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',resized)

#resmin istediğim alanı kesmemizi sağlar
cropped = img[50:200,200:400]

#seçtiğimiz interpolasyon yöntemleri ile resimi farklı teknikler ile istediğimiz oynamaları yapabiliriz
#iteration sayısı ile uyguladığımız iterasyon sayısını değiştirebiliriz
cv.imshow('cropped',cropped)


cv.waitKey(0)
