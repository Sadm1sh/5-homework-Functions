#Сортировщик
documents = [
    {"type": "Паспорт", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "Счёт-фактура", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "Страховой полис", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
def get_name(docs, number):
    doc = list(filter(lambda d: d["number"] == number, docs))
    if doc:
        return f"Имя владельца: {doc[0]['name']}"
    else:
        return "Документа с таким номером нет в базе"

def get_shelf(dirs, numbers):
    for key, value in dirs.items():
        if numbers in value:
            return f"Документ лежит на {key} полке"
        else:
          return "Документа с данным номером нет на полках"

def get_list(docs):
    for doc in docs:
        print (doc["type"], doc["number"], doc["name"])

def add_docs(docs, direct, shelf, type, numbers, name):
    doc = {"type": type.capitalize(), "number": numbers.capitalize() , "name": name}
    docs.append(doc)
    direct[shelf].append(doc["number"])
    return "Документ добавлен"

def dell_docs(direct, numbers, docs):
    for key, value in direct.items():
        if numbers in value:
            inx = value.index(numbers)
            del value[inx]
            print(value)
    docum = next((i for i, x in enumerate(docs) if x["number"] == numbers), None)
    if docum:
        del documents[docum]

def add_shilf(dirs, newkey):
    if newkey in dirs.keys():
        return "Полка с таким названием уже существует!!!"
    else:
        directories[newkey]= list()
        return "Полка успешно создана"

def move_docs(numbers, direct, shelf):
    if shelf not in direct :
        return print("Полки стаким номером не существует")
    for key, value in direct.items():
        if numbers in value:
            value.remove(numbers)
            direct[shelf].append(numbers)
            return print(f"Документ успешно перемещён на {shelf} полку")
    return print("Документа с таким номером не найдено")

while True:
    print("Доступные команды: p, s, l, a, d, m, as, q")
    command = input("Введите команду: ")

    if command == "p":
        number = input("Введите номер документа: ")
        print (get_name(documents, number))

    elif command == "s":
        number = input("Введите номер документа: ")
        print(get_shelf(directories, number))

    elif command == "l":
        get_list(documents)

    elif command == "a":
        shelf = input("Введите номер полки куда положить документ: ")
        if shelf in directories.keys():
            type = input("Введите название документа: ")
            number = input("Введите номер документа: ")
            name = input("Введите имя владельца: ")
            add_docs(documents, directories, shelf, type, number, name)
        else:
            print("Такой полки не существует")

    elif command == "d":
        number = input("Введите номер документа который нужно удалить: ")
        dell_docs(directories, number, documents)

    elif command == "m":
        num = input("Введите номер документа который нужно переместить: ")
        shilf = input("Введите номер полки на которую переместить документ: ")
        move_docs(num,directories , shilf)

    elif command == "as":
        newkey = input("Введите номер новой полки: ")
        add_shilf(directories, newkey)


    elif command == "q":
        break