# Дана переменная, в которой хранится слово из латинских букв. Напишите код,
# который выводит на экран:
# среднюю букву, если число букв в слове нечетное;
# две средних буквы, если число букв четное.


def middle_letter():
    word = 'python'
    # word = 'pythons'
    if len(word) % 2 == 0:
        print(word[(len(word)//2 - 1):(len(word)//2 + 1)])
    else:
        print(word[len(word)//2])
# middle_letter()



# Напишите программу, которая последовательно запрашивает у пользователя числа
# (по одному за раз) и после первого нуля выводит сумму всех ранее введенных чисел.


def inter_number():
    number_list = 0
    while True:
        number = int(input('Введите число:'))
        if number != 0:
            number_list += number
        else:
            break
    print(number_list)
# inter_number()




# Мы делаем MVP dating-сервиса, и у нас есть список парней и девушек.
# Выдвигаем гипотезу: лучшие рекомендации мы получим, если просто отсортируем имена
# по алфавиту и познакомим людей с одинаковыми индексами после сортировки!
# Но мы не будем никого знакомить, если кто-то может остаться без пары.


def dating():
    boys = ['Antony', 'Nick', 'Ivan', 'Bart', 'Rick']
    girls = ['Kate', 'Emma', 'Rose', 'Anna', 'Kimberly']
    sorted_boys = sorted(boys)
    sorted_girls = sorted(girls)
    pairs = list(zip(sorted_boys, sorted_girls))
    if len(sorted_boys) == len(sorted_girls):
            print(f'Идеальные пары:', pairs)
    else:
        print('Внимание, кто-то может остаться без пары!')

# dating()



# У нас есть список, содержащий информацию о среднедневной температуре в Фаренгейтах
# за произвольный период по странам (структура данных в примере).
# Необходимо написать код, который рассчитает среднюю температуру за период в
# Цельсиях(!) для каждой страны.


import statistics

def country_temp_c():
    countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
    ]
    new_list = []
    for country in countries_temperature:
        temp = country[1]
        temp_in_c = round((statistics.mean(temp) - 32)/1.8, 1)
        new_list.append([country[0], temp_in_c])
    print(new_list)
# country_temp_c()




def check_dz():
    number_dz = int(input('Введите номер задания:'))
    match number_dz:
        case 1:
            middle_letter()
        case 2:
            inter_number()
        case 3:
            dating()
        case 4:
            country_temp_c()
check_dz()

