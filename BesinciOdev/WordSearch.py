class WordSearch:
    def __init__(self):
        self.words=[]
        self.board=[]
        self.kelimeSayisi=0
        self.satirSayisi=0
        self.sutunSayisi=0
        self.test=[]
        self.kelime=[]
        self.Output=[]

    def TabloOlustur(self):
        while(True):
            self.satirSayisi=int(input("Lutfen tabloya 1'den 12'ye kadar bir satır sayısı giriniz: "))
            self.sutunSayisi=int(input("Lutfen tabloya 1'den 12'ye kadar bir sütun sayısı giriniz: "))
            self.kelimeSayisi=int(input("Kaç kelime arayacaksiniz(En fazla 104 en az 1))"))
            if(self.sutunSayisi>=1 and self.sutunSayisi<=12 and self.satirSayisi<=12 and self.satirSayisi>=1 and self.kelimeSayisi>=1 and self.kelimeSayisi<=104):
                break
            else:
                print("Hatalı giris")
        while(True):
            satir=[]
            while(True):
                satir.append(input("Lutfen " + str(len(self.board)+1) + ". satırın "+ str(len(satir)+1)+". elemanını giriniz: "))
                print("**********************************")
                print("              Eklendi             ")
                print("**********************************")
                if(len(satir)==self.sutunSayisi):
                    self.board.append(satir)
                    break
            if(len(self.board)==self.satirSayisi):
                break

        while(True):
            self.words.append(input("Lutfen aranacak bir kelime giriniz(En fazla 10 harf olabilir): "))
            print("*************Eklendi****************")
            if(len(self.words)==self.kelimeSayisi):
                break
    def icerikTesti(self,i,j,oge):
        for icerik in oge:
            if (icerik==[i,j]):
                
                return True
        return False

    def esitlikTesti(self,kelime,harf):
        dolasim=[]
        for t in harf:
            dolasim.append(t)
        if(dolasim==kelime):
            return True
        else:
            return False

    def varlikTesti(self,i,j):
        if(i>=0 and (i<(len(self.board)-1)) and j>=0 and (j<(len(self.board[i])-1))):
            return True
        return False
        
        
        
    def coklukTesti(self,i,j,test,kelime,harf):
        kenarlar=[]
        self.test=test
        self.kelime=kelime
        if(self.varlikTesti(i+1,j)) and ((harf[len(self.kelime)])==(self.board[i+1][j])):
            kenarlar.append([i+1,j]) 
        if(self.varlikTesti(i-1,j)) and ((harf[len(self.kelime)])==(self.board[i-1][j])):
            kenarlar.append([i-1,j])    
        if(self.varlikTesti(i,j+1)) and ((harf[len(self.kelime)])==(self.board[i][j+1])):
            kenarlar.append([i,j+1]) 
        if(self.varlikTesti(i,j-1)) and ((harf[len(self.kelime)])==(self.board[i][j-1])):
            kenarlar.append([i,j-1])
        if(len(kenarlar)>1):
            self.kelime.append((harf[len(self.kelime)]))
            for m in kenarlar:
                if(self.kontrol(m[0],m[1],self.test,self.kelime,harf)):
                    return True
        return False
            
                
            
    def altKontrol(self,i,j,test,kelime,harf):
        self.test=test
        self.kelime=kelime
        if(i==(len(self.board)-1)):
            return False
        elif(self.icerikTesti(i+1,j,self.test)):
            return False
        if(harf[len(self.kelime)]==self.board[i+1][j]):
            self.test.append([i+1,j])
            kelime.append(harf[len(self.kelime)])
            if(self.esitlikTesti(self.kelime,harf)):
                return True
            return self.kontrol(i+1,j,self.test,self.kelime,harf)
            
        else:
            return False
        
    def ustKontrol(self,i,j,test,kelime,harf):
        self.kelime=kelime
        self.test=test
        if (i==0):
            return False
        elif(self.icerikTesti(i-1,j,self.test)):
            return False
        if(harf[len(self.kelime)]==self.board[i-1][j]):
            self.test.append([i-1,j])
            kelime.append(harf[len(self.kelime)])
            if(self.esitlikTesti(self.kelime,harf)):
                return True
            return self.kontrol(i-1,j,self.test,self.kelime,harf)
            
        else:
            return False
        
    def sagKontrol(self,i,j,test,kelime,harf):
        self.kelime=kelime
        self.test=test
        if (j==(len(self.board[i])-1)):
            return False
        elif(self.icerikTesti(i,j+1,self.test)):
            return False
        if(harf[len(self.kelime)]==self.board[i][j+1]):
            self.test.append([i,j+1])
            kelime.append(harf[len(self.kelime)])
            if(self.esitlikTesti(self.kelime,harf)):
                return True
            return self.kontrol(i,j+1,self.test,self.kelime,harf)
            
        else:
            return False
        
    def solKontrol(self,i,j,test,kelime,harf):
        self.kelime=kelime
        self.test=test
        if (j==0):
            return False
        elif(self.icerikTesti(i,j-1,self.test)):
            return False
        if(harf[len(self.kelime)]==self.board[i][j-1]):
            self.test.append([i,j-1])
            kelime.append(harf[len(self.kelime)])
            if(self.esitlikTesti(self.kelime,harf)):
                return True
            return self.kontrol(i,j-1,self.test,self.kelime,harf)
            
        else:
            return False

    def kontrol(self,i,j,test,kelime,harf):
        self.kelime=kelime
        self.test=test
        if(self.coklukTesti(i,j,self.test,self.kelime,harf)):
            return True
            
        if(self.ustKontrol(i,j,self.test,self.kelime,harf)):
            return True
        if(self.altKontrol(i,j,self.test,self.kelime,harf)):
            return True
        if(self.sagKontrol(i,j,self.test,self.kelime,harf)):
            return True
        if(self.solKontrol(i,j,self.test,self.kelime,harf)):
            return True
        return False

    def hesapla(self):
        for i in range(0,len(self.board)):
            for j in range(0,len(self.board[i])):
                for harf in self.words:
                    if harf[0]==self.board[i][j]:
                        self.kelime=[]
                        self.test=[]
                        self.test.append([i,j])
                        self.kelime.append(harf[0])
                        if(self.kontrol(i,j,self.test,self.kelime,harf)):
                            self.Output.append(harf)
        return self.Output

yeniArama=WordSearch()
yeniArama.TabloOlustur()
sonuc=yeniArama.hesapla()
print(sonuc)
