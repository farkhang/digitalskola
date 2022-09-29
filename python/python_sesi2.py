## Shorthand
# x = 4
# # if x == 3: print('x adalah 3') -- kalau cuma 1 statement
# print ('x adalah 3') if x == 3 else print('x bukan 3')

## User Input
# name = input('Please insert your name: ')
# age = int(input('Please insert your age: '))
#
# legal_status = 'dewasa' if age > 18 else 'belom dewasa'
# print(legal_status)

## Nested If
# price = 50
# quantity = 5
# amount = price*quantity
# if amount > 100:
#     if amount > 500:
#         print("Amount is greater than 500")
#     else:
#         if amount < 500 and amount > 400:
#             print("Amount is")
#         elif amount < 500 and amount > 300:
#             print("Amount is between 300 and 500")
#         else:
#             print("Amount is between 200 and 500")
#
# elif amount == 100:
#     print("Amount is 100")
# else:
#     print("Amount is less than 100")

## While Loop
# sum = 0
# i = 1
# while i <= 10:
#     sum = sum + i
#     i = i+1 # update counter or i += 1
#     print(i, sum)
# '''print the sum'''
# print("The sum is", sum)

## Continue
# x = 3
# while x <= 10:
#     x += 1
#     if x > 7: # klo false lanjut ke print klo true continue ke loop berikutnya skip print
#         continue
#     print(x)

## Break
# i = 1
# while i < 100:
#     print(i)
#     if i == 7: # klo true loop diputus (break) klo false lanjut ke line berikutnya
#         break
#     i += 1

## For Loop List
# numbers = [6, 5, 3, 11]
# sum = 0
# for val in numbers:
#     sum = sum + val
#     print(sum)
# print(f'the sum is {sum}')

## For Loop Dictionary
# dict_1 = {"name": "farkhan", "age": 29, "job": "martech"}
# for key in dict_1.keys():
#     print(key)
# for value in dict_1.values():
#     print(value)
# for key, value in dict_1.items():
#     print(key, "-->", value)

## Range
# print(list(range(10)))
# print(list(range(4,10)))
# print(list(range(1,10,2)))

## Comprehension
buah = 'apple'
# list = []
#touc
# for huruf in buah:
#     list.append(huruf)
#
# print(list)

list = [huruf for huruf in buah] # code diatas dipersimple
print(list)

## Conditional Comprehension
# numbers = []
#
# for i in range(1,20):
#     if i % 2 == 0:
#         numbers.append(i)
# print(numbers)

numbers = [i for i in range(1,20) if i % 2 == 0]
print(numbers)