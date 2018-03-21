bsm=10000
satilan=500
alinan=100
i=1
while True:
    stokmiktari=bsm-((satilan-alinan)*i)
    i=i+1
    if stokmiktari==0:
        print("sıfırlanacağı ay sayısı",i)
