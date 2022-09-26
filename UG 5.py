class Mobil:

    _Merk = None
    _Tipe = None
    _kapasitasBBM = None
    _jenisBahanBakar = None

    def __init__(self,Merk,Tipe):
        self._Merk = Merk
        self._Tipe = Tipe
        self._kapasitasBBM = None
        self._jenisBahanBakar = None

    def printInfo(self):
        print("============INFO============")
        print("Merk           : ", self.getMerk())
        print("Tipe           : ", self.getTipe())
        print("Bahan Bakar    : ", self.getjenisBahanBakar())
        print("Kapasitas BBM  : ",self.getkapasitasBBM())

    def getMerk(self):
        return self._Merk
    
    def getTipe(self):
        return self._Tipe

    def getkapasitasBBM(self):
        return self._kapasitasBBM

    def setkapasitasBBM(self,kapasitasBBM):
        self._kapasitasBBM = kapasitasBBM

    def setjenisBahanBakar(self,jenisBahanBakar):
        self._jenisBahanBakar = jenisBahanBakar 
    
    def getjenisBahanBakar(self):
        return self._jenisBahanBakar
    
    def isiBBM(self,uang):
        if self._kapasitasBBM == None:
            print("ERROR! Kapastas BBM atau Jenis Bahan Bakar belum diinputkan")
        else:
            a = uang * self._kapasitasBBM
            print("Mengisi ", self._kapasitasBBM, "liter")
            print("Total Harga :",a )

if __name__ == "__main__":
    m1 = Mobil("Toyota", "Avanza")
    m1.printInfo()
    m2 = Mobil("Nissan", "Grand Livina")
    m2.setjenisBahanBakar("Bensin")
    m2.setkapasitasBBM(20)
    m2.printInfo()
    m1.isiBBM(14500)
    m2.isiBBM(14500)














        

