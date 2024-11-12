#Словарь
my_dict={'Хлеб':'55р.', 'Молоко':'78р.','Чай':'225р.','Кофе':'389р.'}
print(my_dict)
print(my_dict['Чай'])
print(my_dict.get('Кетчуп'))
my_dict.update({'Вода':'32р.','Печенье':'114р.'})
a=my_dict.pop('Молоко')
print(a)
print(my_dict)
#Множество
my_set={'Подушка','Навлочка','Одеяло','Подушка','Пододеяльник','Одеяло', True, 2024}
print(my_set)
my_set.add(1997)
my_set.add('Простыня')
my_set.discard('Пододеяльник')
print(my_set)