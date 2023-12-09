nums=[]
cikis=0
while(True):
    target=int(input("Lutfen 110 ile -110 arasında hedef sayiyi giriniz: "))
    print("******************************************************")
    if(target<-110 or target>110):
        print("Lutfen geçerli arada bir değer girin.")
        print("*************************************")
        continue
    else:
        break

while(True):
    ekle=int(input("Lutfen diziye eklemek için -110 ile 110 arasında bir sayı giriniz\n(eğer daha fazla eleman girmek istemiyorsanız\nverilen aralığın dışında bir değer giriniz)"))
    print("***************************************************")
    if (ekle>110 or ekle<-110):
        if (len(nums)<2):
            print("Lutfen en az iki tane geçerli değer giriniz")
            print("*******************************************")
            continue
        break
    nums.append(ekle)
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if ((nums[i]+nums[j])==target):
            firstIndis=i
            secondIndis=j
            cikis=1
            break
    if cikis==1:
        break

print("[",i,",",j,"]")
    
    
        
