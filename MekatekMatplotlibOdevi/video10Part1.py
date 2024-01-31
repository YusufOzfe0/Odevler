#burada gerekli kütüphaneleri ekleriz
import pandas as pd
from matplotlib import pyplot as plt


#bu kod plotumuzun sitilini belirtir
plt.style.use('seaborn')


#bu kısım elimizdeki dataseti data değişkenine atar ve bölüp diğer değişkenlere atar
data = pd.read_csv('data4.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

#burada tek bir pencere üzerine 2 tane alt grafik eklemek için bir satır vardır
# fig , (ax1,ax2) = plt.subplots(nrows=2, #bu komut oluşacak penceredeki grafiklerin satır ve sütun sayılarını verir
#                                ncols=1,
#                                sharex=True)# bu komut ile üst üste binen grafiklerin ortak özellikleri birleştirilip tek bir yere yazılır

# bu komutlar ile iki tane farklı pencere oluşturup her pencereye birer tane grafik ekleriz
fig1 , ax1=plt.subplots()
fig2 , ax2=plt.subplots()

#bu ikinci ve birinci girafiklerimizin plot ayarlarıdır
#ayarlamak istediğimiz grafiği seçerek plot fonksiyonunu çalıştırırız
ax2.plot(ages, py_salaries, label='Python')
ax2.plot(ages, js_salaries, label='JavaScript')

ax1.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

ax1.legend()
ax1.set_title('Median Salary (USD) by Age')

ax1.set_ylabel('Median Salary (USD)')

ax2.legend()

ax2.set_xlabel('Ages')
ax2.set_ylabel('Median Salary (USD)')

#burada tüm plotlarımıza padding ayarı ve gösterilmesi sağlanır
plt.tight_layout()

plt.show()

#burada ise ekrana gelen grafikler arka tarafa png olarak kaydolur
fig1.savefig('resim1.png')

fig2.savefig('resim2.png')

