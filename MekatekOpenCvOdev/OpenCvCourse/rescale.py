import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')
#buraya kadar olan satırlar önceki py dosyamızda öğrendik

#bu fonksiyon aldığı parametreler ile adığı frame değişkenini kullanarak 
#frame i scale çarpanı kadar küçülterek , boyutu küçülttüğü görseli geri döndürür
def rescaleFrame(frame, scale=0.75):
	width = int(frame.shape[1] * scale) # burada küçültülmüş görselin boyunu alır
	height = int(frame.shape[0] * scale)# burada da uzunluğunu
	dimensions= (width,height) # ardından bu değerleri tuple türünde bir değişkene atar

	return cv.resize(frame,dimensions, interpolation= cv.INTER_AREA) 
	#burada yeniden boyutlandırma fonksiyonundan yararlanırız.
	#ilk olarak yeniden boyutlandıracağımız görseli ardından yeni boyutları içeren tuple' yi göndeririz
	#en sonunda yeniden boyutlandırmada kullanıcağımız metodu belirtiriz ve bunu fonksiyonda return ederiz


#bu fonksiyonda capture değişkenindeki videoyu istenilen boyutlara getirir fakat yalnızca canlı videolarda uygulanabilir
def changeRes(width.height): #fonksiyonun tanımı
	capture.set(3,width)# fonksiyonun boyunu atıyoruz
	capture.set(4,height)# fonksiyonun yüksekliğini atıyoruz(ilk parametre yüksekliğini atıcaz anlamına gelen değerdir)


resized_image = rescaleFrame(img,scale=0.2) #burada yazdığımız fonksiyonu kullanıyoruz ve bir değişkene yeni frame i atıyoruz
cv.imshow('Image', resized_image) #burada onu show yapıyoruz



capture = cv.VideoCapture('Resources/Videos/dog.mp4') # bu satır bizim dosya yolundan çektiğimiz resimi bir değişkene atamamızı sağlar

while True: # bu kod sonsuz bir döngü oluşturur
	isTrue, frame = capture.read() # capture.read() bir dizi döndürür ilk elemanı videonun karesi olup olmadığı ikinci değer videodaki tüm kareleri sırayla atar
	
	frame_resized= rescaleFrame(frame,scale=0.2)# burada da yeni size'ı belirlenmiş olan frame'i bir değişkene atıyoruz

	cv.imshow('Video', frame) # bu fonksiyon frame'e atanan kareleri sırayla gösterir
	cv.imshow('Video Resized', frame_resized) # burada yeni boyutları ayarlanmış olan frame'i burada show yapıyoruz

	if cv.waitKey(20) & 0xFF==ord('d'):#burada her kare döndüğünde 20 milisaniye bekleme fonksiyonunu ve ord fonksiyonunu çalıştırır 
		#waitkey 20 milisaniye bekledikten sonra true döndürür ve eğer d tuşu basıldıysa ord bir hexadecimal değer döndürür eğer dödürmemiş ise o zaman False döner ve döngü devam eder
		break




capture.release() #bu kod capture değişkenin içine atadığımız videoyu bellekte serbest bırakır
cv.waitKey(0) # bu kod pencere kapanmadan önce 1 saniye bekler

