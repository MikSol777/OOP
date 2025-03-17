from src.Product import Product

class Category:
    category_count = 0
    products_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.products_count = len(self.__products)
        Category.category_count += 1
        Category.products_count += len(products)

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты класса Product или его наследников")
        self.__products.append(product)

    @property
    def products(self):
        return self.__products

    @property
    def first_product(self):
        return f"{self.name}, {self.__products[0].price} руб. Остаток: {self.__products[0].quantity} шт."

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
