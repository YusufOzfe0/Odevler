from matplotlib import pyplot as plt#burada pyplotu import ederiz

plt.style.use("fivethirtyeight")# bu satırda plot sitilini belirleriz


minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9] # burası yığın grafiği için x eksenini verir

player1 = [8, 6, 5, 5, 4, 2, 1, 1, 0] # bu player1 in değişiklik miktarını çıkartabilceğimiz liste ve diğer playerlerinki verilmiş
player2 = [0, 1, 2, 2, 2, 4, 4, 4, 4]
player3 = [0, 1, 1, 1, 2, 2, 3, 3, 4]

labels= ['player1','player2','player3'] # burada renklerin hangi isime sahip olduğu gösterilmiştir
colors=['#008fd5','#fc4f30','#6d904f'] # burada playerlerin renklerini vermiştir
plt.stackplot(minutes, #burada grafiğin c eksenini verriz 
              player1, # burada grafiğin player değerlerini veririz
              player2,
              player3,
              labels=labels,#renkler ver isimleri verilir
              colors=colors
              )

plt.legend(loc=(0.07,0.05))# burada renklerin isimlerinin olduğu tablayu grafiğin neresinde olduğuna karar veririz

#burada da diğer plot özellikleri verilir
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f