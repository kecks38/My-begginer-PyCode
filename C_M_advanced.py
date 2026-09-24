import json
try:
    users_info = []
    with open("contacts.json", "r", encoding="utf8") as f:
        users_info = json.load(f)
except(FileNotFoundError):
        print("Файл не найден")

while True:
    print("1 - Добавить номер")
    print("2 - Все контакты")
    print("3 - Удалить контакт")
    print("4 - Выход")
    print()
    action = int(input("Что вы хотите сделать? "))
    print()
    if action == 1:
        print("Введите имя контакта и номер")
        username1 = (input("Имя: "))
        userphone1 = (input("Телефон: "))
        new_contact = {"name" : username1, "phone" : userphone1}
        users_info.append(new_contact)

        with open("contacts.json", "w", encoding="utf8") as f:
            json.dump(users_info, f, indent=4, ensure_ascii=False)

    elif action == 2:
        for index, contact in enumerate(users_info):
            print(f"Номер: {index} {contact}")
            print()
        if not users_info  :
            print("Контакты не найдены")
            continue

            
    elif action == 3:
        if not users_info:
            print("Список контактов пуст ")
            continue
        else:
            for index, contact in enumerate(users_info):
                    print(f"Номер: {index} {contact}")
            try:
                delite_contact = int(input("Выберите индекс контакта который хотите удалить: "))
                users_info.pop(delite_contact)    
            except(IndexError, ValueError):
                print("Введите корректные данные")

        with open("contacts.json", "w", encoding="utf8") as f:
            json.dump(users_info, f, indent=4, ensure_ascii=False)

    elif action == 4:
        print("Выход из программы...")
        break

    else:
        print("Ошибка ввода, выберите правильное действие.""\nПрограмма будет начата заново.")