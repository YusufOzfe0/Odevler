#burada gerekli kütüphaneleri import ederiz
import pandas as pd
from matplotlib import pyplot as plt
#burada plotumuzun stilini belirleriz
plt.style.use('seaborn')

#burada x ve ye kordinatları için bir takım datalar
# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
#burada renk ağırlık değerleri 1-10 arası ve noktaların büyüklüğü için değerler
# colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
# sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174,
#           538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]


#burada grafiğimizin sağ tarafına bir tane renk paleti ekleriz

# cbar = plt.colorbar()
#burada renk paletinin ismini veririz
# cbar.set_label('Satisfaction')

#burada her zmanaki gibi csv data setimizi parçalar ve değişkenlere atarız
data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']
#burada youtubeda bir kanalın bilgileri ile  grafiğimizi oluştururuz
plt.scatter(view_count,#burada x eskeni için bilgileri
            likes,# burada y ekseni için bilgiler gireriz
            c=ratio,#burada gelen like oranına göre renklerin koyuluğunu belirtiriz
            cmap='summer',#burada renklerin koyuluğunu hangi stilde olacağını belirleriz
            edgecolor='black',#burada yuvarlakların çevreisndeki çizgilerin rengi belirlenir
            linewidth=1,#burada o çizgilerin kalınlığı belirtilir
            alpha=0.7,#burada yuvarlakların içindeki renklere saydamlık ekleriz
            
            )
cbar = plt.colorbar()#bu kod ile renk barımızı oluştururuz
cbar.set_label('Like/Dislike Ratio')#burada renk barımıza bir isim atarız
plt.xscale('log')#burada x değerlerini logaritmik bir şekilde yayılımını sağlarız
plt.yscale('log')#burada y değerlerini logaritmik bir şekilde yayılmasın sağlarız

#burada geri kalan grafik ayarlarını yapar ve gösterime alırız
plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
