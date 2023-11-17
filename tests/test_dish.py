from lib.dish import *

"""
Correctly stores given dish name
"""
def test_stores_name():
    fried_rice = Dish('Egg Fried Rice', '5')
    assert fried_rice.name == 'Egg Fried Rice'

"""
Correctly stores given dish price
"""
def test_stores_price():
    fried_rice = Dish('Egg Fried Rice', 5)
    assert fried_rice.price == 5

"""
If dish changes price
can update price of dish
"""
def test_updates_price():
    fried_rice = Dish('Egg Fried Rice', 5)
    fried_rice.update_price(6)
    assert fried_rice.price == 6