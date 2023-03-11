name = input('Enter Your Name please:> ')
python_score = float(input('Enter your python Score:> '))
django_score = float(input('Enter your django score:> '))
pygame_score = float(input('Enter your pygame score:> '))

# ave = (python_score + django_score + pygame_score) / 3
# print(f"{name}'s average is : {ave}")

# with list

scores = []
scores.append(python_score)
scores.append(django_score)
scores.append(pygame_score)

ave = sum(scores)/3
print(f"{name}'s average is : {ave:.2f}")
