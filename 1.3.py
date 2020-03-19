'''
Виконайте добуток двох квадратних матриць 3*3, врахуйте розмірність.
Результати множення елементів занесіть до нової матриці та виведіть її на екран
'''
import numpy as np
from functools import reduce
while True:
    print('Матриця A')
    n = 3
    a = np.zeros((n, n), dtype=int)  # ініціалізуємо матрицю розміром 3 на 3 нулями
    for i in range(n):  # за допомогою двох циклів заповнюємо матрицю
        for j in range(n):
            while True:  # перевіряємо щоб користувач вводив лише цифри
                try:
                    a[i, j] = int(input(f'A[{i},{j}] = '))
                    break
                except ValueError:
                    print('Error')
    print('Матриця B')
    b = np.zeros((n, n), dtype=int)  # ініціалізуємо матрицю розміром 3 на 3 нулями
    for i in range(n):  # за допомогою двох циклів заповнюємо матрицю
        for j in range(n):
            while True:  # перевіряємо щоб користувач вводив лише цифри
                try:
                    b[i, j] = int(input(f'B[{i},{j}] = '))
                    break
                except ValueError:
                    print('Error')
    print('Матриця A', a, 'Матриця B', b, sep='\n')
    m = np.zeros((n, n), dtype=int)  # ініціалізуємо матрицю нулями, в яку будемо вносити результат множення
    for i in range(n):
        for j in range(n):
            m[i, j] = reduce(lambda x, y: x + y, a[i, ...] * b[..., j])  # перемножуємо відповідні стопці матриць a та b та додаємо
    print('Матриця A * B', m, sep='\n')  # виводимо результат

    answer = input('Do you want to run the program again? Yes (+), No (anything) ')
    if answer == '+':
        continue
    else:
        break

