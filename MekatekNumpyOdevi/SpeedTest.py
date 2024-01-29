import numpy as np

from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i]*B[i]
    return dot

def dot2():
    return np.dot(a,b)

start1 = timer()
for t in range(T):
    dot1()
end1 = timer()

t1= end1-start1

start = timer()

for t in range(T):
    dot2()
end= timer()
t2 = end-start

print('list calculation', t1) #Bu çıktı bize python listenin çalışma hızını verir
print('np.dot', t2) # Bu çıktı ise bize numpy liste işlem çalışma hızını verir
print('ratio',t1/t2) # Ortalama numpy 130-140 kat arası daha hızlıdır


