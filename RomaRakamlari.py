#!/usr/bin/env python
# -*- coding: utf-8
import re
def replace_last(source_string, replace_what, replace_with):
    head, sep, tail = source_string.rpartition(replace_what)
    return head + replace_with + tail

roma_rakamlari = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
white_list_roma = set('IVXLCDM')
white_list_arabic = set('1234567890')
white_list_binary = set('10')
white_list_menu = set('1239')

def roma_rakam_kontrol(kontrol_roma):

# roma rakamının boşluk veya başka karakterler içermemesinin kontrolü.
    while set(kontrol_roma).issubset(white_list_roma) == 0 or kontrol_roma =="" :
        print("Geçersiz bir roma rakamı girdiniz lütfen tekrar deneyin")
        return 0

# roma rakamı 15den uzun olamıyor. bunun kontrolü.
    if str(kontrol_roma).__len__() > 15:
        print "Roma sayıları 15den fazla rakam içeremez"
        return 0

# roma rakamının içerisinde birden fazla V L D  ve 3 ten fazla I X C M olmamasının kontrolü.
    nesne1 = re.findall("V", kontrol_roma)
    nesne2 = re.findall("L", kontrol_roma)
    nesne3 = re.findall("D", kontrol_roma)
    nesne4 = re.findall("IIII", kontrol_roma) + re.findall("XXXX", kontrol_roma) + re.findall("CCCC", kontrol_roma) + \
             re.findall("MMMM", kontrol_roma)

    if nesne1.__len__() > 1 or nesne2.__len__() > 1 or nesne3.__len__() > 1:
        print "V L D rakamları  1 den fazla kullanılamaz."
        return 0
    if nesne4.__len__() > 0 :
        print "I X C ve M rakamları 3den fazla tekrar edemez."
        return 0
######################################################################################################################

    i = 1
    for key in kontrol_roma:
# döngünün gereğinden fazla çalışmasını engelliyoruz.
        if kontrol_roma.__len__() -1 < i :
           break

#sol tarafta olan çıkarılacak rakamların sağındaki rakamdan 10 kattan fazla küçük olmamasının kontrolü.
        if roma_rakamlari.get(key) * 10 < roma_rakamlari.get(kontrol_roma[i]) and roma_rakamlari.get(key) < roma_rakamlari.get(kontrol_roma[i]):
                print "Bir sayı solundaki kendinden çıkacak sayının 10 katından büyük olamaz"
                return 0

# sol tarafa yazılap çıkarılabilecek sayilarin 1 tane  olması kontrolü.
        if kontrol_roma.__len__()-1 > i and roma_rakamlari.get(key) <= roma_rakamlari.get(kontrol_roma[i]) and roma_rakamlari.get(kontrol_roma[i]) < roma_rakamlari.get(kontrol_roma[i+1]):
            print "Rakamların sol tarafına yalnızca 1 adet çıkarılacak rakam yazılabilir."
            return 0
        if kontrol_roma.__len__()-1 > i and roma_rakamlari.get(key) < roma_rakamlari.get(kontrol_roma[i]) and roma_rakamlari.get(kontrol_roma[i]) == roma_rakamlari.get(kontrol_roma[i+1]):
            print "Rakamların değerleri büyükten küçüğe doğru gitmelidir.-"
            return 0
        if kontrol_roma.__len__()-1 > i and roma_rakamlari.get(key) > roma_rakamlari.get(kontrol_roma[i]) and roma_rakamlari.get(kontrol_roma[i+1]) > roma_rakamlari.get(key):
            print "Rakamların değerleri büyükten küçüğe doğru gitmelidir.--"
            return 0
        if kontrol_roma.__len__()-1 > i and roma_rakamlari.get(key) < roma_rakamlari.get(kontrol_roma[i]) and roma_rakamlari.get(kontrol_roma[i+1]) >= roma_rakamlari.get(key):
            print "Rakamların değerleri büyükten küçüğe doğru gitmelidir.---"
            return 0

# sol tarafa yazılan çıkarılacak sayıların 10un katları olmasının kontrolü.
        if  roma_rakamlari.get(key) < roma_rakamlari.get(kontrol_roma[i]) :
            if kontrol_roma[i-1] == "V" or kontrol_roma[i-1] == "L" or kontrol_roma[i-1] == "D" :
                print "Sol tarafa yazılacak çıkan rakamlar 10un kuvvetleri olmalıdır."
                return 0

        i += 1

