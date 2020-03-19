'''
Виведіть на екран елементи лінійного масиву (заданий користувачем) у зворотньому порядку
'''
import numpy as np
while True:
    while True:  # перевіряємо щоб користувач вводив лише цифри
        try:
            n = int(input('Введіть кількість елементів: '))
            break
        except ValueError:
            print('Error')
    m = np.zeros(n, dtype=int)  # ініціалізуємо лінійний масив нулями такого розміру, який ввів користувач
    for i in range(n):  # циклічно заповнюємо масив
        while True:  # перевіряємо, щоб користувач вводив лише цифри
            try:
                m[i] = int(input(f'A[{i + 1}] - '))
                break
            except ValueError:
                print('Error')
    print(m)
    for j in range(1, n + 1):  # виводимо циклічно елементи за від'ємними індексами, тобто в зворотньому порядку
        print(m[-j])

    answer = input('Do you want to run the program again? Yes (+), No (anything) ')
    if answer == '+':
        continue
    else:
        break