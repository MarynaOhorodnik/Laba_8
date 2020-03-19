'''
У матриці 4*4, що задана користувачем замініть всі від’ємні елементи на 0
'''
import numpy as np
while True:
    n = 4
    m = np.zeros((n, n), dtype=int)  # ініціалізуємо матрицю розміром 4 на 4 нулями
    for i in range(n):  # за допомогою двох циклів заповнюємо матрицю
        for j in range(n):
            while True:  # перевіряємо щоб користувач вводив лише цифри
                try:
                    m[i, j] = int(input(f'A[{i},{j}] = '))
                    break
                except ValueError:
                    print('Error')
    print(m)
    for i in range(n):
        for j in range(n):
            if m[i, j] < 0:  # перевіряємо чи елемент від'ємний, тоді замінюємо його на нуль
                m[i, j] = 0
    print(m)  # виводимо перетворену матрицю

    answer = input('Do you want to run the program again? Yes (+), No (anything) ')
    if answer == '+':
        continue
    else:
        break