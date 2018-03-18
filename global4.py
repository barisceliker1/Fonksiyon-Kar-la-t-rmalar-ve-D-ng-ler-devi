a=int(input("donem başındaki koltuk sayısını giriniz"))
b=int(input("dönem başındaki yatak sayısını giriniz"))
c=int(input("dönem başındaki dolap sayısını giriniz"))
donemsonukoltuk=25
donemsonuyatak=20
donemsonudolap=10
donemicikoltuk=10
donemiciyatak=15
donemicidolap=5
def donembasistok(a,b,c):
    global donembasistok
    donembasistok=a+b+c
    return donembasistok
def donemsonustok(donemsonukoltuk,donemsonuyatak,donemsonudolap,donemicikoltuk,donemiciyatak,donemicidolap):
    global donemsonustok
    donemsonustok=donemsonukoltuk+donemsonuyatak+donemsonudolap+donemicikoltuk+donemiciyatak+donemicidolap
    return donemsonustok
def ortalamastok(donembasistok,donemsonustok):
    ortalamastok=(donembasistok+donemsonustok)/2
    return ortalamastok
donemsonuhesap=donemsonustok(donemsonukoltuk,donemsonuyatak,donemsonudolap,donemicikoltuk,donemiciyatak,donemicidolap)
acilistok=donembasistok(a,b,c)
ortalamastok(acilistok,donemsonuhesap)
ortalamastok=(donembasistok+donemsonustok)/2
print("ortalama stok",ortalamastok)


