def read_file():
    with open(path_file, 'r', encoding='UTF-8') as f:
        for line in f:
            print(line.strip())

def add_file():
    with open(path_file, 'a', encoding='UTF-8') as f:
        f.writelines('\n' + input('Введите имя, фамилию, отчество и телефон нового контакта: '))

def find_file():
    find_p = input('Поиск контактов, введите ключевое слово принадлежащее\
контакту, что бы его найти. Для того что бы посмотреть список всех \
контактов нажмите "Enter" оставив строку поиска пустой: ')
    if find_p == '':
        print('Список всех контактов:')
        read_file()
    else:
        with open(path_file, 'r', encoding='UTF-8') as f:
            for line in f:
                if find_p.casefold() in line.casefold():
                    print(line)

def delete_file():
    find_p = input('Введите ключевое слово принадлежащее\
контакту, что бы его найти: ')
    with open(path_file, 'w', encoding='UTF-8') as f:
        for line in f:
            if find_p.casefold() not in line.casefold():
                f.write(line)

def change_file():
    find_p = input('Введите ключевое слово принадлежащее\
контакту, что бы его найти: ')
    change_p = input(f'Введите контакт на который вы хотите заменить  {find_p}: ')
    with open(path_file, 'w', encoding='UTF-8') as f:
        for line in f:
            if find_p.casefold() not in line.casefold():
                f.write(line)
            else:
                f.writelines('\n' + change_p)

path_file = r'Home_work_python/Telephonebook.txt'

while True:
    m_chose = input(f'Меню\nНайти контакт или посмотреть все существующие контакты ==> 1\
                        \nДобавить новый контакт ==> 2\
                        \nУдалить контакт ==> 3\
                        \nИзменить или удалить контакт ==> 4\
                        \nВведите команду для выбора советующего пункта: ')
    if m_chose == '1':
        find_file()
    elif m_chose == '2':
        add_file()
    elif m_chose == '3':
        delete_file()
    elif m_chose == '4':
        change_file()
    else:
        print('Вы ввели неверное значение')
        print('Для возвращения в меню нажмите запустите программу ещё раз')



# Иванов Иван Иванович +79999999999
# Петров Петр петрович +78888888888
# Денисов Денис Денисович +77777777777
# Александров Александр Александрович +75555555555