goods = []
header = {'Название': '', 'количество': '',  'Ед': '', 'Стоимось': ''}
body =  {'Название': [], 'количество': [],  'Ед': [], 'Стоимось': []}
num = 0
while True:
    if input('Для выхода нажмите Q, для продолжения Enter: ').upper() =='Q':
        break
    num += 1
    for f in header.keys():
        prop = input(f'Введите значение параметра {f} - ')
        header[f] = int(prop) if (f == 'Стоимось' or f == 'количество') else prop
        body[f].append(header[f])
    goods.append((num, header))
    print("f\nСтруктура Товаров\n{goods}")
    print("f\nТекущая аналитика по товарам:\n{'*' * 30}")
    for key, value in body.items():
        print(f"{key[:25]:>30}:{value}")
    print('*' * 30)
    break

