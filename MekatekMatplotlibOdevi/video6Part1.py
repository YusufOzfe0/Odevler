#burada gerekli kütüphanelerimizi import ederiz
import pandas as pd 
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight') # burada plotumuzun sitilini belirtiriz

#burada csv data setimizi parçalar ve değişkenlere atarız
data = pd.read_csv('data2.csv')
ids = data['Responder_id']
ages = data['Age']



bins=[10,20,30,40,50,60,70,80,90,100] #burada histogramımızın x ekseninin kaç parça olacağı ve bunların ne olacağına karar veririz


plt.hist(ages,#burada data setimizden aldığımız verileri aktarırız
         bins=bins,#burada x eksenini bölmek istediğimiz değerleri aktarırız
         edgecolor='black', #burada sütunların kenar renklerini belirtiriz
         log=True # burada verileri logaritmik bir dizilişe sağlanmasını sağlarız
         )


#burada grafiğimizin içinde bir çizgi oluşturmayı sağlarız
median_age = 29
color = '#fc4f30'
plt.axvline(median_age,color=color,label='Age Median',linewidth=2)


#burada grafiğimizin geri kalan özelliklerini veririrz
plt.legend()

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()

plt.show()