a=int(input("Beğeni sayısını giriniz:"))
b=int(input("Yorum sayısını giriniz:"))
c=int(input("Paylaşım sayısını giriniz:"))
d=int(input("İçerik sayısını giriniz:"))
e=int(input("Takipçi sayısını giriniz:"))
def etkilesimorani(a,b,c,d,e):
    global etkilesimorani
    etkilesimorani=(((a+b+c)/d)/e)
    return etkilesimorani
if etkilesimorani(a,b,c,d,e)<0.2:
    print("başarısız ve etkileşim oranınız",etkilesimorani)
else:
    print("Başarılı",etkilesimorani)

