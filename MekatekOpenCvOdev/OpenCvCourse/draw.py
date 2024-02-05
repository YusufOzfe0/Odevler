#gerekli kütüphaneleri import ederiz
import cv2 as cv
import numpy as np

blank= np.zeros((500,500,3), dtype='uint8')#burada üç boyutlu ve her elemanı int alan bir dizi oluştururuz
cv.imshow('Blank', blank)



#resimimizi değişkene atarız
img = cv.imread('Resources/Photos/cat.jpg')
cv.imshow('Cat',img) #ardından resimi çalıştırırız

#burada ayarladığımız boş dizinin içine seçtiğimiz alanın içine renk atarız
blank[200:300, 300:400] = 0,0,255
#burada o blank resmini show yaparız
cv.imshow('Green',blank)

#burada blank üzerinden seçtiğimiz iki nokta arasına bir diktörtgen oluştururuz 
#ilk parametre resimimizi alır, ikinci parametre oluşacak olan diktörgenin sol üst noktası
#üçüncü parametre sağ alt nokta(şeklimizin tam ortası seçilmiştir), thickness ile diktörtgenin kenar uzunluğu veya içinin doldurulmasını seçeriz
cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(0,255,0), thickness=cv.FILLED) # burada cv.FILLED yerine -1 yazarsakta aynı şeyi yapar
cv.imshow('Rextangle',blank)#burada blank'ı yeni pencerede tekrar açarız


#burada parametreler vererek bir daire oluştururuz
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness=-1)
cv.imshow('circle',blank)

#burada parametreler vererek dikdörtgene benzer şekilde bir çizgi oluştururuz
cv.line(blank,(100,250),(300,400) , (255, 255, 255), thickness=2)
cv.imshow('line',blank) 

#burada ise görselimize bir yazı ekleme fonksiyonunu kullanırız.
cv.putText(blank, 'Hello my name is yusuf', (0,255), cv.FONT_HERSHEY_TRIPLEX, 1.0,( 0,255,0), thickness=3)
cv.imshow('Text',blank)
cv.waitKey(0)