# Roma rakamlarindan arabic-hindu rakamlarına dönüşüm.
def r_h(roma) :
    i = 1
    sayi = 0
    for key in roma :
        if roma.__len__() > i and roma_rakamlari.get(key) < roma_rakamlari.get(roma[i]) :
            sayi -= roma_rakamlari.get(key)
        else:
            sayi += roma_rakamlari.get(key)
        i += 1
    return str(sayi)

# Arabic-Hindu rakamlarindan roma rakamlarina donusum.
def h_r(h) :
    hindu = int(h)
    while hindu != 0 :
        if  1000 <= hindu: return "M"  + str(h_r(hindu-1000))
        if  900  <= hindu: return "CM" + str(h_r(hindu-900))
        if  500  <= hindu: return "D"  + str(h_r(hindu-500))
        if  400  <= hindu: return "CD" + str(h_r(hindu-400))
        if  100  <= hindu: return "C"  + str(h_r(hindu-100))
        if   90  <= hindu: return "XC" + str(h_r(hindu-90))
        if   50  <= hindu: return "L"  + str(h_r(hindu-50))
        if   40  <= hindu: return "XL" + str(h_r(hindu-40))
        if   10  <= hindu: return "X"  + str(h_r(hindu-10))
        if    9  <= hindu: return "IX" + str(h_r(hindu-9))
        if    5  <= hindu: return "V"  + str(h_r(hindu-5))
        if    4  <= hindu: return "IV" + str(h_r(hindu-4))
        if    1  <= hindu: return "I"  + str(h_r(hindu-1))

    return ""

def sirala(sayi):
        sayi = list(sayi)
        for i in range(0,sayi.__len__()):
            for j in range(1, sayi.__len__()):
                if roma_rakamlari.get(sayi[i]) < roma_rakamlari.get(sayi[j]) and i < j:
                    temp= sayi[i]
                    sayi[i] = sayi[j]
                    sayi[j] = temp

        donensayi = "".join(sayi)
        return donensayi

# DD XXXX IIII gibi rakamlari birlestirdigimiz yer.
def birlestir(sayi):
        I = re.findall("I", sayi)
        X = re.findall("X", sayi)
        C = re.findall("C", sayi)
        V = re.findall("V", sayi)
        L = re.findall("L", sayi)
        D = re.findall("D", sayi)
        VI = re.findall("VIIII",  sayi)
        LX = re.findall("LXXXX",  sayi)
        MC = re.findall("DCCCC", sayi)
        sadelestirme_gereksiz = 0
        if MC.__len__() > 0 :
            sayi = sayi.replace("DCCCC", "CM")
            sadelestirme_gereksiz = 1
            return sayi,sadelestirme_gereksiz
        if LX.__len__() > 0 :
            sayi = sayi.replace("LXXXX", "XC")
            sadelestirme_gereksiz = 1
            return sayi,sadelestirme_gereksiz
        if VI.__len__() > 0 :
            sayi = sayi.replace("VIIII", "IX")
            sadelestirme_gereksiz = 1
            return sayi,sadelestirme_gereksiz
        if I.__len__() == 6 : sayi = sayi.replace("IIIIII", "VI")
        if I.__len__() == 5 : sayi = sayi.replace("IIIII",  "V")
        if I.__len__() == 4 : sayi = sayi.replace("IIII",   "IV")

        if X.__len__() == 6 : sayi = sayi.replace("XXXXXX", "LX")
        if X.__len__() == 5 : sayi = sayi.replace("XXXXX",  "L")
        if X.__len__() == 4 : sayi = sayi.replace("XXXX",   "XL")

        if C.__len__() == 6 : sayi = sayi.replace("CCCCCC", "DC")
        if C.__len__() == 5 : sayi = sayi.replace("CCCCC",  "D")
        if C.__len__() == 4 : sayi = sayi.replace("CCCC",   "CD")


        if V.__len__() == 2 : sayi = sayi.replace("VV", "X")
        if L.__len__() == 2 : sayi = sayi.replace("LL", "C")
        if D.__len__() == 2 : sayi = sayi.replace("DD", "M")
        return sayi, sadelestirme_gereksiz

def geri_ayristir(sayi1, sayi2):
        negatif1 = ""
        i = 0
        while i < 2 :
            sayi1, negatif2 = ayristir(sayi1, 1)
            negatif1 +=  negatif2
            i += 1
            negatif2 = ""
        return sayi1, negatif1

