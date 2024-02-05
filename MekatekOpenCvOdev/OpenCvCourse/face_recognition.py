#önce gerekli olan kütüphaneler eklenir
import numpy as np 
import cv2 as cv

#burada opencv dataseti ile bir sınıflandırıcı oluşturuyoruz
haar_cascade = cv.CascadeClassifier('haar_face.xml')

#burada eğitime katılan resimlerin sahipleri vardır
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

#burada daha önceden çıkardığımız npy dosyaları birer değişkenlere atanır
features = np.load('features.npy',allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

#burada eğiticimizi oluştururu ve elimizdeki eğitim verisiyle eğitiriz
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

#burada istediğimiz görseli seçer ve bir değişkene atarız
img = cv.imread('/home/yusuf/Masaüstü/OpenCvCourse/Resources/Faces/val/ben_afflek/1.jpg')

#burada bu görseli griye çeviririz
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Person', gray)

#burada elimizdeki yüzü seçen fonksiyonu çalıştırırız ve verileri bir değişkene atarız
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

#burada gelen verilerle elimizdeki resimdeki yüzü kare içine alırız
for (x, y, w, h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w]
    #burada eğitilen modelimize predict fonksiyonu ile kim olduğunu ve ne kadar ihtimalle olduğunu tahmin eden kodu yazarız
    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label={people[label]} with confidence of {confidence}')
    #burada kim olduğunu mevcut resimimize ekleriz
    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    #ve resime bir elimizdeki veriler ile bir diktörtgen çizeriz
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

#son olarak bu görseli çıktı olarak gösteririz
cv.imshow('Detected Face', img)

cv.waitKey(0)