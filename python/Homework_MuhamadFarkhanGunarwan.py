class Hewan:
    # class attributes
    nama_latin = "Animalia"

    # instance attributes
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # instance method
    def bangun(self):
        return "{} sudah bangun".format(self.nama)

    # class method
    @classmethod
    def change_name_latin(cls):
        return "Felis Catus"

# Checker
h = Hewan('doggie',10)
print(h.bangun())
print(h.change_name_latin())

class Kucing(Hewan):
    # set class attributes using class method
    nama_latin_2 = Hewan.change_name_latin()

    def __init__(self, nama, umur, kecepatan):
        super().__init__(nama,umur)
        self.kecepatan = kecepatan

    # override method bangun
    def bangun(self):
        return "si Kucing bangun"

    # new method
    def lari(self):
        if self.kecepatan > 10:
            print("cepat sekali")
        else: print("lambat")

# Checker
    print(nama_latin_2)
k = Kucing("kitty",5,13)
print(k.bangun())
k.lari()
