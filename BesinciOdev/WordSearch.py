#board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
#words=["oath","pea","eat","rain"]
words=[]
board=[]
kelimeSayisi=0
satirSayisi=0
sutunSayisi=0
while(True):
    satirSayisi=int(input("Lutfen tabloya 1'den 12'ye kadar bir satır sayısı giriniz: "))
    sutunSayisi=int(input("Lutfen tabloya 1'den 12'ye kadar bir sütun sayısı giriniz: "))
    kelimeSayisi=int(input("Kaç kelime arayacaksiniz(En fazla 104 en az 1))"))
    if(sutunSayisi>=1 and sutunSayisi<=12 and satirSayisi<=12 and satirSayisi>=1 and kelimeSayisi>=1 and kelimeSayisi<=104):
        break
    else:
        print("Hatalı giris")
while(True):
    satir=[]
    while(True):
        satir.append(input("Lutfen " + str(len(board)+1) + ". satırın "+ str(len(satir)+1)+". elemanını giriniz: "))
        print("**********************************")
        print("              Eklendi             ")
        print("**********************************")
        if(len(satir)==sutunSayisi):
            board.append(satir)
            break
    if(len(board)==satirSayisi):
        break

while(True):
    words.append(input("Lutfen aranacak bir kelime giriniz(En fazla 10 harf olabilir): "))
    print("*************Eklendi****************")
    if(len(words)==kelimeSayisi):
        break
    


test=[]
kelime=[]
Output=[]
def icerikTesti(i,j,oge):
    for icerik in oge:
        if (icerik==[i,j]):
            
            return True
    return False

def esitlikTesti(kelime,harf):
    dolasim=[]
    for t in harf:
        dolasim.append(t)
    if(dolasim==kelime):
        return True
    else:
        return False

def varlikTesti(i,j):
    if(i>=0 and (i<(len(board)-1)) and j>=0 and (j<(len(board[i])-1))):
        return True
    return False
    
    
    
def coklukTesti(i,j,test,kelime,harf):
    kenarlar=[]
    if(varlikTesti(i+1,j)) and ((harf[len(kelime)])==(board[i+1][j])):
        kenarlar.append([i+1,j])
    if(varlikTesti(i-1,j)) and ((harf[len(kelime)])==(board[i-1][j])):
        kenarlar.append([i-1,j])        
    if(varlikTesti(i,j+1)) and ((harf[len(kelime)])==(board[i][j+1])):
        kenarlar.append([i,j+1])
    if(varlikTesti(i,j-1)) and ((harf[len(kelime)])==(board[i][j-1])):
        kenarlar.append([i,j-1])
    if(len(kenarlar)>1):
        for m in kenarlar:
            if(kontrol(m[0],m[1],test,kelime,harf)):
                return True
        
    return False
        
            
        
def altKontrol(i,j,test,kelime,harf):
    if(i==(len(board)-1)):
        return False
    elif(icerikTesti(i+1,j,test)):
        return False
    if(harf[len(kelime)]==board[i+1][j]):
        test.append([i+1,j])
        kelime.append(harf[len(kelime)])
        if(esitlikTesti(kelime,harf)):
            return True
        return kontrol(i+1,j,test,kelime,harf)
        
    else:
        return False
    
def ustKontrol(i,j,test,kelime,harf):
    if (i==0):
        return False
    elif(icerikTesti(i-1,j,test)):
        return False
    if(harf[len(kelime)]==board[i-1][j]):
        test.append([i-1,j])
        kelime.append(harf[len(kelime)])
        if(esitlikTesti(kelime,harf)):
            return True
        return kontrol(i-1,j,test,kelime,harf)
        
    else:
        return False
    
def sagKontrol(i,j,test,kelime,harf):
    if (j==(len(board[i])-1)):
        return False
    elif(icerikTesti(i,j+1,test)):
        return False
    if(harf[len(kelime)]==board[i][j+1]):
        test.append([i,j+1])
        kelime.append(harf[len(kelime)])
        if(esitlikTesti(kelime,harf)):
            return True
        return kontrol(i,j+1,test,kelime,harf)
        
    else:
        return False
    
def solKontrol(i,j,test,kelime,harf):
    if (j==0):
        return False
    elif(icerikTesti(i,j-1,test)):
        return False
    if(harf[len(kelime)]==board[i][j-1]):
        test.append([i,j-1])
        kelime.append(harf[len(kelime)])
        if(esitlikTesti(kelime,harf)):
            return True
        return kontrol(i,j-1,test,kelime,harf)
        
    else:
        return False

def kontrol(i,j,test,kelime,harf):
    if(coklukTesti(i,j,test,kelime,harf)):
        return True
        
    if(ustKontrol(i,j,test,kelime,harf)):
        return True
    if(altKontrol(i,j,test,kelime,harf)):
        return True
    if(sagKontrol(i,j,test,kelime,harf)):
        return True
    if(solKontrol(i,j,test,kelime,harf)):
        return True
    return False

for i in range(0,len(board)):
    for j in range(0,len(board[i])):
        for harf in words:
            if harf[0]==board[i][j]:
                kelime=[]
                test=[]
                test.append([i,j])
                kelime.append(harf[0])
                if(kontrol(i,j,test,kelime,harf)):
                    Output.append(harf)
                    
                    
                
print("Output= ",Output)
                    





