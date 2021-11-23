title = {
    'Неклеточные':
        {
        'Вирусы': 100,
        'Фаги': 56
        },
    'Клеточные':
        {
        'Прокариоты':
            {
               'Бактерии': 325,
               'Архибактерии': 99
            },
        'Эукариоты':
            {
             'Растения': 788,
             'Животные':
                 {
                  'Одноклеточные': 257,
                  'Многоклеточные': 358
                 },
                'Грибы': 256,
                'Лишайники': 73
            }
        }
}


def req(sl,search):

    if search in sl.keys():
        the_values = list(sl[search].values())
        for the_values in sl[search].values():
            if type(the_values) == dict:
                return sum(list(the_values.values()))






    for n in sl.values():
        if type(n) == dict:
            rec = req(n, search)
            if rec != None:
                return rec




print(req(title, input('Enter \n ')))