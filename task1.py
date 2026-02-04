'''
САМАЯ ПОПУЛЯРНАЯ БУКВА

Дана строка из любых символов. Вам необходимо вывести букву, которая встречается чаще всего.
Буквы могут быть любого алфавита. Задание выполняется без учета регистра.
Оформить в виде функции most_wanted_letter. Аргументом функции является строка с
любым содержимым. Функция должна возвращать фразу с буквой или фразу с предупреждением, что букв здесь нет.
'''

def most_wanted_letter(text):
    # Приводим строку к нижнему регистру
    text_lower = text.lower()

    # Собираем только буквы (любого алфавита)
    letters = []
    for char in text_lower:
        if char.isalpha():
            letters.append(char)

    # Если букв нет — возвращаем предупреждение
    if len(letters) == 0:
        return "There are no letters in the string"

    # Подсчитываем частоту каждой буквы
    letter_counts = {}
    for letter in letters:
        if letter in letter_counts:
            letter_counts[letter] = letter_counts[letter] + 1
        else:
            letter_counts[letter] = 1

    # Находим букву с максимальной частотой
    most_common = ""
    max_count = 0

    for letter in letter_counts:
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]
            most_common = letter

    return "The most popular letter is " + most_common


# Тестирование
print(most_wanted_letter("......HeLlo......"))
print(most_wanted_letter("String ssss ttAAds TTTTTTT"))
print(most_wanted_letter("!@#$%^&*(*&^%$#@@#$%^&*DFGBQQQQQQQQqqqrrrrrrrr"))
print(most_wanted_letter("!@#$%^&*543234%^&*%$#@345677^%$#@#$%^&"))
print(most_wanted_letter("....пррррривет..."))
print(most_wanted_letter("....Tschüüüüüüüss!..."))

# Вывод:
# The most popular letter is l
# The most popular letter is t
# The most popular letter is q
# There are no letters in the string
# The most popular letter is р
# The most popular letter is ü

'''
Пояснение к коду:

text.lower() — приводим всё к нижнему регистру, чтобы не учитывать регистр
char.isalpha() — метод проверяет, является ли символ буквой
(работает с любым алфавитом: латиница, кириллица и т.д.)
Словарь letter_counts — хранит количество вхождений каждой буквы
'''
