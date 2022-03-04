import random
import time

class Kumanda():
    def __init__(self,tv_durum="Kapalı",tv_ses =0,kanal_listesi=["Trt"],kanal="Trt"):
        print("kumanda oluşturuluyor")
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi=kanal_listesi
        self.kanal=kanal


    def tv_ac(self):
        if(self.tv_durum == "Açık"):
            print("Televizyon zaten açık..")
        else:
            print("Televizyon açılıyor..")
            self.tv_durum= "Açık"


    def tv_kapat(self):
        if(self.tv_durum=="Kapalı"):
            print("televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor..")
            self.tv_durum="Kapalı"


    def ses_ayarlari(self):

        while True:
            karakter=input("Azaltmak için '<' Arttırmak için '>' Tamam ise 'exit' yazınız ")
            if(karakter == '<'):
                if(self.tv_ses ==0):
                    print("Ses zaten kapalı")
                else:
                    self.tv_ses -=1
                    print("Ses: ",self.tv_ses)
            elif(karakter =='>'):
                if(self.tv_ses==31):
                    print("Ses son seviyede..")
                else:
                    self.tv_ses += 1
                    print("Ses: ", self.tv_ses)
            elif(karakter=='exit'):
                print("Ses güncellendi..")
                print("Ses: ", self.tv_ses)
                break


    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor..")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)


    def rastgele_kanal(self):
        rastgele =random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki kanal: ",self.kanal)


    def __len__(self):
        return len(self.kanal_listesi)


    def __str__(self):
        return "Tv Durum: {} \nTv ses: {} \nKanal Listesi : {} \nŞu anki Kanal: {}".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)
kumanda = Kumanda()

print(""""
Televizyon uygulaması
1.Tv aç
2.Tv Kapat
3.Ses Ayarları
4.Kanal Ekle
5.Kanal Sayısı Öğrenme
6.Rastgele Kanal Geçme
7. Televizyon Bilgileri
Çıkmak için q ya basınız..
""")
while True:
    işlem = input("işlem Seçiniz:")
    if(işlem=="q"):
        print("Program sonlanıyor")
        break

    elif(işlem=="1"):
        kumanda.tv_ac()

    elif(işlem =="2"):
        kumanda.tv_kapat()

    elif(işlem== "3"):
        kumanda.ses_ayarlari()

    elif(işlem=="4"):
        kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak yazınınız")
        kanal_listesi=kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif(işlem=="5"):
        print("Kanal sayısı: ",len(kumanda))

    elif(işlem=="6"):
        kumanda.rastgele_kanal()

    elif(işlem=="7"):
        print(kumanda.__str__())

    else:
        print("Geçersiz işlem")
