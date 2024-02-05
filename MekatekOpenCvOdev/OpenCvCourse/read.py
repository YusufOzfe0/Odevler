import cv2 as cv #bu satır bizim cv2 kütüphanemizi import etmeye yarar


#img = cv.imread('Resources/Photos/cat_large.jpg') # bu satır ise bizim bir görselimizi okuyup bir değişkene nesne olarak atamamızı sağlar

#cv.imshow('Cat', img) # bu satır görsel değişkenimizi Cat parametresi verilerek Cat adında bir pencerede gösterilmesini sağlar

capture = cv.VideoCapture('Resources/Videos/dog.mp4') # bu satır bizim dosya yolundan çektiğimiz resimi bir değişkene atamamızı sağlar

while True: # bu kod sonsuz bir döngü oluşturur
	isTrue, frame = capture.read() # capture.read() bir dizi döndürür ilk elemanı videonun karesi olup olmadığı ikinci değer videodaki tüm kareleri sırayla atar
	cv.imshow('Video', frame) # bu fonksiyon frame'e atanan kareleri sırayla gösterir

	if cv.waitKey(20) & 0xFF==ord('d'):#burada her kare döndüğünde 20 milisaniye bekleme fonksiyonunu ve ord fonksiyonunu çalıştırır 
		#waitkey 20 milisaniye bekledikten sonra true döndürür ve eğer d tuşu basıldıysa ord bir hexadecimal değer döndürür eğer dödürmemiş ise o zaman False döner ve döngü devam eder
		break




capture.release() #bu kod capture değişkenin içine atadığımız videoyu bellekte serbest bırakır
cv.waitKey(1000) # bu kod pencere kapanmadan önce 1 saniye bekler
