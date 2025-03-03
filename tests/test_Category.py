import unittest

from src.Category import Category
from src.Product import Product


def test_category_initialization(category):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 2


def test_category_count(category):
    assert Category.category_count == 2


def test_product_count(category):
    assert category.products_count == 2


class TestCategoryProperties(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.products = [
            Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
        ]

        cls.category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            cls.products,
        )

    def test_products_property(self):
        products = self.category.products

        self.assertEqual(len(products), 3)

        self.assertEqual(products[0].name, "Samsung Galaxy C23 Ultra")
        self.assertEqual(products[1].name, "Iphone 15")
        self.assertEqual(products[2].name, "Xiaomi Redmi Note 11")

    def test_get_product_property(self):
        first_product = self.category.products[0]

        expected_output = f"Смартфоны, {first_product.price} руб. Остаток: {first_product.quantity} шт."

        self.assertEqual(self.category.get_product, expected_output)

class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Товар 1", "Описание товара 1", 100, 10)
        self.product2 = Product("Товар 2", "Описание товара 2", 200, 5)
        self.category = Category("Категория 1", "Описание категории", [self.product1, self.product2])

    def test_str(self):
        self.assertEqual(str(self.category), "Категория 1, количество продуктов: 15 шт.")