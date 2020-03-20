'''
Тестові варіанти для лінійного алгоритму пошуку
'''
import timeit
import numpy as np
test = [[np.array([5, 8, 9, 3, 7, 6, 4, 2, 1]), 7], [np.array([1, 7, 6, 9, 10, 3, 4, 5]), 8], \
        [np.array([1, 18, 15, 7, 13, 11, 6, 2, 0, 9, 11, 10, 17, 15, 20, 3, 4, 5]), 20], \
        [np.array([9, 7, 14, 3, 4, 17, 20, 19, 11, 8, 3, 15, 14, 4, 1, 6, 16, 13]), 2]]
c = 0
for A, x in test:
    c += 1
    print('{:>30}{:<}'.format('Test №', c))
    print(f'{A}, шуканий елемент: {x}')
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
