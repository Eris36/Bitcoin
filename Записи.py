
#--------F строка ---------
name = 'Семен'
mid_name = 'Семенович'
balansce = 32.56

text = f'Дорогой {name} {mid_name}, баланс вашего лицевого счета составляем {balansce} руб'

print (text)

gender = {   #Cловарь м и ж
    'm': 'Дорогой',
    'f': 'Дорогая'
}

gender_op = {   #Cловарь м и ж
    'meg': 'Мегафона',
    'mts': 'МТСа'
}

a = [
    ['Семен', 'Семенов', 32.56, 'm', 'meg'],
    ['Тамара', 'Ивановна', 342.56, 'f', 'mts'],
    ['Михаил', 'Анатольевич', 322.56, 'm', 'meg']
]
for name, mid_name,balansce, g, op in a:
    text = f'{gender[g]} {name} {mid_name}, баланс вашего {gender_op[op]} счета:  ' \
        f'составляем {balansce} руб'
    print (text)



#C:\Users\Name\djangogirls> myvenv\Scripts\activate   Запустить виртуальное окружеие
#python manage.py makemigrations bitbd           Сделать изменения в нашей модели
#python manage.py migrate bitbd