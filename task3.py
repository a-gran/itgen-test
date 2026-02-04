'''
УЧЕНИКИ И ПРЕДМЕТЫ

Для решения этой задачи воспользуйтесь словарями. Программа запрашивает количество учеников в классе,
а затем имя ученика и предметы (через пробел), которые он изучает.

Добавьте функции:
show_all, которая будет выводить содержимое словаря с учениками и предметами, отсортированное по убыванию (ключ – имя ученика),
student_for_sub, которая принимает имя ученика и возвращает список предметов, которые он изучает,
sub_for_students, которая принимает предмет и возвращает список учеников, которые его изучают.
'''


def show_all():
    # Получаем список имён
    names = []
    for name in students:
        names.append(name)

    # Сортируем по убыванию
    names.sort(reverse=True)

    # Выводим в отсортированном порядке
    for name in names:
        print(name + ": " + str(students[name]))


def student_for_sub(name):
    # Проверяем, есть ли студент с таким именем
    if name in students:
        return students[name]
    else:
        return "There are no students with this name."


def sub_for_students(subject):
    # Ищем всех студентов, изучающих этот предмет
    result = []

    for name in students:
        subjects_list = students[name]

        # Проверяем, есть ли предмет в списке
        for subj in subjects_list:
            if subj == subject:
                result.append(name)
                break

    # Если никто не изучает этот предмет
    if len(result) == 0:
        return "There are no matching students."

    return result


# Словарь для хранения данных
students = {}

# Ввод данных
n = int(input("Write number of students: "))

for i in range(n):
    name = input("Name of " + str(i + 1) + " student: ")
    subjects = input("Subjects of " + str(i + 1) + " student: ")

    # Разбиваем строку предметов на список
    subjects_list = subjects.split(" ")

    # Добавляем в словарь
    students[name] = subjects_list


# Тестирование

'''
Write number of students: 3
Name of 1 student: John
Subjects of 1 student: math physics astronomy
Name of 2 student: Jane
Subjects of 2 student: physics astronomy chemistry
Name of 3 student: Jonathan
Subjects of 3 student: math programming physics
'''

print('\t')
show_all()
print('\t')
print(student_for_sub('John'))
print('\t')
print(sub_for_students('math'))
print('\t')
print(student_for_sub('Jack'))
print('\t')
print(sub_for_students('biology'))
print('\t')
print(sub_for_students('astronomy'))


'''
Пояснение к коду:

students — словарь, где ключ = имя студента, значение = список предметов
show_all() — собираем имена в список, сортируем по убыванию (reverse=True), выводим
student_for_sub(name) — проверяем наличие ключа в словаре, возвращаем список предметов или сообщение об ошибке
sub_for_students(subject) — проходим по всем студентам, ищем предмет в их списках, собираем подходящих в результат
'''





