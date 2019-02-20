from product_class import Product

class Cart:
    def __init__(self, name, container = []):
        self.name = name
        self.container = container

    def add_product(self, item_name):
        # self.add_product = item_name
        self.container.append(item_name)

    def rm_product(self, item_name):
        self.remove = item_name
        to_remove = self.container.index(self.remove)
        del self.container[to_remove]

    def add_costs(self):
        self.add_costs = []
        for item in self.container:
            self.add_costs.append(item.base_price)
        self.add_costs = float(sum(self.add_costs))

    def add_costs_tax(self):
        self.add_costs_tax = []
        for item in self.container:
            after_tax = item.base_price*(1+item.tax)
            self.add_costs_tax.append(after_tax)
        self.add_costs_tax= float(sum(self.add_costs_tax))


apple = Product("Apple", 0.85, 0.15)
cucumber = Product("Cucumber", 1.20, 0.15)
orange = Product("Orange", 1.00, 0.13)

cart1 = Cart("cart1", [apple, cucumber])

cart1.add_product(orange)

for item in cart1.container:
    print(item.name)

# cart1.rm_product(orange)
#
for item in cart1.container:
    print(item.name)

cart1.add_costs()
print(cart1.add_costs)

cart1.add_costs_tax()
print(cart1.add_costs_tax)
