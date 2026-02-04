'''
МИНИМУМ

Дан двумерный массив из чисел. Необходимо найти номер строки и столбца с минимальными суммами.
Оформить в виде функции minimum, где массив передается как аргумент.
Функция должна вернуть массив из двух элементов: номер строки с минимальной суммой и номер столбца с минимальной суммой.
'''

def minimum(matrix):
    # Количество строк и столбцов
    rows_count = len(matrix)
    cols_count = len(matrix[0])

    # Находим суммы всех строк
    row_sums = []
    for i in range(rows_count):
        row_sum = 0
        for j in range(cols_count):
            row_sum = row_sum + matrix[i][j]
        row_sums.append(row_sum)

    # Находим суммы всех столбцов
    col_sums = []
    for j in range(cols_count):
        col_sum = 0
        for i in range(rows_count):
            col_sum = col_sum + matrix[i][j]
        col_sums.append(col_sum)

    # Находим номер строки с минимальной суммой
    min_row_index = 0
    min_row_sum = row_sums[0]

    for i in range(rows_count):
        if row_sums[i] < min_row_sum:
            min_row_sum = row_sums[i]
            min_row_index = i

    # Находим номер столбца с минимальной суммой
    min_col_index = 0
    min_col_sum = col_sums[0]

    for j in range(cols_count):
        if col_sums[j] < min_col_sum:
            min_col_sum = col_sums[j]
            min_col_index = j

    return [min_row_index, min_col_index]


# Тестирование
print(minimum([[7, 2, 7, 2, 8],
               [2, 9, 4, 1, 7],
               [3, 8, 6, 2, 4],
               [2, 5, 2, 9, 1],
               [6, 6, 5, 4, 5]]))

print(minimum([[-7, -2, -7, -2, -8],
               [-2, -9, -4, -1, -7],
               [-3, -8, -6, -2, -4],
               [-2, -5, -2, -9, -1],
               [-6, -6, -5, -4, -5]]))

# Вывод:
# [3, 3]
# [0, 1]

'''
Пояснение к коду:

Суммы строк — внешний цикл по строкам (i), внутренний по столбцам (j), суммируем элементы каждой строки
Суммы столбцов — внешний цикл по столбцам (j), внутренний по строкам (i), суммируем элементы каждого столбца
Поиск минимума строки — проходим по списку row_sums, запоминаем индекс с наименьшей суммой
Поиск минимума столбца — аналогично для col_sums
'''
