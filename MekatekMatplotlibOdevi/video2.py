import numpy as np # burada numpy kütüphanesini ekleriz
from matplotlib import pyplot as plt# burada pyplot modülünü ekleriz

plt.style.use("fivethirtyeight") # burada plotumuzun sitilini belirleriz

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #bu bizim x ekseni bilgileri
width = 0.25 #bu değişken sayesinde sütunlar arası mesafeyi arttırıp sütunları görünüz hale getiriyoruz
x_indexes = np.arange(len(ages_x)) #burada ages_x listesinin uzunluğuna kadar 0 dan bir liste oluşturuyoruz


dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752] #burası y ekseni bilgileri
plt.bar(x_indexes - width, #burada x ekseni bilgileri veriliyor{width ile sütunu öne alırız}
        dev_y,# burada ye ekseni listesi verilir
        color="#444444", # burada sütunumuzun rengini veririz
        label="All Devs",# burada sütun türü ismini atarız
        width=0.3) # burada sütunun kalınlığını belirleriz

#burası diğer sütunların bilgileri
py_dev_y = [45372, 48876, 53850, 57287, 63016,
               65998, 70003, 70000, 71496, 75370, 83640] 

plt.bar(x_indexes, py_dev_y, color="#008fd5", label="Python",width=0.3)

js_dev_y = [37810, 43515, 46823, 49293, 53437,
             56373, 62375, 66674, 68745, 68746, 74583]
plt.bar(x_indexes + width, js_dev_y, color="#e5ae38", label="JavaScript",width=0.3)

#burada sütunları türünün olduğu sekme açılır
plt.legend()

#burada x eksenini x_indexes e göre gruplarız sonra isim olarak ages_x değerlerini atarız
plt.xticks(ticks=x_indexes,labels=ages_x)

#burada plotumuzun başlığı ve x ve y ekseni isimlerini belirleriz
plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")

#bu kod grafiği optimize eder
plt.tight_layout()
#bu kod grafiği gösterir
plt.show()

