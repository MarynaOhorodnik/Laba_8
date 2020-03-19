'''
Тестові варіанти для алгоритму лінійного пошуку підрядка
'''
test = [['Коронавірус захопив майже весь світ', 'світ'], ['Бобер на березі з бобренятами бублики пік', 'бобренятка'],\
        ['Водовоз віз воду з водопроводу.', 'віз'], ['Жовтий жук купив жилет', 'жакет']]
c = 0
for text, pattern in test:
    c += 1
    print('{:>30}{:<}'.format('Test №', c))
    print(f'Text: {text} \nPattern: {pattern}')
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
        print(f'Підрядок не знайдений, порівнянь було здійснено {count}')