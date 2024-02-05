import os
import caer
import canaro
import numpy as np
import cv2 as cv
import gc
import matplotlib.pyplot as plt
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import LearningRateScheduler

IMG_SIZE = (80,80)
channels = 1#kanal görüntülerin kaç farklı renk kanalına sahip olduğunu verir
char_path = r'buraya_elimizdeki_datasetin_bilgisayardaki_yolu_yazılmalıdır_ama_githuba_yüklenmesi_zor_olduğundan_bilgilendirme_yazıyor_sadece'

#buraya karakterler için bir sözlük oluşturulur ve böylece her karakterin kaç adet resimi bulunduğu bir sözlükte tutabiliriz
char_dict = {}
for char in os.listdir(char_path): #dosya dolaşılarak her kişinin kaç adet tutulduğu sözlüğe kaydolmuştur
    char_dict[char] = len(os.listdir(os.path.join(char_path,char)))

# bu kod ile birlikte sözlük azalan sıraya göre sıralanır
char_dict = caer.sort_dict(char_dict, descending=True)


# karakterleri characters listesine sıralanmış bir şekilde ekler
#ve sadece ilk 10 karakteri alır
characters = []
count = 0
for i in char_dict:
    characters.append(i[0])
    count += 1
    if count >= 10:
        break


#burada bilgiler verilip eğitim için bir veri seti geri alınır
train = caer.preprocess_from_dir(char_path, characters, channels=channels, IMG_SIZE=IMG_SIZE, isShuffle=True)


#burada örnek sayısını döndürür
len(train)


plt.figure(figsize=(30,30)) # oluşturulan grafiğin boyutunu belirtiyoruz
plt.imshow(train[0][0], cmap='gray') # burada eğitim modelin ilk örneğini gri bir şekilde show yapar
plt.show()



#bu fonksiyonu veri setini hazır hale getirmek için kullanıyoruz
featureSet, labels = caer.sep_train(train, IMG_SIZE=IMG_SIZE)

#bu fonksiyon veri setini normalizasyon yapar
featureSet = caer.normalize(featureSet)


# sınıf etiketlerini ikili sisteme çevirir
labels = to_categorical(labels, len(characters))


# veri setini kullanmak üzere alt kümelere bçler
x_train, x_val, y_train, y_val = caer.train_test_split(featureSet, labels, val_ratio=.2)


# ileride lazım olacak değişkenler
BATCH_SIZE = 32
EPOCHS = 10

# burada resim datası oluşturma nesnesi oluştururuz
datagen = canaro.generators.imageDataGenerator()
#burada elimizdeki datayı akışa çeviririz
train_gen = datagen.flow(x_train, y_train, batch_size=BATCH_SIZE)

# burada özel bir öğrenme modeli oluştuyourz 
# burada ince ayar yapmak için parametreleri kullanırız
# ama genelde default olurlar
model = canaro.models.createSimpsonsModel(IMG_SIZE=IMG_SIZE, channels=channels, output_dim=len(characters), 
                                         loss='binary_crossentropy', decay=1e-7, learning_rate=0.001, momentum=0.9,
                                         nesterov=True)



# LearningRateScheduler fonksiyonu öğrenme oranını geri gönderir
# model.fit ise bu geri çağrıları alır,  eğitim sırasında dinamik olara eğitimin ayarlanmasını sağlar
callbacks_list = [LearningRateScheduler(canaro.lr_schedule)]
training = model.fit(train_gen,
                    steps_per_epoch=len(x_train)//BATCH_SIZE,
                    epochs=EPOCHS,
                    validation_data=(x_val,y_val),
                    validation_steps=len(y_val)//BATCH_SIZE,
                    callbacks = callbacks_list)




#test aşaması

test_path = r'test etmek istediğimiz görsel'

#görseli okuruz
img = cv.imread(test_path)

#görseli plotta gösteririz
plt.imshow(img)
plt.show()

#bu fonksiyonda resimi griye çeviririz
#ardından tekrar boyutlandırırız
#resimi caer.reshape ile yeniden şekillendiririz ve resimi geri göndeririz
def prepare(image):
    image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image = cv.resize(image, IMG_SIZE)
    image = caer.reshape(image, IMG_SIZE, 1)
    return image


predictions = model.predict(prepare(img)) # verilen resim hakkında tahminleri alan fonksiyondur

# gönderdiğimiz karakterin en çok kim olabileceğini veren çıktıdır
print(characters[np.argmax(predictions[0])])