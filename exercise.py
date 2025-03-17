'''
1. Запрашивает у пользователя ввод строки, состоящей из слов, разделенных пробелами.\
2. Подсчитывает, сколько раз встречается каждое слово.
3. Выводит результат в отсортированном порядке (по убыванию количества вхождений).

Пример работы:
Введите строку: яблоко банан яблоко апельсин банан яблоко
Результат:
яблоко: 3
банан: 2
апельсин: 1
'''

text = input('Введите строку: ')

text_list = text.split()
text_unique = set(text_list)
text_counts = {text: text_list.count(text) for text in text_unique}

print(f'{text_unique}: {text_counts}, end=" "')