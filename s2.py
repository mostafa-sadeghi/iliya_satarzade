# string = 'abcdefghi'
# print(string[0:3])
# print(string[:])
# print(string[:3])
# print(string[::2])
# print("last chararcter is:", string[-1])

# message = "he said \"don't do that\""
# print(message)

# message = "welcome to our pyrhon class. \nwe are going to learn every thong aboyt python. \npython from zero to hero!"
# print(message)
# message = """welcome to our pyrhon class.
# we are going to learn every thong aboyt python.
# python from zero to hero!"""
# print(message)
# message = '''welcome to our pyrhon class.
# we are going to learn every thong aboyt python.
# python from zero to hero!'''
# print(message)
# message = '''he said "don't do that"'''
# print(message)


# name = input('enter student name: ')
# # print("name type is:", type(name))
# family = input('enter student family: ')
# age = int(input('enter student age: '))
# # print("name type is:", type(age))

# # message = name + " " + family + " is " + str(age) + " years old"
# # print(message)
# # fstring
# message = f"{name} {family} is {age} years old."
# print(message)


# number1 = int(input('enter first number: '))
# number2 = int(input('enter second number: '))

# result = number1 + number2

# print("result is :", result)
# print(f"{number1} + {number2} = {result}")

# exercise 1 : سه عدد را از ورودی بگیر و عبارات زیر را به همین صورت با همین اعداد محاسبه کن . پرینت
#  2 + 3*4 = 14
#  4 + 8/2 = 8

n1 = int(input('enter first number: '))
n2 = int(input('enter second number: '))
n3 = int(input('enter third number: '))

s1 = f'{n1} + {n2} * {n3} = {n1 + n2 * n3}'
s2 = f'{n1} + {n2} / {n3} = {n1 + n2 / n3}'
print(s1)
# print(s2)
print(int(input('enter first number')) +
      int(input('enter second number')) * int(input('enter third number')))
