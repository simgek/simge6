class Personel:
    baslangic_maas = 1.400
    def __init__(self,Ad,Soyad,Telefon):
        self.Ad      = Ad
        self.Soyad   = Soyad
        self.Telefon = Telefon

    def TamAdi(self):
        return "{} {}".format(self.Ad,self.Soyad)
    def Telefon(self):
        return "+(90){}".format(self.Telefon)
    def __str__(self):
        return "{} {} {}".format(self.Ad,self.Soyad,self.Telefon)


class Yazilimci(Personel):
    baslangic_maas = 10.000

    def __init__(self,Ad,Soyad,Telefon,Yazılımdili):

        super().__init__(Ad,Soyad,Telefon) # miras aldığımız sınıfın constructor (yapıvı metot)(__init__)değerine parametre gönderiyoruz

        # Personel.__init__(Ad,Soyad,Telefon)=> süper metoduyla aynı iş görür fakata sınıf ismini değişitirdiğinizde personel
        # employee olursa bu alanı da değiştirmenzi gerekecektir

        self.Yazılımdili = Yazılımdili


    def __str__(self):
        print("{} {}".format(super().__str__(),self.Yazılımdili))

personel = Personel("simge", "karademir", "11111",)
yazilimci = Yazilimci("simge", "karademir", "11111", "python")

print(personel)
print(yazilimci)

print(issubclass(Personel,Yazilimci))
print(issubclass(Yazilimci,Personel))




