from matplotlib import pyplot as plt # bu bölüm matplotlib kütüphanesini içeri almamızı sağlar

plt.xkcd() # bu kod grafiğimizin çizgi roman gibi gözükmesini sağlıyor

print(plt.style.available) #bu kod grafiğimizin alabileceği tiplerin kodlarını veriyor
plt.style.use('ggplot') #burda grafiğimize bir tarz belirttiık
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #burada bir liste değişkeninin içine grafik için x kordinatlarını verdik

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752] # burada ilk çizgimiz için y kordinatlarını verdik

plt.plot(ages_x, #burada grafiğimizin x kordinatları için değişkenimizi verdik
         dev_y,color='#444444', #burada grafiğimizin y kordinatları için değişkenimizi verdik
         linestyle='--', #burada grafik sonucu çıkan çizgimizin tarzını belirledik
         linewidth=3,# burada o çizginin kalınlığını belirledik
         marker='.',# burada kordinatların kesiştiği noktaların tarzını belirledik
         label='All Devs' # burada çizgimizin adını belirledik
         )

py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640] #burada diğer çizgimiz için y kordinatları bulunuyor

plt.plot(ages_x,
         py_dev_y,
         color='#5a7d9a',#burada diğer çizgimizden farklı olarak heksadesimal ile bir renk ekledik
         marker='o',
         linewidth=3,
         label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437,
            56373, 62375, 66674, 68745, 68746, 74583] # burada üçüncü çizgimizin y kordinatlarını bir değişkene atadık
plt.plot(ages_x,
         js_dev_y,
         color='#adad3b',
         marker='o',
         label='JavaScript')



plt.xlabel('Ages') #burada x kordinatlarını ismini belirttik
plt.ylabel('Medain Salary (USD)')# burada y kordinatlarının ismini belirttik
plt.title('Median Salary (USD) by Age')# burada direk grafiğimizin ismini belirttik


plt.legend() #burada çizgilerimizin adının varolmasını sağladık

plt.grid(True) #burada arka planı ızgara yaptık

plt.tight_layout() #bu kod çizimi optimize eder

plt.savefig('plot.jpeg') #bu kod çizelgemizi jpeg olarak kaydeder
plt.show()#bu kod çizelgemizi çıktı olarak çıkarır























