# Дана переменная, в которой хранится словарь, содержащий гео-метки для каждого
# пользователя (пример структуры данных приведен ниже). Вам необходимо написать
# программу, которая выведет на экран множество уникальных гео-меток всех
# пользователей.


ids = {'user1': [213, 213, 213, 15, 213],
    'user2': [54, 54, 119, 119, 119],
    'user3': [213, 98, 98, 35]}

def geo_signs():
    new_ids = []
    for el in ids.values():
        new_ids += el
    print(set(new_ids))
# geo_signs()



# Дана переменная, в которой хранится список поисковых запросов пользователя
# (пример структуры данных приведен ниже, но запросы потенциально могут быть любые).
# Вам необходимо написать программу, которая выведет на экран распределение
# количества слов в запросах в требуемом виде.


queries = ['смотреть сериалы онлайн', 'новости спорта', 'афиша кино',
    'курс доллара', 'сериалы этим летом', 'курс по питону', 'сериалы про спорт', '',
    'рептилоиды живут под Петропаловкой', '', 'очень странные дела']

def count_words():
    count_el_in_queries = len(queries)
    split_list = {}
    for el in queries:
        word_len = len(el.split())
        word_value = split_list.get(word_len)
        word_value = word_value + 1 if word_value else 1
        split_list.update({word_len: word_value})
    for i_key, i_value in split_list.items():
         print(f'Поисковых запросов, содержащих {i_key} слов(а): {round(i_value/
                                                count_el_in_queries*100, 2)}% ')
# count_words()



# Дана переменная, в которой хранится информация о затратах и доходе
# рекламных кампаний по различным источникам. Необходимо дополнить исходную структуру
# показателем ROI, который рассчитаем по формуле: ((revenue / cost) - 1) * 100


results = {'vk': {'revenue': 103, 'cost': 98},
    'yandex': {'revenue': 179, 'cost': 153},
    'facebook': {'revenue': 103, 'cost': 110},
    'adwords': {'revenue': 35, 'cost': 34},
    'twitter': {'revenue': 11, 'cost': 24},
}
def adv_company():
    for indicator in results.values():
        roi_value =  round(((indicator['revenue']/indicator['cost']) - 1)*100, 2)
        indicator.setdefault('ROI', roi_value)
    print(sorted(results.items()))
# adv_company()



# Дана переменная, в которой хранится статистика рекламных каналов по объемам продаж
# (пример структуры данных приведен ниже). Напишите программу, которая возвращает
# название канала с максимальным объемом продаж.

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99,
    'email': 42, 'ok': 98}

def statistics():
    max_stat = 0
    max_key = ''
    for k, v in stats.items():
        if max_stat < v:
            max_stat = v
            max_key = k
    print(max_key)
# statistics()



# Дан список произвольной длины. Необходимо написать код, который на основе
# исходного списка составит словарь такого уровня вложенности, какова длина
# исхондого списка.

test_ex = ['2018-01-01', 'yandex', 'cpc', 100]


def dict_from_list(my_list):
    pre_dict = {}
    for el in reversed(my_list):
        if not pre_dict:
            pre_dict = el
        else:
            pre_dict = {el: pre_dict}
    return pre_dict
print (dict_from_list(test_ex))



def check_dz():
    number_dz = int(input('Введите номер задания:'))
    match number_dz:
        case 1:
            geo_signs()
        case 2:
            count_words()
        case 3:
            adv_company()
        case 4:
            statistics()
        case 5:
            dict_from_list()
# check_dz()



