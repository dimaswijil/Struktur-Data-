class Peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":",self.cityList[kota])
        
    def tambahkanKota(self,kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def hapusKota(self,kotaDihapus):
        #cek apakah kota yang ingin dihapus ada di list
        if kotaDihapus in self.cityList:
        #iterasi setiap kotalain untuk hapus kotadihapus
            for kotalain in self.cityList:
                #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
                if kotaDihapus in self.cityList[kotalain]:
                    self.cityList[kotalain].remove(kotaDihapus)
            del self.cityList[kotaDihapus]
            return True
        return False
    
    def tambahkanJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #masukkan kota 1 di list kota2
            self.cityList[kota2].append(kota1)
            #masukkan kota 2 di list kota1
            self.cityList[kota1].append(kota2)
            return True
        return False
    
    def hapusJalan(self,kota1,kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            #hapus kota 1 di list kota2
            self.cityList[kota2].remove(kota1)
            #hapus kota 2 di list kota1
            self.cityList[kota1].remove(kota2)
            return True
        return False
        

petajawabarat = Peta()
petajawabarat.tambahkanKota("Cikampek")
petajawabarat.tambahkanKota("Purwakarta")
petajawabarat.tambahkanKota("Subang")
petajawabarat.tambahkanKota("Bandung")
petajawabarat.tambahkanKota("Sumedang")
petajawabarat.tambahkanKota("Garut")
petajawabarat.tambahkanKota("Cianjur")
petajawabarat.tambahkanKota("Sukabumi")
petajawabarat.tambahkanKota("Tasikmalaya")
petajawabarat.tambahkanKota("Kuningan")
petajawabarat.tambahkanKota("Cirebon")
petajawabarat.tambahkanKota("Banjar")
petajawabarat.tambahkanKota("Indramayu")

petajawabarat.tambahkanJalan("Cikampek","Purwakarta")
petajawabarat.tambahkanJalan("Subang","Cikampek")
petajawabarat.tambahkanJalan("Subang","Purwakarta")
petajawabarat.tambahkanJalan("Bandung","Subang")
petajawabarat.tambahkanJalan("Cianjur","Sukabumi")
petajawabarat.tambahkanJalan("Cianjur","Bandung")
petajawabarat.tambahkanJalan("Bandung","Sumedang")
petajawabarat.tambahkanJalan("Bandung","Purwakarta")
petajawabarat.tambahkanJalan("Bandung","Garut")
petajawabarat.tambahkanJalan("Garut","Tasikmalaya")
petajawabarat.tambahkanJalan("Garut","Kuningan")
petajawabarat.tambahkanJalan("Cirebon","Kuningan")
petajawabarat.tambahkanJalan("Sumedang","Kuningan")
petajawabarat.tambahkanJalan("Tasikmalaya","Kuningan")
petajawabarat.tambahkanJalan("Banjar","Kuningan")
petajawabarat.tambahkanJalan("Banjar","Tasikmalaya")
petajawabarat.tambahkanJalan("Cirebon","Sumedang")
petajawabarat.tambahkanJalan("Cirebon","Indramayu")
petajawabarat.tambahkanJalan("Subang","Indramayu")
petajawabarat.tambahkanJalan("Sumedang","Indramayu")
petajawabarat.tambahkanJalan("Subang","Indramayu")
petajawabarat.tambahkanJalan("Sumedang","Indramayu")
petajawabarat.printPeta()
print('------------------------------')
petajawabarat.hapusKota("Banjar")
petajawabarat.printPeta()

