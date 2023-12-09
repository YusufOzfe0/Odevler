nums=[]
OutPut=[]
cikis=False
while(True):
    ekle= int(input("Lutfen listeye eklemek için 106 ile -106 arasında bir değer giriniz.\n(Çıkış yapmak için verilen aralığın dışında bir sayı giriniz)"))
    print("************************************")
    if (ekle<-160 or ekle>105) or len(nums)>=3000:
        if(len(nums)<3):
            print("Lutfen en az 3 değer girmeden çıkış yapmayınız")
            continue
        break
    nums.append(ekle)
for i in range(0,len(nums)):
    if i == len(nums)-2:
        break
    for j in range(i+1,len(nums)):
        if j == len(nums)-1:
            break
        for k in range(j+1,len(nums)):
            if(nums[i]+nums[j]+nums[k])==0:
                gecici=[nums[i],nums[j],nums[k]]
                gecici.sort()
                print(gecici)
                for nesne in OutPut:
                    if nesne==gecici:
                        cikis=True
                if cikis==False:
                    OutPut.append(gecici)
                gecici=[]
print(OutPut)
            
            
            
    
            
            


    
