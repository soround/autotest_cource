# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
def find_three_most_expensive_purchases(filename):
    return 1


three_most_expensive_purchases = find_three_most_expensive_purchases('./test_file/task_3.txt')

assert three_most_expensive_purchases == 202346
