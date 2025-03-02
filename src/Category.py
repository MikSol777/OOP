class Category:
    category_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.products_count = len(self.__products)
        Category.category_count += 1

    def add_product(self, product):
        self.__products.append(product)

    @property
    def products(self):
        return self.__products

    @property
    def get_product(self):
        return f"{self.name}, {self.__products[0].price} руб. Остаток: {self.__products[0].quantity} шт."
