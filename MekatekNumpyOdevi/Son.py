import numpy as np

A = np.array([[1,1],[1.5,4.0]])
b= np.array([2200,5050])

x= np.linalg.inv(A).dot(b)
print(x)

#burada matrisin tersini eşitliğin karşı tarafına göndererek sonuca ulaştırk



x= np.linalg.solve(A,b)
print(x)

#bu da direkt basit bir fonksiyon kullanarak basitleştirme yöntemi



# np.loadtxt ile txt yüklenir
# np.genfromtxt da txt yükler ama dah esnek bir araçtır