#a=toplamsatis miktari
#b=hammadde maliyeti
#c=bakım onarım giderleri
#d=sevkiyat giderleri
#e=satın alınan hizmet giderleri
a=int(input("Toplam satış miktarı giriniz"))
b=int(input("hammadde maliyeti giriniz"))
c=int(input("bakım onarım giderleri giriniz"))
d=int(input("sevkiyat giderleri girini"))
e=int(input("satın alınan hizmet giderleri"))
def katmadeğercirosu(a,b,c,d,e):
    global ciro
    ciro=a-(b+c+d+e)
    return ciro
def katmadeğercirosu(a,b,c,d,e):
    ciro=a-(b+c+d+e)
    if ciro>1000:
        print("işletme katma değer cirosu yüksek")
    elif 500<ciro<1000:
        print("işletme katma değer cirosu normal")
    else:
        print("işletme katma değer cirosu düşük")
ciro=katmadeğercirosu(a,b,c,d,e)
ciro=a-(b+c+d+e)
    
    
    
