# Словари


person = {
    'name': 'John',
    'age': 18,
    'last_name': 'Johnson',
    # 'addres': 'Durand, Michigan(MI), 48429 Mount Street',
    'addres': {
        'city': 'Durand',
        'state': 'Michigan(MI)',
        'zip': 48429,
        'street': 'Mount Street'
    },
    'phone': None,
}


print(
    'person: ', person,
)
# result:
# person:  {'name': 'John', 'age': 18, 'last_name': 'Johnson', 'addres': {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}, 'phone': None}


# Получение значений
print(
    'name: ', person.get('name'),
    '\nname: ', person['name'],
    # 'email: ', person['email'],
    '\nemail: ', person.get('email', None),
)
# result:
# name:  John 
# name:  John
# email:  None


# Получение только значений словаря
print(
    person.values()
)
# result:
# dict_values(['John', 18, 'Johnson', {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}, None])


# Получить только ключи
print(
    person.keys()
)
# result:
# dict_keys(['name', 'age', 'last_name', 'addres', 'phone'])


# Получение пар ключ-значение
print(
    person.items()
)
# result:
# dict_items([('name', 'John'), ('age', 18), ('last_name', 'Johnson'), ('addres', {'city': 'Durand', 'state': 'Michigan(MI)', 'zip': 48429, 'street': 'Mount Street'}), ('phone', None)]) 


for k in person.items():
    print(k)

for k in person.values():
    print(k)

# Добавление значения
person['birthday'] = '2005-06-14'
print(
    'person', person
)

person.setdefault('birthday', '2005-06-14')
print(
    'person', person
)

