class Menu():
    def __init__(self):
        self._dishes = []
        self._in_order = []
    def add(self, dish):
        self._dishes.append(dish)
    def list_dishes(self):
        new_string = ''
        for dish in self._dishes:
            new_string += f"* {dish.name}: £{dish.price} \n"
        return new_string
    def add_to_order(self, to_order):
        for dish in self._dishes:
            if to_order == dish.name:
                self._in_order.append(dish)
    def view_order(self):
        if self._in_order == []:
            return ''
        total_price = sum(dish.price for dish in self._in_order)
        new_string = 'The following items are in your order:\n\n'
        for dish in self._in_order:
            new_string += f"* {dish.name}: £{dish.price} \n"
        new_string += f"\nThe total for your order is: £{total_price}"
        return new_string
    def submit_order(self):
        self._in_order = []