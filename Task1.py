# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 1, 1, 2, 2, 3, 4, 5, 5, 5, 6, 6, 7, 8, 9]
res_list = []
for item in my_list:
    if my_list.count(item) > 1 and item not in res_list:
        res_list.append(item)

print(res_list)