def   sadelestir(sayi1, sayi2) :
    sadelestirme_gereksiz = 0



    def sadelestir1(sayi1,sayi2) :   # Eksi ve artı işaretli ayni sayıları sadeleştirme.
        sayac = 0
        while sayi2.__len__() > 0 and sayac < sayi2.__len__():
            j=0
            while sayi2.__len__()>0 and j < sayi1.__len__():
                if sayi2[sayac] == sayi1[j]:
                    if j-1 > -1 and roma_rakamlari.get(sayi1[j-1])*5 == roma_rakamlari.get(sayi1[j]):
                        sayi2 += sayi1[j-1]
                        sayi1 = sayi1.replace(sayi1[j-1], "", 1)
                        j -= 1

                    sayi1 = sayi1.replace(sayi1[j], "", 1)
                    sayi2 = sayi2.replace(sayi2[sayac], "", 1)
                    sayi2 = sirala(sayi2)
                    j -= 1
                    sayac = 0
                j += 1
            sayac +=1
        return sayi1, sayi2


    def direk_sol(sayi1,sayi2):
        white_list_direk_sol = set("IXC")
# Direk olarak  herhangi bir rakamın soluna yazabileceğimiz eksi işaretli rakamları yazıyoruz.
        z = 0 # sayi 1 tek haneli ise zyi 1 yapıp for dakı kontrole ekliyoruzki for en az 1 kere çalışsın.
        for i in range(0, sayi1.__len__()):
            for k in range(0, sayi2.__len__()):
               while sayi2.__len__()-1 >= k and set(sayi2[k]).issubset(white_list_direk_sol):
                   if k > sayi2.__len__()-1  : break
                   unique = re.findall(sayi2[k], sayi2)
                   unique2 = re.findall(sayi2[k], sayi1)
                   if unique.__len__() == 1 and unique2.__len__() == 0 :
                       if sayi1.__len__() == 1 : z = 1
                       for l in range(0, sayi1.__len__()-1 + z):
                               if sayi2.__len__()>0 and roma_rakamlari.get(sayi2[k])*10 >= roma_rakamlari.get(sayi1[sayi1.__len__()-l-1]):
                                   if roma_rakamlari.get(sayi2[k]) < roma_rakamlari.get(sayi1[sayi1.__len__()-l-1]):
                                       sayi1 = replace_last(sayi1, sayi1[sayi1.__len__()-l-1], sayi2[k]+sayi1[sayi1.__len__()-l-1])
                                       sayi2 = sayi2.replace(sayi2[k], "" ,1)
                                       k -= 1
                   break
        return sayi1, sayi2

    def parcala_birlestir(sayi1,sayi2):
        yeterli =  0 # 3 DEN FAZLA PARCALAMAYA IHTIYACIMIZ YOK GALIBA :)
        buldum  = ""
        len1 = sayi1.__len__()
        len2 = sayi2.__len__()
        if len2 > 0 :
# Direk sola yazılamayan veya sadeleşemeyen sayıları burda parçalayıp sadeleştirip tekrar birleştiriyoruz.
            for  z in range(0, len2):
                for p in range(0, len1):
                    if len2 > 0 and roma_rakamlari.get(sayi2[len2-z-1]) < roma_rakamlari.get(sayi1[len1-p-1]):
                       while roma_rakamlari.get(sayi2[len2-z-1])*10 <= roma_rakamlari.get(sayi1[len1-p-1])\
                               or sayi2[len2-z-1]== "V" or sayi2[len2-z-1] == "L" or sayi2[len2-z-1] == "D":
                           if yeterli < 3 and buldum.__len__() == 0:
             # parçalancak sayının solunda eksi değerli rakam var ise karışıklık olmaması için onu eksilere alıyoruz.
             # fakat sadece parçalan sayı solundakı sayının 5 katına eşit ise.Diğer türlü sorun çıkmıyor.
                               if  len1-p-2 >-1  and \
                                   roma_rakamlari.get(sayi1[len1-p-1]) == 5*roma_rakamlari.get(sayi1[len1-p-2]) and \
                                   roma_rakamlari.get(sayi1[len1-p-1]) > roma_rakamlari.get(sayi1[len1-p-2]) :
                                   sayi2 += sayi1[len1-p-2]
                                   sayi2 = sirala(sayi2)
                                   sayi1 = sayi1.replace(sayi1[len1-p-2], "",1)
                                   len1 = sayi1.__len__()
                                   len2 = sayi2.__len__()

                               sayi1 = parcala(sayi1, len1-p-1)
                               len1 = sayi1.__len__()
                               len2 = sayi2.__len__()
                               yeterli += 1
                               if yeterli > 1 and len1-p-2 >-1  and \
                                  roma_rakamlari.get(sayi1[len1-p-1]) == 5*roma_rakamlari.get(sayi1[len1-p-2]) and \
                                  roma_rakamlari.get(sayi1[len1-p-1]) > roma_rakamlari.get(sayi1[len1-p-2]) :
                                   sayi2 += sayi1[len1-p-2]
                                   sayi2 = sirala(sayi2)
                                   sayi1 = sayi1.replace(sayi1[len1-p-2], "",1)
                                   sayi1, sadelestirme_gereksiz = birlestir(sayi1)
                               for a in range(0, len2):
                                   buldum = re.findall(sayi2[a-z], sayi1)
                           else: return sayi1, sayi2
                       # sayi1, sayi2 = sadelestir(sayi1, sayi2)
                       # sayi1, sadelestirme_gereksiz  = birlestir(sayi1)
        if buldum == 0 :
            sayi1 = parcala(sayi1, len1-1)
            sayi1, sayi2 = sadelestir(sayi1, sayi2)
            sayi1, sadelestirme_gereksiz  = birlestir(sayi1)
            sayi2 , a = birlestir(sayi2)
        return sayi1, sayi2

    sayi1, sayi2 = sadelestir1(sayi1, sayi2)
