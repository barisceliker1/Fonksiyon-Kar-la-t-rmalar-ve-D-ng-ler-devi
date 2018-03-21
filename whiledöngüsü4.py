personelsayisi=50
calismasüresi=40
ücret=90
mesaisaati=int(input("haftalık mesai saati giriniz:"))
while True:
    if mesaisaati*4>22 and mesaisaati>0:
        print("aylık mesai saati kuraldan fazladır düzeltiniz.mesai saatiniz:",mesaisaati*4)
        break
    elif mesaisaati*4<22 and mesaisaati>0:
        print("mesai yaptınız her mesai saati başı ücretin yüzde 10'u alıcaksınız",9)
        zamlıtoplammaas=personelsayisi*(calismasüresi*ücret)*(mesaisaati*9)
    elif mesaisaati*4<22 and mesaisaati==0:
            zamsıztoplammaas=personelsayisi*4*ücret
            print("mesaisiz toplam maaşı:",zamsıztoplammaas)
            break
