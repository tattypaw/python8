import json

def help():
    print("Команды для управления справочником:","0 - помощь", "1 - начало работы","2 - конец работы","3 - просмотр контактов","4 - добавление контакта","5 - поиск контакта","6 - удаление контакта","7 - редактирование контакта","8 - сохранение контактов","9 - Выход",sep="\n")
    return

def load():
    with open("telephones.json", 'r', encoding="utf-8") as fh:
        telephones_data = json.load(fh)
        if len(telephones_data)!=0 : print('Справочник был успешно загружен')
        else : print("Справочник пуст, перейдите к добавлению контакта")
    return telephones_data

def save():
    with open("telephones.json", 'w', encoding="utf-8") as fh:
        fh.write(json.dumps(telephones_data, ensure_ascii=False))
    print("Наш справочник успешно сохранен в файле telephones.json")

def view():
        i = 1
        for item in telephones_data:
            user = item
            print(i, user['firstName'] +' ' + user['lastName'], sep='\n')
            print(user['address']['streetAddress'],user['address']['city'],user['address']['postalCode'])
            print(user['phoneNumbers'][0])
            print(user['phoneNumbers'][1])
            print(user['birthday'])
            print(user['email'])
            i+=1
        return

def addEl():
        data={}
        data['firstName'] = input("Введите имя: ")
        data['lastName'] = input("Введите фамилию: ")
        print("Введите адрес:")
        address = {}
        address['streetAddress'] = input("Улица и номер дома: ")
        address['city'] = input("Населенный пункт: ")
        address['postalCode'] = input("Индекс: ")
        data['address'] = address
        phoneNumbers = [0,1]
        phoneNumbers[0]=input("Введите номер телефона 1: ")
        phoneNumbers[1]=input("Введите номер телефона 2: ")
        data['phoneNumbers'] = phoneNumbers
        data['birthday'] = input("День рождения: ")
        data['email'] = input("e-mail: ")
        telephones_data.append(data)
        print("Контакт был успешно добавлен в коллекцию! ")
        return

def search(f):
        i = 0
        findArr = []
        for item in telephones_data:
            flag = False
            for value in item.values() :
                if f in value: flag = True
            if flag :
                i += 1
                findArr.append(item)
        print()
        print(f'Найдено {i} вхождений')
        return findArr

def removeEl(f):
    i = 0
    for item in telephones_data:
        flag = False
        for value in item.values() :
            if f in value: flag = True
        if flag :
            i += 1
            telephones_data.remove(item)
    print()
    print(f'Найдено {i} вхождений')
    return i 

def editEl(f,p):
    i = f-1
    keys = ["firstName", "lastName", "streetAddress", "city", "postalCode", "phoneNumbers1","phoneNumbers2", "birthday", "email"]
    if 1< p-1 < 5:
        telephones_data[i]['address'][keys[p-1]] = input("Введите новое значение")
    elif 4<p-1<7:
        if p==5: telephones_data[i]['phoneNumbers'][0] = input("Введите новое значение")
        else: telephones_data[i]['phoneNumbers'][0] = input("Введите новое значение")
    else:
        telephones_data[i][keys[p-1]] = input("Введите новое значение")
    view()

help()
telephones_data = load()
while True:
    command = input("Введите команду ")
    if command =="1":
        print("Система готова к работе ")
    elif command=="2":
        save()
        print("Конец работы. Заходите ещё, будем рады! ")
        break
    elif command=="3":
        print('Текущий список контактов: ')
        view()
    elif command=="4":
        addEl()
    elif command=="0":
        help()
    elif command=="5":
        f = input("Введите поисковый контент: ")
        arrRes = []
        arrRes.append(search(f))
        for item in arrRes:
             print(item)
    elif command=="6":
        f = input("Какой контакт надо удалить? ")
        n = removeEl(f)
        if n == 1: 
            print(f'{n} контакт был удален')
        elif 1<n<=4:
            print(f'{n} контакта было удалено')
        else:
            print(f'{n} контактов были удалены')
    elif command=="7":
        view()
        f = int(input("Введите номер редактируемого контакта: "))
        if 0<f<=len(telephones_data):
            print("Какой параметр будем редактировать?","1 - Имя;","2 - Фамилия;","3 - улица и номер дома; ","4 - населенный пункт; ","5 - почтовый индекс; ","6 - мобильный телефон; ","7 - рабочий телефон; ","8 - датарождения; ","9 - электронная почта", sep = "\n")
            p = int(input("Ваш выбор: "))
            if 0<p<10: 
                editEl(f,p)
            else:
                print("Такого параметра нет")
        else:
            print("Такого контакта нет")

    elif command=="8":
        save()
    elif command=="9":
        print("Если не сохранить изменения, после выхода они будут отменены. Сохранить справочник? 1 - да; 2 - нет")
        i = input("Ваш выбор: ")
        if i == "1": 
            save()
        else:
            print("Изменения отменены.")
        print("До свидания! Сеанс окончен.")
        break
    else:
        print("Неопознанная команда. Просьба изучить мануал через /help ")