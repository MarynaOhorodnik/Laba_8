'''
Тестові варіанти для бінарного алгоритму пошуку
'''
import numpy as np
test = [[np.array([1, 3, 4, 7, 8, 9, 11, 13, 15]), 7], [np.array([1, 3, 4, 5, 6, 7, 9, 11, 19, 20]), 8],\
        [np.array([0, 1, 2, 4, 5, 7, 9, 10, 12, 13, 16, 18, 19, 20, 22, 27, 30]), 20],\
        [np.array([1, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 16, 18, 19, 20, 23, 28, 30]), 2]]
c = 0
for A, x in test:
    c += 1
    print('{:>30}{:<}'.format('Test №', c))
    print(f'{A}, шуканий елемент: {x}')
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
