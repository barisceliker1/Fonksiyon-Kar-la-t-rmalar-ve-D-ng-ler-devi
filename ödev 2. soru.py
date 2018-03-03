def kullanabilirlik():
    x=int(input("Planlanmış üretim süresi"))
    y=int(input("plansız duruş giriniz"))
    z=int(input("planlanmış üretim süresi"))
    kullanabilirlik=(x-y)/z
    return kullanabilirlik
def performans():
    a=int(input("standart çevrim zamanı giriniz"))
    b=int(input("üretim miktarı giriniz"))
    c=int(input("planlanmış üretim süresi"))
    d=int(input("plansız duruş giriniz"))
    performans=(a*b)/(c-d)
    return performans
def kalite():
    a=int(input("sağlam ürün miktarı"))
    b=int(input("toplam üretim miktarı"))
    kalite=a/b
    return kalite
def OEE():
    OEE=kullanabilirlik()*performans()*kalite()
    return OEE
          
