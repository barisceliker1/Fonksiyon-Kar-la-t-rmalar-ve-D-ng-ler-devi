a=int(input("ilk 6 aylık yazılım gelirlerini giriniz"))
b=int(input("ilk 6 aylık Finansman gelirlerini giriniz"))
c=int(input("ilk 6 aylık Ürün satış gelirlerini giriniz"))
d=int(input("ilk 6 aylık Çalışan maaşları giderlerini giriniz"))
e=int(input("ilk 6 aylık Kira giderlerini giriniz"))
f=int(input("ilk 6 aylık Donanım maliyeti giriniz"))
j=int(input("son 6 aylık Yazılım gelirlerini giriniz"))
k=int(input("son 6 aylık Sponsorluk gelirlerini giriniz"))
l=int(input("son 6 aylık E Ticaret gelirlerini giriniz"))
m=int(input("son 6 aylık Ürün satış gelirlerini giriniz"))
n=int(input("son 6 aylık Çalışan maaşları giriniz"))
o=int(input("son 6 aylık Kira giderleri giriniz"))
p=int(input("son 6 aylık bakım maliyeti"))
def ilk6aykar(a,b,c,d,e,f):
    global ilk6aydakikar
    ilk6aydakikar=a+b+c-d-e-f
    return ilk6aydakikar
def son6aykar(j,k,l,m,n,o,p):
    global son6aydakikar
    son6aydakikar=j+k+l+m-n-o-p
    return son6aydakikar
def isletmekari(ilk6aykar,son6aykar):
    isletmekari=ilk6aykar-son6aykar
    if isletmekari>5000:
        print("işletme karlıdır")
    elif 1000<isletmekari<5000:
        print("işetme karı normal")
    else:
        print("işletme karı düşük")
ilk6aydakikar=ilk6aykar(a,b,c,d,e,f)
son6aydakikar=son6aykar(j,k,l,m,n,o,p)
isletmekari(ilk6aydakikar,son6aydakikar)


        

        



    
    
    
    
    
    
