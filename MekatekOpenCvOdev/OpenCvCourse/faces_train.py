#burada gerekli kütüphaneleri ekleriz
import os 
import cv2 as cv 
import numpy as np

#burada tespit edeceğimiz insanların olduğu bir liste yaparız
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']



DIR = r'/home/yusuf/Masaüstü/OpenCvCourse/Resources/Faces/train' #burada eğitimi vereceğimiz görsellerin olduğu dosya yolunu bir değişkene atadık

#burada opencv yüz eğitim dosyasını sınıflandırıcı olarak bir değişkene atadık
haar_cascade= cv.CascadeClassifier('haar_face.xml')

#burada daha sonra kullanmak üzere iki tane boş dizi oluşturuyoruz
features = []
labels= []

#bu fonksiyonun amacı verilen dosyadaki resimleri inceleyip her resimdeki yüzü gösteren değerleri
#birer diziye atmaktır
def create_train():
	for person in people: #bu döngüde ismin listesi içinde dolaşılır
		path= os.path.join(DIR, person) #bu satırda her isimin götürdüğü dosya bulunur
		label = people.index(person) #burada label dizisinin içine dolaştığımız isim atanır

		for img in os.listdir(path): # burada girilen dosyadaki her resim dolanılır
			img_path= os.path.join(path,img)# burada her resimin path'i oluşturulur

			img_array = cv.imread(img_path)# burada her resim okunarak bir değişkene atanır
			gray= cv.cvtColor(img_array,cv.COLOR_BGR2GRAY) # burada her resim griye çevirilir
			faces_rect= haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4) #burada her resimdeki yüz tanımlanır ve yüzlerdeki değerler bir değişkene atanır
			for(x,y,w,h) in faces_rect: # bu değerler önceden oluşturduğumuz feautures ve labels dizilerine eklenir
				faces_roi = gray[y:y+h,x:x+w]
				features.append(faces_roi)
				labels.append(label)





create_train() # önce tüm resimler hakkında bilgiler alınıp labels ve features dizilerine eklenir
print('Training done...............')

features= np.array(features ,dtype='object') #eklenen bilgiler bir numpy dizisine object türünde dönüştürülür
labels= np.array(labels) # aynı şekilde label'larda dönüştürülür
#print(f'Length of the features = {len(features)} ')
#print(f'Length of the labels = {len(labels)} ')

face_recognizer = cv.face.LBPHFaceRecognizer_create() #open cvnin kendi kütüphanelerindne yüz tanımak için yapılan bir eğitici değişken oluştururuz

face_recognizer.train(features,labels) #burada alınan bilgiler labellar ile eğitilir

face_recognizer.save('face_trained.yml') # ve eğitilen bilgiler face_trained.yml adlı bir belgeye kaydedilir
np.save('features.npy',features) # burada da features ve labelları birer numpy verisi olarak bir belgeye kaydeder
np.save('labels.npy',labels)