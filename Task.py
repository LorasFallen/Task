#Импорт
import shelve
#Класс выполнения
class adressbook:

    def staticinform(self):
        self.editbook = shelve.open('book')
        self.index = (shelve.open('book'))

    def play(self):
        print('Добро пожаловать в меню книги. Здесь вы можете выбрать, что вам необходимо:')
        while True:
            try:
                menu = int(input('\nДля перехода в режим записи введите 1\nДля перехода в режим поиска записей введите 2\nДля перехода к списку всех записей введите 3\nДля удаления записей введите 4\nДля внесения изменений введите 5\nДля выхода из программы введите 0\n:'))
                if menu == 1:
                    b = bookadd()
                    b.bookAdd()
                elif menu == 2:
                    s = search()
                    s.Search()
                elif menu == 3:
                    l = llist()
                    l.Llist()
                elif menu == 4:
                    d = delete()
                    d.Delete()
                elif menu == 5:
                    e = edits()
                    e.Edits()
                elif menu == 0:
                    print('Вы завершили работу программы\nВсего доброго!')
                    break
                else:
                    print('Вы ввели некорректную команду')
                    continue
            except ValueError:
                print('Вы ввели некорректную команду')
                continue

#Класс добавления
class bookadd(adressbook):
    def bookAdd(self):
        adressbook.staticinform(self)
        while True:
            print(
                '\nВы вошли в режим записи. Для выхода в меню, введите "!"\n')
            nameadd = str(input('Введите имя: '))
            if nameadd == str('!'):
                print('Запись остановлена')
                break
            elif nameadd not in self.editbook.keys():
                descriptionadd = str(input('Введите описание: '))
                if descriptionadd == '!':
                    print('Вы вышли в меню')
                    break
                else:
                    self.editbook.update({nameadd: descriptionadd})
                    print('Запись добавлена')
            elif nameadd in self.editbook.keys():
                print('!!!Данный ключ уже записан, выберите другое название\n')
                continue
            elif nameadd == '!':
                print('Некоректное название для объекта, введите другое')
                continue
        self.editbook.close()


class search(adressbook):
    def Search(self):
        adressbook.staticinform(self)
        while True:
            searching = input('\nВведите имя объекта для начала поиска или "!" для возврата в главное меню\n:')
            if searching == "!":
                print('Вы вышли в меню')
                self.editbook.close()
                break
                #Дописать Меню
            elif searching not in self.editbook:
                print('\nЗапись с введенным именем не существует')
                continue
            elif searching in self.editbook:
                print('\nЗапись "{0}" найдена в справочнике'.format(searching))
                s = searching
                print('\nНаименование:', s, '\nОписание:', self.editbook[s])
                continue
            else:
                pass

class llist(adressbook):
    def Llist(self):
        adressbook.staticinform(self)
        while True:
            try:
                output = int(input('Для вывода всех наименований: 1\nДля вывода полной информации: 2\nДля выхода в меню:3\n:'))
                if output == 1:
                    for o in self.editbook:
                        print(o)
                elif output == 2:
                    for o in self.editbook:
                        print('\nНаименование:', o, '\nОписание:', self.editbook[o])
                elif output == 3:
                    print('Вы вышли в меню')
                    self.editbook.close()
                    break
            except ValueError:
                print('Вы ввели не правильную команду')
                continue

class delete(adressbook):
    def Delete(self):
        adressbook.staticinform(self)
        while True:
            print('Для удаления записи введите наименование записи. Для удаления всех записей введите "@del"\nДля выхода в меню введите "!"')
            dell = input('Удалить\n:')
            if dell == '!':
                print('Вы вышли в меню')
                self.editbook.close()
                break
            elif dell == "@del":
                self.editbook.clear()
                print('Все записи удалены')
            elif dell not in self.editbook:
                print('Объект "{0}" не найден в книге, введите другое наименование'.format(dell))
            elif dell in self.editbook:
                print('Объект "{0}" удалён из книги'.format(dell))
                del self.editbook[dell]
                continue

class edits(adressbook):
    def Edits(self):
        adressbook.staticinform(self)
        while True:
            print('\nДля внесения изменений введите имя записи\nДля выхода в меню введите "!"')
            search = input('Имя записи:')
            if len(search) <= 20:
                if search == '!':
                    print('\nВы вышли в меню')
                    self.editbook.close()
                    break
                elif search not in self.editbook:
                    print('\nДанной записи не существует')
                    continue
                elif search in self.editbook:
                    while True:
                        try:
                            number = int(input('\nДля изменеия имени введите 1\nДля зименения описания 2\nДля возврата назад 3\n:'))
                            if number == 1:
                                while True:
                                    name = str(input('Новое имя:'))
                                    if len(name) <= 20:
                                        self.editbook[name] = self.editbook.pop(search)
                                        break
                                    else:
                                        print('Введите длину имени менее 20 символов')
                                        continue
                                break
                            elif number == 2:
                                while True:
                                    print('Старое описание:\n{0}'.format(self.editbook[search]))
                                    discription = str(input('\nВведите новое описание\n:'))
                                    if len(discription) <= 600:
                                        self.editbook[search] = discription
                                        break
                                    elif len(discription) > 600:
                                        print('Слишком длинный текст, попробуйте ещё раз')
                                        continue
                            elif number == 3:
                                break
                            else:
                                print('\nВы ввели некорректную команду')
                                continue
                        except ValueError:
                            print('\nВы ввели некорректную команду')
                            continue
            else:
                print('\nВведите имя менее 20 символов')
                continue


a = adressbook()
a.play()
