class Peta:
    def __init__(self):
        self.listKota = {}

    def printPeta(self):
        for kota in self.listKota:
            print(kota, ":", self.listKota[kota])

    def tambahkanKota(self, kota):
        if kota not in self.listKota:
            self.listKota[kota] = {}
            return True
        return False

    def hapusKota(self, hapusKota):
        if hapusKota in self.listKota:
            for kotaLain in self.listKota:
                if hapusKota in self.listKota[kotaLain]:
                    del self.listKota[kotaLain][hapusKota]
            del self.listKota[hapusKota]
            return True
        return False

    def tambahkanJalan(self, kota1, kota2, jarak):
        if kota1 in self.listKota and kota2 in self.listKota:
            self.listKota[kota2][kota1] = jarak, 'KM'
            self.listKota[kota1][kota2] = jarak, 'KM'
            return True
        return False

    def hapusJalan(self, kota1, kota2):
        if kota1 in self.listKota and kota2 in self.listKota:
            if kota1 in self.listKota[kota2]:
                del self.listKota[kota2][kota1]
            if kota2 in self.listKota[kota1]:
                del self.listKota[kota1][kota2]
            return True
        return False

    def djikstra (self, source):
        jarak = {kota: float('inf') for kota in self.listKota}
        jarak[source] = 0

        unvisitedCities = list(self.listKota.keys())
        while unvisitedCities:
            minJarak = float('inf')
            dekatKota = None

            for kota in unvisitedCities:
                if jarak[kota] < minJarak:
                    minJarak = jarak[kota]
                    dekatKota = kota
            unvisitedCities.remove(dekatKota)

            for neighbor, weight in self.listKota[dekatKota].items():
                jarakNeighbor = jarak[dekatKota] + weight[0]
                if jarakNeighbor < jarak[neighbor]:
                    jarak[neighbor] = jarakNeighbor

        return jarak


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
print('------------------------------')
print('Jalan yang terhubung')

petajawabarat.tambahkanJalan("Cikampek","Purwakarta", 22)
petajawabarat.tambahkanJalan("Subang","Cikampek",54)
petajawabarat.tambahkanJalan("Subang","Purwakarta", 57)
petajawabarat.tambahkanJalan("Bandung","Subang", 61)
petajawabarat.tambahkanJalan("Cianjur","Sukabumi", 31)
petajawabarat.tambahkanJalan("Cianjur","Bandung", 65)
petajawabarat.tambahkanJalan("Bandung","Sumedang", 54)
petajawabarat.tambahkanJalan("Bandung","Purwakarta", 62)
petajawabarat.tambahkanJalan("Bandung","Garut", 131)
petajawabarat.tambahkanJalan("Garut","Tasikmalaya", 88)
petajawabarat.tambahkanJalan("Garut","Kuningan", 161)
petajawabarat.tambahkanJalan("Cirebon","Kuningan", 35)
petajawabarat.tambahkanJalan("Sumedang","Kuningan", 120)
petajawabarat.tambahkanJalan("Tasikmalaya","Kuningan", 80)
petajawabarat.tambahkanJalan("Banjar","Kuningan", 73)
petajawabarat.tambahkanJalan("Banjar","Tasikmalaya", 44)
petajawabarat.tambahkanJalan("Cirebon","Sumedang", 95)
petajawabarat.tambahkanJalan("Cirebon","Indramayu", 55)
petajawabarat.tambahkanJalan("Subang","Indramayu", 81)
petajawabarat.tambahkanJalan("Sumedang","Indramayu", 99)
petajawabarat.printPeta()
print('------------------------------')
#print('Banjar')

petajawabarat.djikstra("Bandung")
jarakSemuaKota = petajawabarat.djikstra("Bandung")
print("Jarak Kota Berikut Nya dari Bandung")
for kota, jarak in jarakSemuaKota.items():
    print(kota, "adalah", jarak, "KM")
