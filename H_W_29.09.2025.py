import random

string = input('Введите данные: ')
x1 = string.upper() # Все буквы большие
x2 = string.lower() # Все буквы маленькие

# Вероятность того или другого варианта
pu_pu_pu = [x1, x2]

x3 = random.choice(pu_pu_pu)

if str(string) == str(string)[::-1]:
    print(x3, '- это палиндром')
else:
    print(x3, '- это не палиндром')
"""
# надо было
string = input('Введите данные: ').strip().lover()
if string == str(string)[::-1]:
    print(x3, '- это палиндром')
else:
    print(x3, '- это не палиндром')
"""