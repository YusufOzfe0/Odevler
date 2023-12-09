class TwoSum:
    def __init__(self):
        self.nums=[]

    def hedefAl(self):
        while(True):
            target=int(input("Lutfen 110 ile -110 arasında hedef sayiyi giriniz: "))
            print("******************************************************")
            if(target<-110 or target>110):
                print("Lutfen geçerli arada bir değer girin.")
                print("*************************************")
                continue
            else:
                break
        return target

    
    def sayilariAl(self):
        while(True):
            ekle=int(input("Lutfen diziye eklemek için -110 ile 110 arasında bir sayı giriniz\n(eğer daha fazla eleman girmek istemiyorsanız\nverilen aralığın dışında bir değer giriniz)"))
            print("***************************************************")
            if (ekle>110 or ekle<-110):
                if (len(self.nums)<2):
                    print("Lutfen en az iki tane geçerli değer giriniz")
                    print("*******************************************")
                    continue
                break
            self.nums.append(ekle)
        return self.nums
        
    def hesapla(self,nums,target):
        cikis=0
        for i in range(0,len(self.nums)):
            for j in range(i+1,len(self.nums)):
                if ((self.nums[i]+self.nums[j])==target):
                    firstIndis=i
                    secondIndis=j
                    return [i,j]
                break

yeniArama=TwoSum()
hedef=yeniArama.hedefAl()
sayiDizisi=yeniArama.sayilariAl()
sonuc=yeniArama.hesapla(sayiDizisi,hedef)
print(sonuc)








    