# oluşan rakam kurallara uygun olana kadar birleştirip sadeleştiriyoruz.
    while sayi2.__len__() > 0 and roma_rakam_kontrol(sayi1) == 0 and sadelestirme_gereksiz==0 :
        sayi1, sadelestirme_gereksiz = birlestir(sayi1) 
        if sadelestirme_gereksiz == 0 :
            sayi1, sayi2 = sadelestir(sayi1, sayi2)

    if sayi2.__len__() > 0:
        sayi1, sayi2 = direk_sol(sayi1, sayi2)
    if sayi2.__len__() > 0:
        sayi1, sayi2 = parcala_birlestir(sayi1, sayi2)
    if sayi2.__len__() > 0:
        if sadelestirme_gereksiz == 0 :
            sayi1, sayi2 = sadelestir(sayi1, sayi2)
            sayi1, sadelestirme_gereksiz = birlestir(sayi1)
    else : sayi1, sayi2 = son_kontroller(sayi1, sayi2)





    if sayi2.__len__() > 0 : sayi1, sayi2 = sadelestir(sayi1, sayi2)
    return sayi1, sayi2

def parcala(sayi, indis):
        if sayi[indis] == "V" : sayi = replace_last(sayi, "V", "IIIII")
        if sayi[indis] == "X" : sayi = replace_last(sayi, "X", "VIIIII")
        if sayi[indis] == "L" : sayi = replace_last(sayi, "L", "XXXXX")
        if sayi[indis] == "C" : sayi = replace_last(sayi, "C", "LXXXXX")
        if sayi[indis] == "D" : sayi = replace_last(sayi, "D", "CCCCC")
        if sayi[indis] == "M" : sayi = replace_last(sayi, "M", "DCCCCC")
        return sayi

def son_kontroller(sayi1, sayi2):
        for s in range(0, sayi1.__len__()-1):
            if s < sayi1.__len__()-1 and roma_rakam_kontrol(sayi1) == 0 and negatif_var(sayi1) == 1\
                    and roma_rakamlari.get(sayi1[s])*5 == roma_rakamlari.get(sayi1[s+1]) :
                    sayi1 , yenisayi2 = geri_ayristir(sayi1, sayi2)
                    sayi2 = sirala(sayi2 + yenisayi2)
                    yenisayi2 = ""
        return sayi1, sayi2

def negatif_var(sayi1):
    for i in range(0, sayi1.__len__()-1):
        if roma_rakamlari.get(sayi1[i]) < roma_rakamlari.get(sayi1[i+1]):
            return 1
    return 0

# roma rakamını + - olarak işaretlendirip ayırıyoruz.
def ayristir(r1,islem):

    eksiler = ""
    artilar = ""
    if islem == 1: # islem= 1 toplama demek sayilar normal ayristirilir.
        for i in range(0, r1.__len__()-1) :
            if roma_rakamlari.get(r1[i]) < roma_rakamlari.get(r1[i+1]) :
                eksiler += r1[i]
            else:
                artilar += r1[i]
     # en sonda tek kalan rakamı direk artılara yazabiliriz.
            if i+1 == r1.__len__()-1 :
                artilar += r1[i+1]
 # Eğer girilen rakamlar tek haneli ise ayrıştırma yapmadan direk  yazabiliriz.
        if r1.__len__() == 1 : artilar += r1

    else:            # Çıkarma durumu
        for i in range(0, r1.__len__()-1) :
            if roma_rakamlari.get(r1[i]) < roma_rakamlari.get(r1[i+1]) :
                artilar += r1[i]
            else:
                eksiler += r1[i]
     # en sonda tek kalan rakamı direk artılara yazabiliriz.
            if i+1 == r1.__len__()-1 :
                eksiler += r1[i+1]
 # Eğer girilen rakamlar tek haneli ise ayrıştırma yapmadan direk  yazabiliriz.
        if r1.__len__() == 1 : eksiler += r1
    return artilar,eksiler

