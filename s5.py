# my_list = [1, 2, 3, 4, 5, 'a', [1, [1, 2]], 'something']
# print(my_list[6])
# print(my_list[6][0])
# print(my_list[6][1][0])
# print(my_list[6][1][1])


# characters = ['a', 'b', 'c', 'd', 'e', 'f']
# characters.append([1,2])

# print('charcters are:', characters)

# del characters[-1]
# del characters[6]
# print(len(characters))
# del characters[len(characters)-1]
# characters.pop()
# del characters[0]
# characters.pop(0)

# print('charcters are:', characters)


names = []

name1 = input('enter a name:> ')
name2 = input('enter a name:> ')
name3 = input('enter a name:> ')

names.append(name1)
names.append(name2)
names.append(name3)

print("names:", names)
print("we want to remove second name from our list ...")
del names[1]  # names.pop(1)
print("names:", names)


# exercise :
# برنامه ای بنویسید که پنج عدد را از ورودی دریافت نماید و
# در لیستی ذخیره کند
# اولین و آخرین عضو لیست را حذف کنید
# مجموع اعداد باقی مانده در لیست را محاسبه و پرینت نمائید.
