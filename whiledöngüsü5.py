gunlukuretim=200
defoluurun=int(input("defolu üürün sayısı giriniz"))
kacgunluk=gunlukuretim/defoluurun
i=0
while True:
    i=i+1
    if defoluurun>gunlukuretim/100*20:
        print("defolu ürün miktarınız çok artmıştır")
    else:
        print("1 günde üretilen",gunlukuretim,"pantolondan",defoluurun,"tanesi defoludur")
        break
