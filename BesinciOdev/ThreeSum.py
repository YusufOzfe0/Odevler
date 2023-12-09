class ThreeSum:
    def __init__(self):
        self.nums=[]
        self.OutPut=[]
        self.cikis=False
        
    def ListeEkleme(self):
        while(True):
            ekle= int(input("Lutfen listeye eklemek için 106 ile -106 arasında bir değer giriniz.\n(Çıkış yapmak için verilen aralığın dışında bir sayı giriniz)"))
            print("************************************")
            if (ekle<-160 or ekle>105) or len(self.nums)>=3000:
                if(len(self.nums)<3):
                    print("Lutfen en az 3 değer girmeden çıkış yapmayınız")
                    continue
                break
            self.nums.append(ekle)

    def Hesapla(self):
        for i in range(0,len(self.nums)):
            if i == len(self.nums)-2:
                break
            for j in range(i+1,len(self.nums)):
                if j == len(self.nums)-1:
                    break
                for k in range(j+1,len(self.nums)):
                    if(self.nums[i]+self.nums[j]+self.nums[k])==0:
                        gecici=[self.nums[i],self.nums[j],self.nums[k]]
                        gecici.sort()
                        for nesne in self.OutPut:
                            if nesne==gecici:
                                self.cikis=True
                        if self.cikis==False:
                            self.OutPut.append(gecici)
                        gecici=[]
        return self.OutPut

yeniArama=ThreeSum()
yeniArama.ListeEkleme()
sonuc=yeniArama.Hesapla()
print(sonuc)
