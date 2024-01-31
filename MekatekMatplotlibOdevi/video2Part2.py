import csv #burada csv uzantılı dosyaları okumak için csv kütüphanisin import ederiz
import numpy as np #burada numpy  kütüphanesini import ettik
import pandas as pd #burada ilerde kullanmak üzere pandas kütüphanesini import ederiz
from matplotlib import pyplot as plt #bu bizim ana konu kütüphanemiz
from collections import Counter # bu kütüpahne ile listedeki tüm elemanların kaç tane olduğnu bulabiliyoruz
plt.style.use("fivethirtyeight") #bu kod ile plotumuzun türünü belirleriz

# with open ('data.csv') as csv_file: #burada data.csv yi csv_file olarak açarız
#     csv_reader = csv.DictReader(csv_file) # bu kod csv dosyasını satır satır işler ve csv_reader dosyasına atar
    
#     language_counter = Counter() # bu kod bu değişkeni bir Counter nesnesine çevirir
    
#     for row in csv_reader:
#         language_counter.update(row['LanguagesWorkedWith'].split(';'))# bu for döngüsü ile csv_reader içindeki data seti bölerek parça parça Counter nesnesine sayıları saydırır


data =  pd.read_csv('data.csv') # bu kod ile data.csv data setini data adlı değişkene atarız



ids= data['Responder_id'] #bu satır ise datadaki Responder_id sütununu ids değişkeine atar
lang_responses= data['LanguagesWorkedWith'] # bu satır LanguagesWorkedWith bilgi kısmını lang_responses değişkenine atar

language_counter = Counter() # bu kod language_counter değişkenini bir Counter nesnesi yapar
    
for response in lang_responses:
    language_counter.update(response.split(';')) # burada LanguagesWorkedWith bilgilerini Counter ile sıra ile sayar

languages = []
popularity = []


for item in language_counter.most_common(15): # bu döngü ile en çok kullanılan dilleri languages dizisine ve kullanım sayısını popularity dizisine atar
    languages.append(item[0])
    popularity.append(item[1])

languages.reverse() # barh tipindeki grafiğimizde yüksel popüler olan üstten aşa sıralansın diye language ve popularity dizilerini ters çeviririz
popularity.reverse()

#burada barh grafiğimizn y ekseni ve x eksenini veririz
plt.barh(languages,popularity)
# burada y ve x ekseninin ismini atarız ve grafiğin ismini atarız
plt.title("Most Popular Languages")
plt.ylabel("Programming Languages")
plt.xlabel("Numper of People Who Use")
    #burada grafiğimizi optimize ederiz
plt.tight_layout()
    #burada grifiğimizi show yaparız 
plt.show()

