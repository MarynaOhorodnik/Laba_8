'''
Алгоритм лінійного пошуку підрядка
'''
import string as str
import random
import timeit
while True:
    while True:
        K = input('Заповнювати елемети рандомно(r) чи вручну(v): ')
        if K == 'v':
            text, pattern = input('Text: '), input('Pattern: ')
            break
        elif K == 'r':
            text = ''.join(random.choice(str.ascii_lowercase) for i in range(int(input('Length of text: '))))
            pattern = ''.join(random.choice(str.ascii_lowercase) for i in range(int(input('Length of pattern: '))))
            print(f'Text: {text}, \nPattern: {pattern}')
            break
        else:
            print('Введіть v або r.')
    i, j, count = -1, 0, 0
    while j < len(pattern) and i < (len(text) - len(pattern)):
        j = 0
        i += 1
        count += 4
        while j < len(pattern) and pattern[j] == text[i + j]:
            j += 1
            count += 2
    if j == len(pattern):
        print(f'Підрядок знайдений в позиції {i}, порівнянь було здійснено {count}')
    else:
        print(f'Елемент не знайдений, порівнянь було здійснено {count}')
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print('Час виконання алгоритму пошуку: {:.5f}'.format(t))

    answer = input('Бажаєте запустити програму ще раз? Так (+), ні (будь-що) ')
    if answer == '+':
        continue
    else:
        break
