#!/usr/bin/env python3


#  A cash register code that :

#  - you can add items and prices to 
#  -- by using the add_item method

#  - you can remove items and prices from
#  -- by using the remove_item method

#  - you can calculate the discount
#  -- by using the calculate_discount method

#  - Keep track of what's been added to it
#  -- by using the get_items method

#  - Void the last transaction
#  -- by using the void_transaction method

#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=None):
        self.discount = discount
        self.total = total
        self.items = items if items is not None else []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction_amount = price * quantity
        self.total += self.last_transaction_amount
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        discount_amount = (self.total * self.discount) / 100.0
        self.total -= discount_amount
        self.apply_discount_success_message()
        return self.total

    def apply_discount_success_message(self):
        if self.discount != 0:
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            last_item_price = self.last_transaction_amount
            self.total -= last_item_price
            self.last_transaction_amount = 0
            self.items.pop()
        else:
            print("No transactions to void.")