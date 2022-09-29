## User Defined Function
# def square (value:int):
#     """
#     Pangkat 2
#     :param value:
#     :return:
#     """
#     new_value = value ** 2
#     # print(new_value)
#     return new_value
#
# hasil = square(5)
# print(hasil)

# def perkalian(angka1, angka2:int):
#     """
#     Perkalian antara dua angka
#     :param angka1:
#     :param angka2:
#     :return:
#     """
#     new_value = angka1 * angka2
#     return new_value
#
# if __name__ == '__main__':
#     hasil_2 = perkalian("2",4)
#     print(hasil_2)

# def return_multiple(angka1:int, angka2:int):
#     """
#     Fungsi untuk mengembalikan 2 angka
#     :param angka1:
#     :param angka2:
#     :return:
#     """
#     perkalian = angka1 * angka2
#     penambahan = angka1 + angka2
#
#     multiple_value = (perkalian, penambahan)
#     return multiple_value
#
# hasil_3 = return_multiple(2,3)
# print(hasil_3[0])

def greet(*names):
    for name in names:
        print(f'Hello {name}')

greet('angga','farkhan')