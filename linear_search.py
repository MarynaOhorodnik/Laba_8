'''
Лінійний алгоритм пошуку
'''
import numpy as np
import random
import timeit
while True:
    while True:
        try:
            N, x = int(input('Розмірність масиву: ')), int(input('Шуканий елемент: '))
            break
        except ValueError:
            print('Неправильний запис')
    A = np.zeros(N, dtype=int)
    while True:
        K = input('Заповнювати елемети рандомно(r) чи вручну(v): ')
        if K == 'r':
            print('Вкажіть межі чисел:')
            while True:
                try:
                    a, b = int(input('Від: ')), int(input('До: '))
                    if a < b:
                        break
                    else:
                        print('Неправильно введені дані')
                except ValueError:
                    print('Це не число')
            for i in range(N):
                A[i] = random.randint(a, b)
            break
        elif K == 'v':
            for i in range(N):
                while True:
                    try:
                        A[i] = int(input(f'A[{i}] = '))
                        break
                    except ValueError:
                        print('Це не число')
            break
        else:
            print('Введіть v або r')
    print(A)
    n, i, count = len(A), 0, 0
    while i < n and A[i] != x:
        count += 2
        i += 1
    if i == n:
        print(f'Елемент {x} не знайдений, порівнянь було здійснено {count + 1}')
    else:
        print(
            f'Елемент {x} знайдений на позиції {i}, порівнянь було здійснено {count + 1 if i == len(A) - 1 else count + 2}')
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Час виконання алгоритму пошуку: {:.5f}'.format(t))

    answer = input('Бажаєте запустити програму ще раз? Так (+), ні (будь-що) ')
    if answer == '+':
        continue
    else:
        break
