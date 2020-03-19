'''
Виведіть на екран транспоновану матрицю 3*3 (початкова матриця задана користувачем)
'''
import numpy as np
while True:
    n = 3
    m = np.zeros((n, n), dtype=int)  # ініціалізуємо матрицю розміром 3 на 3 нулями
    for i in range(n):  # за допомогою двох циклів заповнюємо матрицю
        for j in range(n):
            while True:
                try:
                    m[i, j] = int(input(f'A[{i},{j}] = '))
                    break
                except ValueError:
                    print('Error')
    print(m)
    for i in range(n):
        for j in range(n):
            if i > j or i == j:  # міняємо елементи місцями, але застосовуємо тільки для елементів нижньої трикутної матриці
                m[i, j], m[j, i] = m[j, i], m[i, j]
    print('Транспонована матриця:', m, sep='\n')

    answer = input('Do you want to run the program again? Yes (+), No (anything) ')
    if answer == '+':
        continue
    else:
        break