def roma_toplama(r1,r2):
    artilar1, eksiler1 = ayristir(r1, 1) # 1 sayıyı normal ayrıstırırken 0 - ile çarpıyormuş gibi ayrıştırır.
    artilar2, eksiler2 = ayristir(r2, 1)
    artilar = artilar1 + artilar2
    eksiler = eksiler1 + eksiler2

    artilar = sirala(artilar)
    eksiler = sirala(eksiler)
    artilar, eksiler = sadelestir(artilar, eksiler)
    return artilar


def roma_cikarma(r1,r2):
    artilar1, eksiler1 = ayristir(r1, 1)
    artilar2, eksiler2 = ayristir(r2, 0)
    artilar = artilar1 + artilar2
    eksiler = eksiler1 + eksiler2

    artilar = sirala(artilar)
    eksiler = sirala(eksiler)
    #eksiler, a = birlestir(eksiler)
    artilar, eksiler = sadelestir(artilar, eksiler)
    i = 0
    while roma_rakam_kontrol(artilar) == 0 and i < 3:
           artilar , a = birlestir(artilar)
           i += 1


    if i < 2 : artilar ,eksiler = sadelestir(artilar, eksiler)

    return artilar

#
# def binary_toplam(n1,n2) :
#
# def binary_cikarma(n1,n2) :
#
# def binary_carpma(n1,n2) :
#
# def binary_bolme(n1,n2) :
secim = 0
while(secim != 9):
    print "Yapmak istediginiz islemi secin \n \
           1. Roma rakamından Hindu-Arab rakamına dönüşüm \n \
           2. Hindu-Arab rakamından Roma rakamına dönüşüm \n \
           3. Roma rakamları ile toplama veya cıkarma \n \
           9. Çıkış "
    secim = raw_input("")
# seçim işleminin 1 2 3  ve 9 karakterlerinden başka olmamasınının kontrolü.
    while set(secim).issubset(white_list_menu) == 0 or secim.__len__() > 1 or secim =="":
        secim = raw_input("Lütfen geçerli bir seçim yapınız ")

    if (secim) == "1":
        roma = raw_input("Dönüştürmek istediğiniz roma rakamı girin.")
# Girilen rakamın roma rakamı olup olmadığının kontrolü
        while  roma_rakam_kontrol(roma) == 0  :
            roma = raw_input("Geçersiz bir roma rakamı girdiniz lütfen tekrar deneyin: \n ")

# Girilen rakamın dönüştürülmüş halinin kullanıcıya gösterilmesi
        print "Girdiğiniz rakamın dönüşmüş hali: %s" % (r_h(roma))


    if secim == "2" :
        hindu_arabic = raw_input("Dönüştürmek istediğiniz sayıyı giriniz: ")

        while set(hindu_arabic).issubset(white_list_arabic) == 0 or 1 < int(hindu_arabic) > 3999 or hindu_arabic == "":
            hindu_arabic = raw_input("Girdiğiniz sayı 1-3999 arasında olmalıdır: ")
        print "Girdiğiniz sayının dönüşmüş hali: %s" % (h_r(hindu_arabic))

    if secim == "3" :
        roma1 = raw_input("Birinci rakamı girin: ")
        roma2 = raw_input("İkinci  rakamı  girin: ")
        while True:
            while  roma_rakam_kontrol(roma1) == 0 or roma_rakam_kontrol(roma2) == 0:
                print ("Geçersiz bir roma rakamı girdiniz tekrar deneyin.")
                roma1 = raw_input("Birinci rakamı girin: \n")
                roma2 = raw_input("İkinci  rakamı  girin: \n")

            islem = raw_input("Yapacağınız işlemi seçin \n 1.Toplama \n 2.Çıkarma \n 3.Ana menüye dön :(\n")
            if islem == "1" and int(r_h(roma1)) + int(r_h(roma2)) > 3999 :
                print "İşlem sonucu oluşacak sayı 3999'dan büyük olamaz"
                break
            if islem == "2" and int(r_h(roma1)) - int(r_h(roma2)) < 1 :
                print "İşlem sonucu oluşacak sayı 1'den küçük olamaz"
                break
            if islem == "3" : break

            if islem == "1" :
                print "Girdiğiniz sayıların toplamı: %s" % (roma_toplama(roma1, roma2))
            if islem == "2" :
                print "Girdiğiniz sayıların farkı:   %s" % (roma_cikarma(roma1, roma2))
