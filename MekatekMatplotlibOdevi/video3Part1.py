from matplotlib import pyplot as plt #burada matplotlib kütüphanesindeki pyplot sınıfını import  ederiz

plt.style.use("fivethirtyeight") #burada grafiğimize bir sitil atarız
#buradaki bilgiler pasta şeklindeki grafik içindir
#slices = [120,80,30,20] 

# label= ['Sixty',
#         'Forty',
#         'Extra1',
#         'Extra2']

# colors= ['#008fd5',
#          '#fc4f30',
#          '#e5ae37',
#          '#6d904f']

explode = [0, 0 , 0, 0.5 , 0 ,0,0,0,0,0,0,0,0,0,0]#bu kod ile her pasta diliminin ne pastadan ne kadar ayrılacağına dair bir liste hazırlarız
#buradakiler pasta dilimi için her dilimin ismi ve pastada ne kadar yer kaplıcağını belirlicek alanları
slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
labels = ['JavaScript',
          'HTML/CSS',
          'SQL',
          'Python',
          'Java',
          'Bash/Shell/PowerShell',
          'C#',
          'PHP',
          'C++',
          'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

plt.pie(
        slices,#burada slices değişkein ile pastanın dilimlerinin ne kadar büyüklüğü olacak onu atarız
        labels=labels,# bu kod ile de her dilimin ismini veririz
        shadow=True, # bu kod ile pasta grafiğine bir gölge atayabiliriz
        startangle=90, # bu kod ile pasta grafiğimiz istediğimiz derecede çevirebiliriz
        autopct='%1.1f%%', # bu kod ile dilimlerin yüzdelik işaretlerini atarız
        wedgeprops={'edgecolor':'black'}, #burada kenar rengini veririz
        explode=explode#burada ise daha önce belirlerdiğimiz explode listeni atayarak her pastanın ne kadar uzakta olduğunu ayarlarız
        )
#bunlar ise grafiğin isimi, optimizasyonu ve gösterilmesi için her zaman yazılan kodlar
plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f