# a = 21
# b = 23
#
# if a > b:
#     print("a > b")
# # elif b > a:
#     print("a < b")

# from python_sesi_3 import perkalian
#
# if __name__ == '__main__':
#     hasil = perkalian(2,3)
#     print(hasil)

# for num in range(10, 14):
#     for i in range(2, num):
#         if num % i == 1:
#             print(num)
#             break

# numbers = [10, 20]
# items = ["Chair", "Table"]
#
# for x in numbers:
#     for y in items:
#         print (x, y)

# for num in range (-2,-5,-1):
#     print(num, end=", ")

# for l in "Jhon":
#     if l == 'o':
#         pass
#     print(l, end=", ")

# class Dog:
#     def walk(self):
#         return "*walking*"
#     def speak(self):
#         return "Woof!"
#
# class JackRusselTerrier(Dog):
#     def speak(self):
#         return "Arrf!"
#
# bobo = JackRusselTerrier()
# print(bobo.walk())

# def outer_fun(a,b):
#     def inner_fun(c,d):
#         return c + d
#     return inner_fun(a,b)
#
# res = outer_fun(5,10)
# print(res)

# def fun1(name,age=20):
#     print(name, age)
# fun1('Emma',25)

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


# h = Hewan('doggie',10)
# print(h.change_name_latin())
# print(h.bangun())

class Kucing(Hewan):

    nama_latin_2 = Hewan.change_name_latin()

    def bangun (self):
        return "si Kucing bangun"

    def lari (self, kecepatan):
        if self.kecepatan > 10:
            print("cepat sekali")
        else: print("lambat")

    # print(nama_latin_2)
