from shop.project.drink import Drink
from shop.project.food import Food
from shop.project.product import Product

class ProductRepository:
    def __init__(self):
        self.products: list = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name:str):
        product = [p for p in self.products if p.name == product_name][0]
        return product

    def remove(self, product_name:str):
        try:
            product = [p for p in self.products if p.name == product_name][0]
            self.products.remove(product)
        except IndexError:
            pass

    def __repr__(self):
        result = ""
        for product in self.products:
            result += f"{product.name}: {product.quantity}\n"
        return result[:1]


food = Food("apple")
drink = Drink("water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

