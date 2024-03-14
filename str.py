# Операции со стоками

s = "Lorem \tipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."
#\t - пробел
#\n - с новой строки

print(s)

#первый символ
print(s[0])

# длина строки
print('len str: ', len(s))

# последний символ строки
print(s[len(s)-1])
print(s[-1])

# срез из 10 первых символов
print(s[:10])

# срез с 10 по 20 символ
print (s[10:20])

# срез с 10 по 20 каждый третий символ
print(s[10:20:2])

# каждый третий символ в строке
print(s[::3])

# не сработает, тк строка является неизменяемым типом данных
# s[0] = 'lllflfl'

# конкатенация строк
s1 = '11111' + 'hedgehog'
print(s1)

# замена первого символа в строке s на строку s1
s = s1 + s[1:]
print(s)

# создание строки из списка по разделителю ' ' (пробел)
l = ['Lorem', 'Ipsum', 'is', 'simly', 'dummy', 'of']
s2 = ' '.join(l)
print(s2)

# создание списка из строки с разделителем  'a'
l2 = s.split('a')
print(l2)

# удаление пробела слева и справа
s3 = ' Hello, John! '
print(s3,'len: ', len(s3))
s3 = s3.lstrip()
print(s3,'len: ', len(s3))
s3 = s3.rstrip()
print(s3,'len: ', len(s3))

# изменить регистр
s4 = 'nam libero'
print(s4.upper())
s5 = 'LOREM IPSUM'
print(s5.lower())


s6 = 'lorem ipsum dolor sit amet, consectetur adipiscing elit'
print(s6)
s7 = s6[:1]
s7 = s7.upper()
s8 = s7 + s6[1:]
print(s8)


# форматирование строк

n = 105
s7_0 = 'str 1'
s7_1 = 'str 2'
s7 = f'Lorem ipsum: {s7_0}. {s7_1}. {8+8}, {str(n)}'
print(s7)

s7_2 = 'Lorem ipsum: {}. {}'.format(s7_0, s7_1)
print(s7_2)