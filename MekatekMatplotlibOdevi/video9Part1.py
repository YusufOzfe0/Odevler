#burada gerekli kütüphaneleri ekleriz
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')#burada plotumuzun stilini veririz

#burada boş x ve ye için birer tane dizi tanımlarız
x_vals = []
y_vals = []

# plt.plot(x_vals, y_vals) #  bu kod bize normal bir plot oluşturur


index = count() #burada sonsuza kadar sayan bir sayaç üretiriz

#burada bir animasyon fonksiyonu tanımlarız
def animate(i):
    data = pd.read_csv('data.csv') # burada data.csv dosyasından verileri çekeriz
    x = data['x_value']#  buralarda o verileri parçalar ve değişkenlere aktarırırız
    y1 = data['total_1']
    y2 = data['total_2']
    
    plt.cla()# bu satır ile mevcut varolan tüm verileri siler böylece tekrar tekrar üstüne yazmaz
    

    # burada elimize gelen veriler ile grafikte veriler hakkında çizgiler çizeriz
    plt.plot(x,y1,label='Channel 1') 
    plt.plot(x,y2,label='Channel 2')
    
    plt.legend(loc='upper left') # burada çizgilerin ne anlama geldiğinden bahsetmek için çizgilerin adlarını verdiğimiz yerin konumunu belirleriz
    plt.tight_layout() # burada grafiğimizi optimize ederiz
    

#burada FuncAnimation nesnesini gerekli parametre ve fonksiyonları göndererek ani değişkenine atarız
ani = FuncAnimation(plt.gcf(), animate, interval=1000)

#burada da kalan grafik ayarlarını yapıp gösterime koyarız
plt.tight_layout()
plt.ion() 
plt.show()

#benim derleyicimde düzgün çalıştıramadım

