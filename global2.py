calisilansüre1=170
toplammüsterisayisi1=50
calisilansüre2=220
toplammüsterisayisi2=70
def ilkcalismasüresi(calisilansüre1,toplammüsterisayisi1):
    global ilkcalismasüresi
    ilkcalismasüresi=calisilansüre1/toplammüsterisayisi1
    return ilkcalismasüresi
def sonrakicalismasüresi(calisilansüre2,toplammüsterisayisi2):
    global sonrakicalismasüresi
    sonrakicalismasüresi=calisilansüre2/toplammüsterisayisi2
    return sonrakicalismasüresi
def müsterilerlecalismasüresi(sonrakicalismasüresi,ilkcalismasüresi):
    global müsterilerlecalismasüresi
    müsterilerlecalismasüresi=sonrakicalismasüresi-ilkcalismasüresi
    return müsterilerlecalismasüresi
ilkcalismasüresi(calisilansüre1,toplammüsterisayisi1)
sonrakicalismasüresi(calisilansüre2,toplammüsterisayisi2)
müsterilerlecalismasüresi(sonrakicalismasüresi,ilkcalismasüresi)
print(müsterilerlecalismasüresi)




    
    
    
    
    
    
