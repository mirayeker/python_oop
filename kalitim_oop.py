class Calisan ():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfının init fonksiyonu")
        self.isim=isim
        self.maaş=maaş
        self.departman =departman
    def bilgileri_goster(self):
        print("Çalışan sınıf bilgileri")
        print("isim: {} \nMaaş: {} \nDepartman: {}".format(self.isim,self.maaş,self.departman))
    def departman_degistir(self,yeni_departman):
        self.departman=yeni_departman
class Yönetici(Calisan):
    #pass eğer burayı boş bırakıp sonra yazmak istiyorsak pass deyip geçebilriz sıkıntı çıkmaz
    def __init__(self,isim,maaş,departman,kişi_sayısı): #OVERRIDING ETTİK !!!
        super().__init__(isim, maaş, departman)
        #Alttaki selfle başlayan 3 kodu kısaca böyle yazabillriz
        print("Yönetici sınıfının init fonksiyonu")
        #self.isim = isim
        #self.maaş = maaş
        #self.departman = departman

        self.kişi_sayısı=kişi_sayısı
    def zam_yap(self,zam_miktarı):
        self.maaş +=zam_miktarı

    def bilgileri_goster(self):
        print("Yönetici sınıf bilgileri")
        print("isim: {} \nMaaş: {} \nDepartman: {} \nSorumlu kişi sayısı: {}".format(self.isim, self.maaş, self.departman,self.kişi_sayısı))
yonetici2= Yönetici("Dilara Eker",500,"Bilişim",35)
yonetici2.bilgileri_goster()



