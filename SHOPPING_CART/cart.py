class Cart:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_item(self, name, price, quantity):
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def remove_item(self, name):
        self.items = [item for item in self.items if item["name"] != name]

    def get_total(self):
        return sum(item["price"] * item["quantity"] for item in self.items)

    def apply_discount(self, percent):
        total = self.get_total()
        return total - (total * percent / 100)

    def get_item_count(self):
        return len(self.items)

    def clear_cart(self):
        self.items.clear()

    def show_items(self):
        if self.is_empty():
            return "Cart is empty"
        lines = []
        for item in self.items:
            line = f"{item['name']} - Qty: {item['quantity']} - Price: {item['price']} each"
            lines.append(line)
        return "\n".join(lines)
    
    def total_quantity(self):
        return sum(item["quantity"] for item in self.items)