class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __repr__(self):
        return self.name

    @classmethod
    def new_product(cls, product_dict: dict, products: list):
        for product in products:
            if product.name == product_dict["name"]:
                product.quantity += int(product_dict["quantity"])
                if product_dict["price"] > product.__price:
                    product.__price = product_dict["price"]

            return Product(
                product_dict["name"], product_dict["description"], product_dict["price"], product_dict["quantity"]
            )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif value < self.__price:
            confirmation = input(f"Новая цена меньше текущей цены . Вы уверены, что хотите понизить цену? (y/n): ")
            if confirmation.lower() == "y":
                self.__price = value
                print(f"Цена успешно понижена до {self.__price}.")
            else:
                print("Цена не была изменена.")
        else:
            self.__price = value
            print(f"Цена обновлена")

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        else:
            raise ValueError("ошибка.")
