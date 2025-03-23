from abc import ABC, abstractmethod


# Миксин для логирования
class LoggerMixin:
    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        params = ", ".join([f"{key}={value}" for key, value in kwargs.items()])
        print(f"Создан объект класса {class_name} с параметрами: {params}")
        super().__init__()


# Базовый абстрактный класс для всех продуктов
class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, product_dict: dict, products: list):
        pass


# Класс-продукт с логированием и дополнительной функциональностью
class Product(LoggerMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут
        self.quantity = quantity
        super().__init__(name, description, price, quantity)

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

        new_product = cls(
            **product_dict
        )  # распаковываем словарь на именованные аргументы name="a", description="b", price=1, quantity=2, country='c' и т.д.
        products.append(new_product)
        return new_product

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(f"Новая цена меньше текущей цены. Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = value
                print(f"Цена успешно понижена до {self.__price}.")
            else:
                print("Цена не была изменена.")
        else:
            self.__price = value
            print(f"Цена обновлена")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise ValueError("Можно складывать только объекты Product")
        return (self.price * self.quantity) + (other.price * other.quantity)


# Класс-смартфон, который наследует Product
class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


# Класс-газонная трава, который наследует Product
class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
