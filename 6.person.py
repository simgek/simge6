kisiler = []

class Person:
    firstname = "",
    lastname  = "",
    phone     = "",
    mail      = "",
    id        = "",

    def __str__(self):
        return "{} {}".format(self.firstname ,self.lastname)
    def Bul(self,kelime):
        if kelime in self.firstname or kelime in self.lastname or kelime in self.phone or kelime in self.mail:
            return True
        else:
            return False



isimler = ["simge", "okan", "beste", "rabia", "dilara", "çağla", "başak", "beril", "batuhan", "sinan"]
soyisimler = ["elma", "armut", "çilek", "şeftali", "karpuz", "kavun", "kayısı", "erik", "kiraz", "vişne"]

import random
for i in range(10):
    kisi = Person()
    kisi.firstname = random.choice(isimler)
    kisi.lastname = random.choice(soyisimler).upper()
    kisi.phone = "+(90)5{} {} {} {}".format(random.randrange(10,99),random.randrange(100,999),random.randrange(10,99),random.randrange(10,99))
    kisi.mail = "{}.{}@bilgeadam.com".format(kisi.firstname.lower(),kisi.lastname.lower())
    kisiler.append(kisi)

#for kisi in kisiler:
  #  print("-"*40)
   # print("kişi adı : {}\nkisi soyadı : {}\nkisi telefonu : {}\nkişi maili : {}".format(kisi.firstname,kisi.lastname,kisi.phone,kisi.mail))

def Liste(kelime = ""):
    if kelime == "":
        i = 0
        for kisi in kisiler:
           print("-" * 50)
           print("id : {}\nkişi adı : {}\nkisi soyadı : {}\nkisi telefonu : {}\nkişi maili : {}".format(i,
                                                                                                         kisi.firstname,
                                                                                                         kisi.lastname,
                                                                                                         kisi.phone,
                                                                                                         kisi.mail))
           i += 1
    else:
        i = 0
        for kisi in kisiler:
            if kisi.Bul(kelime):
              print("-" * 50)
              print("id : {}\nkişi adı : {}\nkisi soyadı : {}\nkisi telefonu : {}\nkişi maili : {}".format(i,
                                                                                                         kisi.firstname,
                                                                                                         kisi.lastname,
                                                                                                         kisi.phone,
                                                                                                         kisi.mail))
              i += 1


        print("kişiyi bul")

def Main():
    ekle = "a"
    sil =  "d"
    guncelle = "u"
    liste = "l"
    bul = "f"
    islem = ""
    go_on = "y"
    result = True

    while True:

        print("lütfen yapmak için bir işlem seçiniz")
        print("-"*32)
        print("kişi eklemek için : a\nkişi silmek için : d\nkişi güncellemek için : u\nkişi listelemek için : l\nkişi bulmak için : f ")
        print("-"*32)
        islem = input("lütfen bir anahtar kelime giriniz : ").lower()

        if islem == "a":
            kisi = Person()
            kisi.firstname = input("lütfen isim giriniz : ")
            kisi.lastname = input("lütfen soyisim giriniz : " )
            kisi.phone = input("lütfen telefon giriniz : ")
            kisi.mail = input("lütfen mail giriniz : ")
            kisiler.append(kisi)
            print("kişi rehbere eklendi")

        elif islem == "d":
            Liste()
            id = int(input("lütfen id değerini giriniz"))
            kisiler.remove(kisiler[id])
            print("kişi rehberden silindi")

        elif islem == "u":
            Liste()

            id = int(input("lütfen güncellemek istdiğiniz kişinin id değerini giriniz : "))

            upsate_person = kisiler[id]
            for key, value in vars(upsate_person).items():
                v1 = input("lüyfen giriniz : ".format(key))
                vars(upsate_person).__setitem__(key,v1)
            #upsate_person = input("lütfen isim giriniz : ")
            #upsate_person = input("lütfen soyisim giriniz : ")
            #upsate_person = input("lütfen telefon giriniz : ")
            #upsate_person = input("lütfen mail giriniz : ")
            print("kişi rehberde güncellendi")

        elif islem == "l":
            Liste()
            print("kişi listesi ")

        elif islem == "f":
            Liste(input("lütfen anahtar kelimeyi giriniz : "))

            print("kişi bilgiler")

        else:
            result = False
            print("rehber uygulamasından çıkış sağlandı")
        print("devam etmek için herhangi bir tuşa basın")


Main()

#kullanıcı dışardan telefon  numarası girdiğine içeride telefon formatlanması
#metot içerisinde telefon numarası alacak geriye formatlı bir şekilde teslim edecek
#minimum girilecek değeri 10 hanedir, eğer kullanıcı eksik değer girerse uyarı verdiriniz
# 05332576414 => +90 (533) 257 64 14
# 5332576414
# 905332576414
#+905332576414