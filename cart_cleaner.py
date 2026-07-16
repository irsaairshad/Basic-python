class CartItem:
    def __init__(self, item_name, quantity, price):
        self.item_name = item_name
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price


if __name__ == "__main__":
    cart = [
        CartItem("Shampoo", 2, 350),
        CartItem("Notebook", 5, 60),
        CartItem("Water Bottle", 0, 200),
    ]

    active_items = [item for item in cart if item.quantity > 0]
    total_cost = sum(item.total_price() for item in active_items)

    print("Total cart balance:", total_cost)
