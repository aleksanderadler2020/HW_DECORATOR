from pprint import pprint
from datetime import datetime


def logger(path):
    def _logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with (open(path, 'a') as log_file):
                log_line = 'Время вызова: ' + str(datetime.now())
                log_line += ' Наименование метода: ' + str(old_function.__name__) + '('
                if len(args) > 0:
                    log_line += str(args)
                if len(kwargs) > 0:
                    log_line += str(kwargs)
                log_line += ') Результат функции: ' + str(result) + '\n'
                log_file.write(log_line)
            return result

        return new_function

    return _logger


cook_book = {}
# Задача №1


@logger('Task_1.log')
def task1():
    with open('recipes.txt') as f:
        while True:
            dish = f.readline().replace('\n', '')
            if dish == '':  # Конец файла
                break
            ing_count = int(f.readline())
            cook_book[dish] = []
            for i in range(ing_count):
                ing = f.readline().split('|')
                cook_book[dish].append({'ingredient_name': ing[0], 'quantity': int(ing[1].replace(' ', '')),
                                        'measure': ing[2].replace('\n', '')})
            f.readline()

    print('Задача №1')
    pprint(cook_book)
    print()


task1()


@logger('Task_2.log')
def get_shop_list_by_dishes(dishes, person_count):
    ingridients = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            if ing['ingredient_name'] in ingridients.keys():
                ingridients[ing['ingredient_name']]['quantity'] += ing['quantity'] * person_count
            else:
                ingridients[ing['ingredient_name']] = {'measure': ing['measure'],
                                                       'quantity': ing['quantity'] * person_count}
    return ingridients


print('Задача №2')
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()

file_line_size = {}
with open('1.txt') as f:
    file_line_size['1.txt'] = len(f.read().split('\n'))
with open('2.txt') as f:
    file_line_size['2.txt'] = len(f.read().split('\n'))
with open('3.txt') as f:
    file_line_size['3.txt'] = len(f.read().split('\n'))


@logger('Task_3.log')
def task_3():
    sort_file_list = sorted(file_line_size.items(), key=lambda item: item[1])

    with open('result.txt', 'w') as wf:
        for file_name, file_line_count in sort_file_list:
            wf.writelines(file_name)
            wf.writelines('\n')
            wf.writelines(str(file_line_count))
            wf.writelines('\n')
            with open(file_name, 'r') as rf:
                wf.write(rf.read())
            wf.writelines('\n')

    print('Задача №3')
    with open('result.txt') as rf:
        print(rf.read())


task_3()


class context_manager:
    @logger('Task_4.log')
    def __enter__(self):
        print('Вошли')

    @logger('Task_4.log')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Вышли')


test = context_manager()
print('Задача №4')
with test:
    pass
