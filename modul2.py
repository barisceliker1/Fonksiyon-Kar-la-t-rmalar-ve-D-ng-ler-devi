a=int(input("100 kasa heasbı giriniz"))
b=int(input("101 alınan çekler giriniz"))
c=int(input("102 bankalar hesabına değer giriniz"))
d=int(input("121 alacak senetleri hesabına değer giriniz"))
e=int(input("153 Ticari mal hesabına değer giriniz"))
f=int(input("252 Binalar hesabaına değer giriniz"))
g=int(input("254 taşıtlar hesabına değer giriniz"))
h=int(input("255 demirbaşlar hesabına değer giriniz"))
def aktif(a,b,c,d,e,f,g,h):
            global aktif
            aktif=a+b+c+d+e+f+g+h
            return aktif
x=int(input("300 banka kredileri hesabına değer giriniz"))
y=int(input("320 satıcılar hesabına değer giriniz"))
z=int(input("400 banka kredileri hesabına değer giriniz"))
w=int(input("421 borç senetleri hesabına değer giriniz"))
v=int(input("500 sermaye hesabına değer giriiniz"))
def pasif(x,y,z,w,v):
            global pasif
            pasif=x+y+z+w+v
            return pasif
aktif(a,b,c,d,e,f,g,h)
pasif(x,y,z,w,v)
print("bilançonun aktif tarafının miktarı:",aktif)
print("bilançonun pasif tarafının miktarı:",pasif)
def kapanis(aktif,pasif):
    if (aktif==pasif):
        print("kapanış bilançosu doğru hesaplandı")
    else:
        print("kapanış bilançosu yanlış hesaplandı")
kapanis(aktif,pasif)

