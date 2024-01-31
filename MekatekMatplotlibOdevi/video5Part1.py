import pandas as pd# burada pandas kütüphanesini ve pyplot modülünü import ederiz
from matplotlib import pyplot as plt
#burada csv dosyamızı data set haline getirip data değişkenine atarız
data = pd.read_csv('data1.csv') 
#burada bu datasetteki bilgileri parçalayıp değişkenlere atarız
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

#burada plot grafiğiklerinin gerekli parametreleri atanır
plt.plot(ages, dev_salaries, color='#444444',
         linestyle='--', label='All Devs')

plt.plot(ages, py_salaries, label='Python')

#fill_between komutları ile istediğimiz aralıkları doldurabiliyoruz
plt.fill_between(ages, # doldurmak istediğimiz  x ekseni bilgilerini giriyoruz
                 py_salaries,#bu satırda y ekseni bilgilerini giriyoruz
                 dev_salaries,# bu satırda çizgiden başlayarak nereye kadar doldurulacağını seçiyoruz
                 alpha=0.25,#bu satırda doldurduğumuz alanı biraz şeffaflaştırıyoruz
                 where=(py_salaries > dev_salaries),#burada istediğimz alan dışında yerleri doldurmamasını istiyoruz
                 interpolate=True,# bu kod verilmeyen bilgileri de doldurmasını sağlar
                 label='Above Avg'# bu kod ise doldurulan alanlara isim atanmasını sağlar
                 )

plt.fill_between(ages,
                 py_salaries,
                 dev_salaries,
                 alpha=0.25,
                 where=(py_salaries <= dev_salaries),
                 interpolate=True,
                 color='red',
                 label='Below Avg'
                 )

#geri kalan kodları daha önceki uygulamalarda açıklamasını yazmıştım
plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()

plt.show()

