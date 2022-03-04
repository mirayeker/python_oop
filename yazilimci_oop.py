class Yazilimci():
    def __init__(self,isim,soyisim,numara,maas,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maas=maas
        self.diller=diller
    def bilgilerigoster(self):
        print("""
        Yazılımcı objesinin özellikleri
        İsim : {}
        Soyisim : {}
        Numara : {}
        Maas : {}
        Bildiği Diller : {}
        """.format(self.isim,self.soyisim,self.numara,self.maas,self.diller))
    def zam_yap(self,zam_miktari):
        print("Zam Yapılıyor...")
        self.maas +=zam_miktari
    def dil_ekle(self,yeni_dil):
        print("Dil ekleniyorr..")
        self.diller.append(yeni_dil)
yazilimci =Yazilimci("Miray","Eker",5325456071,15000,["Python","Java","C"])
yazilimci.bilgilerigoster()
yazilimci.zam_yap(5000)
yazilimci.dil_ekle("C#")
yazilimci.bilgilerigoster()