a=int(input("finansman geliri giriniz"))
b=int(input("pazar geliri giriniz"))
c=int(input("kira geliri giriniz"))
d=int(input("ücret giriniz"))
e=int(input("finansman gideri giriniz"))
f=int(input("pazar gideri giriniz"))
g=int(input("kira gideri giriniz"))
x=int(input("muhasebe gideri giriniz"))
gelir=a+b+c
gider=d+e+f+g+x
kar=gelir-gider
if kar>1000:
    print("karlı bir iş")
elif kar==1000:
    print("denge")
else:
    print("zarar")
