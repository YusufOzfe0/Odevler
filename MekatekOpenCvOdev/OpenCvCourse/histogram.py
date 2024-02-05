#burada gerekli olan kütüphanelerimizi import ederiz
import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np  

#burada resimimizi okuruz
img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Cats',img)

#burada boş bir görsel oluştururuz
blank = np.zeros(img.shape[:2], dtype='uint8')

#burada resimimizi gri hale getirebiliriz
#gray= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray',gray)

#burada resimde kapatmak istediğimiz yer için bir kapatma bölgesi ayarlarız
mask= cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

#burada bu kapatma bölgesiyle resmimizi sadece kalan daire olarak bırakırız
masked= cv.bitwise_and(img,img,mask=mask)
cv.imshow('mask',masked)

#burada elimizdeki gri kapanmış bölgenin içindeki grinin tonlarının kaç tane olduğunu alırız
#gray_hist = cv.calcHist([gray],[0],mask,[256], [0,256])
#elimizdeki parametreleri görselin değerine göre ayarlarız mesela gride içi [0] değeri kullanılır
#aralık 256 dır 

#burada basit bir plot , grafik oluştururuz
#plt.figure()
#plt.title('Grayscale Histogram')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256]) #burada x ekseninin limiti 256 olarak ayarlarız
#plt.show()


plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors= ('b','g','r')


#burada enumerate ile bir listedeki elmanın indexsini ve kendini ayrı ayrı verir
for i,col in enumerate(colors):
	hist = cv.calcHist([img],[i],mask, [256],[0,256])#burada her rengin indexi sırayla verilir ve rengin histogramı hesaplanır
	plt.plot(hist,color=col)#burada oluşturduğumuz histogramı grafiğe çeviririz ve enumerate ile harfleri sıra ile girip grafiğin rengini değiştiririz
	plt.xlim([0,256]) #burada da x ekseni limitini belirtiriz
#burada ise o grafiğimizi gösteririz
plt.show()


cv.waitKey(0)






