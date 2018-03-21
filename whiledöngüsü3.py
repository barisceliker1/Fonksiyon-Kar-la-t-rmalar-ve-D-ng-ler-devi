#kullanıcıya programdan çıkması için bilgi veriyorum
print("çıkmak için 0 yazınız")
#boş bir liste açıyorum
yeni=[]
while True:
    girilensayi=int(input("bir sayı giriniz"))
    #girilen sayının 3'e bölümünden kalanı bulucam
    kalan=girilensayi%3
    #şimdi bu kalanları boş bir yeniye atıyorm
    yeni.append(kalan)
    #attığım her kalanın bir öncekiyle toplanmasını sağlıyorum.
    toplam=sum(yeni)
    print(toplam)
    if girilensayi==0:
        break

