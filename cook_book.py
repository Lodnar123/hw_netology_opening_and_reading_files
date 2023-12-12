# Функция для создании  списка покупок.
def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            ingrid = cook_book[dish]
            for ing in ingrid:
                name = ing['ingredient_name']
                measure = ing['measure']
                quantity = int(ing['quantity'])*person_count
                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure':measure, 'quantity':quantity}
    return shop_list
#Функция закрытия файла.
def is_closed(file_):
    """
    Функция принимает объект файл и проверяет его состояние
    """
    if file_.closed:
        print('Файл закрыт')
    else:
        print('Файл открыт')    

cook_book = {}
with open('recipes.txt', encoding='utf-8') as f:
    data = f.read().split('\n\n')
    for food in data:
        key = food.split('\n')[0]
        values = food.split('\n')[2:]
        ingridients = []
        for value in values:
            ingridient = {}
            value = value.split('|')
            ingridient['ingredient_name'] = value[0]
            ingridient['quantity'] = value[1]
            ingridient['measure'] = value[2]
            ingridients.append(ingridient)
        cook_book[key] = ingridients

is_closed(f)

print(cook_book)

dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

result = get_shop_list_by_dishes(dishes, person_count)
print(result)