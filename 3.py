while True:
    u_month = input('Введите номер месяца от 1 до 12:')
    if u_month.isdigit() and 0<= int(u_month) <= 12:
        season_1 = ['Зима', 'Весна', 'Лето', 'Осень', 'Зима']
        print(f'Время Года - {season_1[int(u_month) // 3]}\n')
        break
    else:
        print('Ошибка')



