def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(7, 'black', False)
print_params(33, 'борьщевик')
print_params(b = 'катушка')
print_params(b = 17)
print_params(c = [1, 2, 3])


values_list = [458, 'мох', True]
values_dict = {'a': 45, 'b': 'крот', 'c': False}
print_params(*values_list)
print_params(**values_dict)



values_list_2 = [9, 'ноутбук']
print_params(*values_list_2, 42)