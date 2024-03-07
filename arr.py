# списки

a = []

# добавление элемента в конец списка
a.append(1)
a.append(2)

print(
        'list:', a
)

# длина списка
print(
    'len:', len(a)
)

# получение элемента по индексу
print(
    'first element:', a[0]
)

# создание последовательности
b = list(range(5, 20, 2))
print(
    'b:', b
)

# max and min
c = [2, 2, 2, 2, 5, 12, 8, -4, 55]
print(
    'max:', max(c),
    'min:', min(c)
)

# сумма
print(
    'sum:', sum(c)
)

# сортировка от А-Я
c.sort
print(
    'sort:', c
)

# сортировка от Я-А
c.sort(reverse=True)
print(
    'sort:', c
)

# кол-во элементов по значению
print(
    'count:', c.count(2)
)

# удаление
del c[0]
print(
    'c:', c
)

# удаление по значению
c.remove(2)
print(
    'c:', c
)

# 
d = ['яблоки', 'дыни', 'груши', 'клубника']
e = d.pop()
print(
    'd:', d,
    'e:', e
)

# копирование
f = d.copy()
f.append('арбуз')
print(
    'd:', d,
    '\nf:', f
)