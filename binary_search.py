'''
Алгоритм бінарного пошуку
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
    A.sort()
    print(A)
    L, R, k, count = 0, len(A) - 1, 0, 0
    Flag = False
    while L <= R and not Flag:
        k = (L + R) // 2
        count += 1
        if A[k] == x:
            count += 1
            Flag = True
        elif A[k] < x:
            L = k + 1
            count += 2
        else:
            R = k - 1
    if not Flag:
        print(f'Елемент {x} не знайдено, порівнянь було здійснено {count + 1}')
    else:
        print(f'Елемент {x} знайдений на позиції {k}, порівнянь було здійснено {count + 1}')
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Час виконання алгоритму пошуку: {:.5f}'.format(t))

    answer = input('Бажаєте запустити програму ще раз? Так (+), ні (будь-що) ')
    if answer == '+':
        continue
    else:
        break
