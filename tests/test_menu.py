from lib.menu import *
from unittest.mock import Mock

"""
Initially
contains no dishes
"""
def test_no_dishes_at_first():
    menu = Menu()
    assert menu.list_dishes() == ''


"""
After several dishes are added
can return list of dishes and their respective prices
"""
def test_can_return_dish_names_and_prices():
    menu = Menu()
    dish_1 = Mock()
    dish_1.name = 'Egg Fried Rice'
    dish_1.price = 5
    dish_2 = Mock()
    dish_2.name = 'Taiwanese Braised Pork Belly'
    dish_2.price = 12
    dish_3 = Mock()
    dish_3.name = 'Three Cup Sauce Chicken'
    dish_3.price = 8
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    assert menu.list_dishes() == '* Egg Fried Rice: £5 \n* Taiwanese Braised Pork Belly: £12 \n* Three Cup Sauce Chicken: £8 \n'

"""
User can order several dishes
and view order to see total price
"""
def test_can_order_dishes_and_view_order():
    menu = Menu()
    dish_1 = Mock()
    dish_1.name = 'Egg Fried Rice'
    dish_1.price = 5
    dish_2 = Mock()
    dish_2.name = 'Taiwanese Braised Pork Belly'
    dish_2.price = 12
    dish_3 = Mock()
    dish_3.name = 'Three Cup Sauce Chicken'
    dish_3.price = 8
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    menu.add_to_order("Egg Fried Rice")
    menu.add_to_order("Three Cup Sauce Chicken")
    assert menu.view_order() == "The following items are in your order:\n\n* Egg Fried Rice: £5 \n* Three Cup Sauce Chicken: £8 \n\nThe total for your order is: £13"

"""
Submitting order
clears order list
"""
def test_submitting_order_clears_order_list():
    menu = Menu()
    dish_1 = Mock()
    dish_1.name = 'Egg Fried Rice'
    dish_1.price = 5
    dish_2 = Mock()
    dish_2.name = 'Taiwanese Braised Pork Belly'
    dish_2.price = 12
    dish_3 = Mock()
    dish_3.name = 'Three Cup Sauce Chicken'
    dish_3.price = 8
    menu.add(dish_1)
    menu.add(dish_2)
    menu.add(dish_3)
    menu.add_to_order("Egg Fried Rice")
    menu.add_to_order("Three Cup Sauce Chicken")
    menu.submit_order()
    assert menu.view_order() == ''