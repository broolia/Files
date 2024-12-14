
def parse_recipes(filename="recipes.txt"):
    
    cook_book = {}
    
    with open(filename, "r", encoding="utf-8") as f:
        while True:
            recipe_name = f.readline().strip()
            if not recipe_name:
                break  
            
            ingredient_count = int(f.readline().strip())
            ingredients = []
            for _ in range(ingredient_count):
                line = f.readline().strip()
                parts = line.split("|")
                ingredient_name = parts[0].strip()
                quantity = int(parts[1].strip())
                measure = parts[2].strip()
                ingredients.append({
                    "ingredient_name": ingredient_name,
                    "quantity": quantity,
                    "measure": measure
                })
            cook_book[recipe_name] = ingredients
            f.readline() 

    return cook_book




cook_book = (parse_recipes())
# print(cook_book)

def get_shop_list_by_dishes(dishes, person_count,cook_book):

    shop_list = {}
    for dish_name in dishes:
        if dish_name not in cook_book:
            print(f"Error: Dish '{dish_name}' not found in the cookbook.")
            return {}  
            
        for ingredient in cook_book[dish_name]:
            ingredient_name = ingredient["ingredient_name"]
            quantity = ingredient["quantity"] * person_count
            measure = ingredient["measure"]
                
            if ingredient_name in shop_list:
               shop_list[ingredient_name]['quantity'] += quantity
            else:
              shop_list[ingredient_name] = {'quantity': quantity, 'measure': measure}

    return shop_list
shop_list1 = get_shop_list_by_dishes(['Омлет'], 3, cook_book)
print(shop_list1)
shop_list2 = get_shop_list_by_dishes(['Запеченный картофель', 'Утка по-пекински'], 2, cook_book)
print(shop_list2)
shop_list3 = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3, cook_book) 
print(shop_list3)


