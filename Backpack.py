# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

LIMIT = 10
list_of_things = {"спальник": 4, "еда": 3, "вода": 1, "горелка": 3, "аптечка": 1, "фонарик": 0.5,
                  "компас": 0.1, "карта": 0.2, "навигатор": 0.5, "дождевик": 1, "спички": 0,
                  "посуда": 2, "коврик": 1.5, "павербанк": 0.5, "запасная одежда": 1.5,
                  "предметы гигиены": 1, "репеллент": 0.1}

sorted_list_of_things = sorted(list_of_things.items(), key=lambda item: item[1])
# print(sorted_list_of_things)
weight = 0
result_list = {}
for thing, value in sorted_list_of_things:
    weight = weight + value
    if weight < LIMIT:
        result_list[thing] = value
print(result_list)


weight = 0
result_list = {}
for thing, value in list_of_things.items():
    # print(thing, value)
    if(weight + value <= LIMIT):
        weight = weight + value
        result_list[thing] = value

print(f"Вес:  {round(weight, 2)}, \n"
      f"{result_list}")


