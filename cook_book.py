
from pprint import pprint
​
def dict_collector(file_path):
    with open(file_path, 'r') as file_work:
        menu = {}
        for line in file_work:
            dish_name = line[:-1]
            counter = file_work.readline().strip()
            list_of_ingridient = []
            for i in range(int(counter)):
                ingridient = file_work.readline().strip().split(' | ')
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure'])
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                list_of_ingridient.append(dish_items)
                cook_book = {dish_name: list_of_ingridient}
                menu.update(cook_book)
            file_work.readline()
      ​
    return(menu)
  ​
dict_collector('cookbook.txt')
​
def get_shop_list_by_dishes(dishes, persons=int):
    menu = dict_collector('cookbook.txt')
    print('Наше меню выглядит вот так:\n\n')
    pprint(menu)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                  ​
                else:
                    shopping_list.update(items_list)
          ​
        print(f"\nДля приготовления блюд на {persons} человек нам необходимо купить:\n")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")
  ​
  ​
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)