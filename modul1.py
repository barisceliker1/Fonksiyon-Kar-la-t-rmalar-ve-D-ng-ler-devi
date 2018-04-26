gelirler=int(input("gelir giriniz:"))
giderler=int(input("gider giriniz:"))
def isletmekari(gelirler,giderler):
    global isletmekari
    isletmekari=gelirler-giderler
    return isletmekari
toplamciro=int(input("toplam ciro giriniz:"))
toplamcalisansayisi=int(input("toplam çalışan sayısı giriniz"))
def adambasiciro(toplamciro,toplamcalisansayisi):
    global adambasiciro
    adambasiciro=toplamciro/toplamcalisansayisi
    return adambasiciro
isletmekari(gelirler,giderler)
adambasiciro(toplamciro,toplamcalisansayisi)
print("işletme karı:",isletmekari)
print("adam başı ciro:",adambasiciro)
