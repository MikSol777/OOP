from abc import ABC

# Миксин для логирования
class LoggerMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ', '.join([f"{key}={value}" for key, value in kwargs.items()])
        print(f"Создан объект класса {class_name} с параметрами: {params}")
        if hasattr(super(), '__init__'):
            super().__init__(*args, **kwargs)

# Базовый абстрактный класс для всех продуктов
class BaseProduct(ABC):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity

    @property
    def price(self):
        return self.__price

    def __repr__(self):
        pass

# Класс-продукт с логированием и дополнительной функциональностью
class Product(LoggerMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        super().__init__(name=name, description=description, price=price, quantity=quantity)

    def __repr__(self):
        return self.name

    @classmethod
    def new_product(cls, product_dict: dict, products: list):
        for product in products:
            if product.name == product_dict["name"]:
                product.quantity += int(product_dict["quantity"])
                if product_dict["price"] > product.price:
                    product.price = product_dict["price"]
                return product

        new_product = Product(
            product_dict["name"], product_dict["description"], product_dict["price"], product_dict["quantity"]
        )
        products.append(new_product)
        return new_product

    @property
    def price(self):
        return self._BaseProduct__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self._BaseProduct__price:
            confirmation = input(f"Новая цена меньше текущей цены. Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() == "y":
                self._BaseProduct__price = value
                print(f"Цена успешно понижена до {self._BaseProduct__price}.")
            else:
                print("Цена не была изменена.")
        else:
            self._BaseProduct__price = value
            print(f"Цена обновлена")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Можно складывать только объекты Product")
        return (self.price * self.quantity) + (other.price * other.quantity)

# Класс-смартфон, который наследует Product
class Smartphone(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

# Класс-газонная трава, который наследует Product
class LawnGrass(Product):
    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: str, color: str):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
