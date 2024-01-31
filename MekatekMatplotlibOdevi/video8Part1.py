#burada gerekli kütüphaneleri import ederiz
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

#burada plotumuzun sitilini berlirleriz
plt.style.use('seaborn')

#burada belirli zaman data setimizi bir liste haline getiririz
# dates = [
#     datetime(2019, 5, 24),
#     datetime(2019, 5, 25),
#     datetime(2019, 5, 26),
#     datetime(2019, 5, 27),
#     datetime(2019, 5, 28),
#     datetime(2019, 5, 29),
#     datetime(2019, 5, 30)
# ]
#burada ye ekseni için bir veri listesi hazırlarız
# y = [0, 1, 3, 4, 6, 5, 7]
#burada plot_date tipinde grafiğimizi oluştururuz ardından x ve y ekseni için gerekli listeleri içine aktarırız
# plt.plot_date(dates,y,linestyle='solid')

#bu satır ile tarihleri çapraz bir şekilde x eksenine yazılmasını sağlarız
# plt.gcf().autofmt_xdate()

# bu satır ile bir tarih formatı belirleriz
# date_format = mpl_dates.DateFormatter('%b,%d %Y')

#bu satır ile de belirlediğimiz formatı x eksenindeki formata atarız
# plt.gca().xaxis.set_major_formatter(date_format)

#buradaki satır ile elimizdeki dataseti bir değişkene atarız
data = pd.read_csv('data3.csv')


#ardından buradaki satır ile de elimizdeki data setin 'Date' kısmını datetime formatına çevirerek tekrar data değişkenine geri atarız
data['Date']=pd.to_datetime(data['Date'])


data.sort_values('Date',inplace=True) # bu satır ise verileri Date 'e göre sıralar

#bu satırlar elimizdeki dataseti böler ve değişkenlere atar
price_date = data['Date']
price_close = data['Close']

#bu satır ile elimizdeki verileri kullanarak bir plot_date tipinde bir grafik oluştururuz
plt.plot_date(price_date,price_close,linestyle='solid')#solid ile noktaları birleştiririz

#bu satır ile x eksenindeki tarihleri çapraz bir şekilde yazarız
plt.gcf().autofmt_xdate()

#burada ise grafiğin kalan özellikleri verilip grafiği görünür hale getiririz
plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Closing Price')

plt.tight_layout()

plt.show()