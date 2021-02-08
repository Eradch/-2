m_list = [9, 8, 7, 6, 5, 3, 3, 1]
new_n = int(input('Введите новый рейтинг в виде натурального числа'))
i = 0

for n in m_list:
    if new_n <= n:
      i +=1
m_list.insert(i, new_n)
print(m_list)

