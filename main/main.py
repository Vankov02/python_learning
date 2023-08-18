# number = 6
#
# print("Мое число: ", number)
# del number
#
# number1 = 10
# print("Мое число: ", number1)
#
# digit = 1.0001
# word = "good time"
# print(word, digit)
#
# bool_per = False
#print(word + " " + str(bool_per))

# number1 = int(input("Введите первое число: ")) #либо при вводе числа преобразуем в тип данных int при
# number2 = int(input("Введите второе число: ")) # помощи вспомогательной функции "int"
#
# rez = print("A + B = ", int(number1) + int(number2)) # либо здесь каждый раз переменную
# rez1 = print("A - B = ", int(number1) - int(number2)) # преобразовываем в целочисленный тип
# rez2 = print("A * B = ", int(number1) * int(number2))
# rez3 = print("A / B = ", int(number1) / int(number2))
# rez4 = print("A // B = ", number1 // number2) # деление с округлением до целого
# rez4 = print("A ** B = ", number1 ** number2) # возведение в степень
#
# word = "Привет, Лох"
# rez5 = print(word * 3)
#
# word = 45 # переопределяем тип данных в пер
#______________________________________________
# if..else operators
# user_data = int(input("Введите число: "))
#
# if user_data > 5 and user_data > 10:
#     print("число больше!")
# elif user_data == 3:
#     print("YOU LOSER!")
# else:
#     print("You LUCKY!")
#
# if user_data > 5 or user_data > 10:
#     print("число больше!")
# elif user_data == 3:
#     print("YOU LOSER!")
# else:
#     print("You LUCKY!")
#________________________________________________________________
# Тернанрный оператор(тоже самое что if..else только записывается в одну строку)
# data = input()
#
# number = 5 if data == "Five" else 0
# print(number)
#_______________________________________________________________

# for i in range(2,6,2):
#     print(i,end=' ')
#___________________________________________________
# Программа поиска буквы с помощью цикла FOR
# string = input("Введите слово: ")
# word = input("Введите искомую букву: ")
# num = 0
# for i in string:
#     num = num + 1
#     if i == word:
#         print("Буква найдена! Позиция: ",num)
#         signal = True
# if signal != True:
#     print("Увы, такой буквы нет в этом слове!")
#_________________________________________________________

# списки и работа с ними
#nums = [] #создание пустого списка

# nums = [3, 9, 10, 11, 102, 39, 0]
# for i in range(len(nums)): # с помощью len обращаемся к индексам и перебираем их
#     if (nums[i] % 3) == 0:
#         nums[i] = 100
#     else:
#         nums[i] = 1000
# print(nums)

# методы для списков
# append - помогает добавить элемент в конец списка
# insert(i,ch) - помгает установить значение ch в определенный индекс i списка
# extend([элементы списка]) - помогает поместить набор элементов в конец списка
# sort() - сортирует массив по возростанию
# reverse() - выводит элементы в обратном порядке
# pop(i) - удаляет элемент с индексом i(если  pop без параментра то удаляется последний эелемент)
# remove(elem) - удаляет элемент значения elem из списка
# clear - удаляет все эелементы в списке
# count(elem) - подсчитывает количество элементов со значением elem
#len(название_списка) - подсчитывает длину списка(количество элементов)

# Код программы, где пользователь сам задает размер списка и вводит данные в него
# n = int(input("Введите количество людей: "))
# guest_list = []
# i = 0
# while i < n:
#     string = "Введите имя " + str(i+1) + "-го гостя: "
#     guest_list.append(input(string))
#     i += 1
# print(guest_list)


# def print_to_file(name_of_file):
#     try:
#         with open(name_of_file, 'r') as file: #r- reopen
#             content = file.read() # чтение файла
#             print(content)
#     except FileNotFoundError: #исключение отсутствия найденого файлa
#         print(f"Файл '{name_of_file}' не найден.")
#     except Exception as e:
#         print(f"Ошибка: {e}")
#
# file_to_read = input('Введите название файла: ')
# print_to_file(file_to_read)

#использование срезов в списке
# list = [1,2,3,4,5,6]
# print(list[1]) # вывести элемент в данном случае второй
# print(list[3:5]) # вывести элемент в данном случае с четвертого по шестой(не включая шестой)
# print(list[1:5:2])# вывести элемент в данном случае со второго по шестой с шагом 2(не включая шестой)
# print(list[1:-2:2]) #аналогично предыдущему(индекс -2 означает по второй элемент с конца)
# print(list[::-1]) #вывод списка в обратном порядке
#___________________________________________________________________________________________________
#Кортежи - аналог списков, отличие в том что значения кортежей нельзя изменять(они своего рода константы), но при этом
#занимают меньше места. Используются чаще для передачи каких либо данных.
# nametuple = (1,2,True,'word', 4.7, 4) #создание кортежа
# othertuple = 1,4, 'round', 6.6
# print(othertuple)
# number = (5) # не воспринимается кортежем
# print(number)
# number1 = (5,) # уже воспринимается как кортеж
# print(number1)
#
# for i in nametuple:
#     print(i, end=' ') #вывести все элементы кортежа используя цикл
# print('\n')
#
# #преобразование списка в кортеж с помошью метода tuple
# nums = [1,2,4,7,5,9]
# tuple_nums = tuple(nums)
# print(tuple_nums)
# #преобразование строки в кортеж с посимвольными элементами
# string_tuple = 'Hello world'
# print(tuple(string_tuple))
#___________________________________________________________________________________
#Словари
example = {3:'True'} #создание словаря(в данном случае 3- ключ, True - значение, которое присвоено данному ключу)
#в качестве ключа можно использовать любые типы данных, также кортежи, но списки - НЕЛЬЗЯ
print(example[3])

country = {'code': 'RU', 'name' : 'Russia', 'population': 144}
#аналогичный способ создания словаря(здесь в качестве ключа можно использовать только букв обозначения)
country1 = dict(code = 'RU', name = 'Russia', population = 144)
print(country1)
print(country.items())#выводит словарь в виде списка, где каждый элемент это пара ключ-значение в виде кортежа

#цикл для перебора ключей в словаре
for key in country:
    print(key)

#цикл для перебора ключей и значений в словаре
for key, value in country.items():
    print(key,value)

#методы для работы со словарями
print(country.get('code')) #get('key') - получить значение ключа key
# country.clear() - очистить словарь полностью
#country.pop(key) #- удалить элемент по ключу key
#country.popitem() #удалить последний элемент словаря
#print(country.keys()) #получить все ключи словаря
#print(country.values()) #получить все значения словаря
#country['code'] = 'None' #изменение значения ключа code на значение None(то бишь было значение у code = RU, теперь code = None)

person = {
            'user1' : {
                        'name' : 'Ivan',
                        'lastname' : 'Maslennikov',
                        'age' : 15,
                        'address' : ['Altay region','Biysk', 'Kutuzova', '33', '55'],
                        'hobby' : {'football' : 7, 'swimming' : 7, 'music' : 2}
            }
        }

print(person['user1']['address'][:3])
#______________________________________________________________________________________________