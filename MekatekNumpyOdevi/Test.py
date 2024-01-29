import numpy as np

a = np.array([[1,2],[3,4]])
eigenvalues,eigenvectors = np.linalg.eig(a)

print(eigenvalues) # özdeğer ve 

print(eigenvectors) # özvektör hesaplar

b = eigenvectors [:,0] * eigenvalues[0]
print(b)

c = a @ eigenvectors [:,0] # özvektörle matris çarpımı özvektörle özdeğer çarpımına eşittir

print(b)

print(b==c) # bazen doğru bazen yanlış sonucunu alırız


print(np.allclose(b,c))# bu ifade de aradaki toleransı kaldırır ve istisna kadeyi bozmaz mantığı ile True çevirir



