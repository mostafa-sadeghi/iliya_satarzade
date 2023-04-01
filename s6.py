# a = int(input('enter a number'))
# b = int(input('enter a number'))

# if a > b:
#     print(f'{a} > {b}')
# elif a == b:
#     print(f'{a} = {b}')
# else:
#     print(f'{a} < {b}')

'''
name

age

< 8  kid
8 - 12 junior
12 18  teenager
> 18 adult

'''


# a = 2
# b = 3

# if a == b:
#     print("a is equal to be")

# if a != b:
#     print(' a is not eq to b')

# a = 3
# b = 3

# if a >= b:
#     print("1")
# if a <= b:
#     print("2")
# if a >= b:
#     print("1")
# elif a <= b:
#     print("2")


# a = True

# if a:
#     print("some thing")

# a = False
# if a:
#     print("another")


# a = True
# b = False

# if a and b:
#     print("and")

# if a or b:
#     print("or")

# a = 3
# b = 3

# c = a == b
# print(c)


# if 1:
#     print("one")

# if 0:
#     print("zero")

# if -1:
#     print("-1")


# name = ''

# if name:
#     print("hello")

# name = 'ali'

# if name:
#     print("hhhhhhhh")


USERNAME = 'admin'
PASSWORD = 'root'


user_name = input('enter user name: ')
password = input('enter password: ')

if user_name and password:
    if user_name == USERNAME and password == PASSWORD:
        print("success")
        print("account is valid")

    else:
        print("account is not valid")
else:
    print("you must enter user name and password")
