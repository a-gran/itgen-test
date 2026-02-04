'''
КЛАССЫ И ОбъЕКТЫ

Создайте класс Autobus. Поля класса:
- название начального пункта,
- название конечного пункта,
- номер маршрута,
- время поездки.

Методы класса:
- получение информации об автобусе в читаемом виде,
- изменение и считывание полей класса (каждого по отдельности).

Далее необходимо создать программу на основе класса Autobus. Добавить методы со следующим
функционалом:
- создание списка из n объектов класса Autobus и сохранение этого списка в файл
(используйте любой удобный вам модуль для работы с файлами),
- чтение из файла списка с объектами Autobus,
- сортировка списка по убыванию номера маршрута,
- вывод информации об автобусах, которые начинаются или заканчиваются в пункте, название
которого ввел пользователь (поиск по остановке).
'''


import json


class Autobus:

    def __init__(self, number, start, destination, time):
        self.number = number
        self.start = start
        self.destination = destination
        self.time = time

    # Методы для номера маршрута
    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    # Методы для начального пункта
    def set_start(self, start):
        self.start = start

    def get_start(self):
        return self.start

    # Методы для конечного пункта
    def set_destination(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination

    # Методы для времени поездки
    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    # Информация об автобусе
    def info(self):
        print("--------------------------")
        print("Route number: " + str(self.number))
        print("Starting point: " + self.start)
        print("Destination point: " + self.destination)
        print("Travel time: " + self.time)


# Создание списка автобусов и сохранение в файл
def create_autopark():
    # Создаём локальный список
    new_autopark = []

    n = int(input("Enter the number of buses: "))

    for i in range(n):
        print("--------------------------")
        number = int(input("Enter the route number of " + str(i + 1) + " bus: "))
        start = input("Enter the starting point of " + str(i + 1) + " bus: ")
        destination = input("Enter the destination point of " + str(i + 1) + " bus: ")
        time = input("Enter the travel time of " + str(i + 1) + " bus: ")

        bus = Autobus(number, start, destination, time)
        new_autopark.append(bus)

    # Возвращаем созданный список
    return new_autopark


# Сохранение автопарка в JSON-файл
def save_to_file(autopark):
    # Преобразуем объекты в словари для сохранения
    data = []
    for bus in autopark:
        bus_dict = {
            "number": bus.number,
            "start": bus.start,
            "destination": bus.destination,
            "time": bus.time
        }
        data.append(bus_dict)

    # Записываем в файл
    file = open("autopark.json", "w")
    json.dump(data, file)
    file.close()


# Загрузка автопарка из JSON-файла
def load_from_file():
    # Создаём локальный список
    loaded_autopark = []

    # Читаем из файла
    file = open("autopark.json", "r", encoding = "utf-8")
    data = json.load(file)
    file.close()

    # Преобразуем словари обратно в объекты
    for bus_dict in data:
        bus = Autobus(
            bus_dict["number"],
            bus_dict["start"],
            bus_dict["destination"],
            bus_dict["time"]
        )
        loaded_autopark.append(bus)

    # Возвращаем готовый список
    return loaded_autopark


# Показать информацию обо всех автобусах
def show_autopark(autopark):
    print("--------------------------")
    for bus in autopark:
        print("Route number: " + str(bus.number))
        print("Starting point: " + bus.start)
        print("Destination point: " + bus.destination)
        print("Travel time: " + bus.time)
        print("--------------------------")


# Сортировка по убыванию номера маршрута
def sort_autopark(autopark):
    # Сортировка пузырьком по убыванию номера маршрута
    n = len(autopark)

    for i in range(n):
        for j in range(n - 1 - i):
            if autopark[j].number < autopark[j + 1].number:
                # Меняем местами
                temp = autopark[j]
                autopark[j] = autopark[j + 1]
                autopark[j + 1] = temp

    return autopark


# Поиск автобусов по названию остановки
def search_by_stop(autopark):
    stop = input("Enter the stop name: ")

    # Сначала собираем результаты
    results = []
    for bus in autopark:
        if bus.start == stop or bus.destination == stop:
            results.append(bus)

    # Если ничего не нашли — выходим из функции
    if len(results) == 0:
        print("No buses found for this stop.")
        return

    # Выводим найденные автобусы
    for bus in results:
        bus.info()


# Глобальный список автобусов
autopark = []


# Тестирование

bus = Autobus(422, 'Moscow', 'Minsk', '10:15')
bus.set_number(244)
print(bus.get_number())
bus.info()

print('\t')

autopark = create_autopark()
save_to_file(autopark)
autopark = load_from_file()
autopark = sort_autopark(autopark)
show_autopark(autopark)
search_by_stop(autopark)


'''
Пояснение к коду:

__init__ — конструктор класса, принимает все 4 параметра и сохраняет их в поля объекта
Геттеры (get_...) — методы для получения значения каждого поля
Сеттеры (set_...) — методы для изменения значения каждого поля
info() — выводит всю информацию об автобусе в читаемом виде с разделителями
'''


