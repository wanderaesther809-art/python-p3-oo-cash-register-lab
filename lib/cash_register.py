#!/usr/bin/env python3
class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.discount = discount
        self.items = []
        self.last_transaction = 0.0

    def add_item(self, title, price, quantity=1):
        """Add item(s) to the register."""
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        self.items.extend([title] * quantity)

    def apply_discount(self):
        """Apply discount if it exists and print message."""
        if self.discount > 0:
            self.total -= (self.discount / 100) * self.total
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Remove the last transaction from the total."""
        self.total -= self.last_transaction
        self.last_transaction = 0.0
