# Задание 1
# Даны 2 переменных, в которых хранятся строки произвольной длины:
# phrase_1 и phrase_2. Напишите код, который проверяет какая из этих строк длиннее.
# phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
# phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
# phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
# phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'

phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
def frase_len(x, y):
    if len(x) > len(y):
        print('Фраза 1 длиннее, чем фраза 2')
    elif len(x) < len(y):
        print('Фраза 2 длиннее, чем фраза 1')
    else:
        print('Обе фразы одной длины')
# frase_len(phrase_1, phrase_2)



# Задание 2
# Дана переменная, в которой хранится число (год). Необходимо написать программу,
# которая выведет, является ли данный год високосным или обычным.


def leap_year():
    year = int(input('Введите год:'))
    if year % 4 == 0:
        print('Високосный год')
    else:
        print('Обычный год')

# leap_year()

# Задание 3
# Необходимо написать программу,
# которая будет запрашивать у пользователя месяц и дату рождения и выводить
# соответствующий знак зодиака

def sings():
    day = int(input("Введите день рождения (число): "))
    month = input("Введите месяц рождения (например: январь, март и т.д.): ").lower()
    if (month == "декабрь" and day >= 22) or (month == "январь" and day <= 19):
        sign = "Козерог"
    elif (month == "январь" and day >= 20) or (month == "февраль" and day <= 18):
        sign = "Водолей"
    elif (month == "февраль" and day >= 19) or (month == "март" and day <= 20):
        sign = "Рыбы"
    elif (month == "март" and day >= 21) or (month == "апрель" and day <= 19):
        sign = "Овен"
    elif (month == "апрель" and day >= 20) or (month == "май" and day <= 20):
        sign = "Телец"
    elif (month == "май" and day >= 21) or (month == "июнь" and day <= 20):
        sign = "Близнецы"
    elif (month == "июнь" and day >= 21) or (month == "июль" and day <= 22):
        sign = "Рак"
    elif (month == "июль" and day >= 23) or (month == "август" and day <= 22):
        sign = "Лев"
    elif (month == "август" and day >= 23) or (month == "сентябрь" and day <= 22):
        sign = "Дева"
    elif (month == "сентябрь" and day >= 23) or (month == "октябрь" and day <= 22):
        sign = "Весы"
    elif (month == "октябрь" and day >= 23) or (month == "ноябрь" and day <= 21):
        sign = "Скорпион"
    elif (month == "ноябрь" and day >= 22) or (month == "декабрь" and day <= 21):
        sign = "Стрелец"
    else:
        sign = "Неверная дата или месяц"

    print(f"Ваш знак зодиака: {sign}")

# sings()

# Задание 4
# Вам нужно написать программу для подбора упаковок по размерам товара.
# Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах):
#
# Используйте следующие правила:
#
# если каждое из трех измерений менее или равно 15 сантиметрам, то выведите на экран “Коробка №1”;
# если хотя бы одно из измерений больше 2 метров, то выводите “Упаковка для лыж”;
# если хотя бы одно из измерений больше 15 сантиметров, но менее 50 сантиметров, то выводите “Коробка №2”;
# во всех остальных случаях выводите “Коробка №3”

def box_size():
    widht = int(input('Введите ширину товара:'))
    length = int(input('Введите длину товара:'))
    height = int(input('Введите высоту товара:'))
    if widht <= 15 and length <= 15 and height <= 15:
        print('Коробка №1')
    elif widht > 200 or length > 200 or height > 200:
        print('Упаковка для лыж')
    elif 15<widht<50 or 15<length<50 or 15<height<50:
        print('Коробка №2')
    else:
        print('Коробка №3')
# box_size()
#
# Задание 5 (необязательное)
# Дана переменная, в которой хранится шестизначное число (номер проездного билета).
# Напишите программу, которая будет определять, является ли данный билет “счастливым”.
# Билет считается счастливым, если сумма первых трех цифр совпадает с суммой
# последних трех цифр номера.

def lucky_ticket():
    number = input('Введите номер билета:')
    massive = list(map(int, number))
    if sum(massive[:3]) == sum(massive[3:]):
        print('Ура! Вам достался счастливый билет!')
    else:
        print('Вам повезет в другой раз')
# lucky_ticket()

#
# **Задание 6 (необязательное)
# Напишите программу, которая сможет вычислять площади трех фигур
# (круг, треугольник и прямоугольник). Тип фигуры запрашиваем через пользовательский
# ввод, после чего делаем запрос характеристик фигуры:
#
# если пользователь выбрал круг, запрашиваем его радиус,
# если треугольник – длины трех его сторон;
# если прямоугольник – длины двух его сторон.
import math
def area_figure():
    type_f = input('Введите тип фигуры:').lower()
    if type_f == 'круг':
        r = int(input('Введите радиус фигуры:'))
        print('Площадь = ', math.pi*r**2)
    elif type_f == 'прямоугольник':
        side_a = int(input('Введите длину фигуры:'))
        side_b = int(input('Введите ширину фигуры:'))
        print('Площадь = ', side_a*side_b)
    elif type_f == 'треугольник':
        side_c = int(input('Введите длину первой стороны фигуры:'))
        side_d = int(input('Введите длину второй стороны фигуры:'))
        side_e = int(input('Введите длину третьей стороны фигуры:'))
        print('Площадь = ', math.sqrt(((side_c+side_d+side_e)/2)*(((side_c+side_d+side_e)/2)-side_c)*(((side_c+side_d+side_e)/2)-side_d)*(((side_c+side_d+side_e)/2)-side_e)))
# area_figure()


def check_dz():
    number_dz = int(input('Введите номер задания:'))
    match number_dz:
        case 1:
            frase_len(phrase_1, phrase_2)
        case 2:
            leap_year()
        case 3:
            sings()
        case 4:
            box_size()
        case 5:
            lucky_ticket()
        case 6:
            area_figure()
check_dz()