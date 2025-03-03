import unittest
from unittest.mock import patch

from src.Product import Product


def test_product_initialization():
    product = Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера", "Description should be initialized correctly"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_fixture(sample_product):
    assert sample_product.name == "Xiaomi Redmi Note 11"
    assert sample_product.description == "1024GB, Синий"
    assert sample_product.price == 31000.0
    assert sample_product.quantity == 14


class TestProductProperties(unittest.TestCase):

    def setUp(self):
        self.product = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    def test_price_getter(self):
        self.assertEqual(self.product.price, 180000.0)

    @patch("builtins.input", return_value="y")
    def test_price_setter_increase(self, mock_input):
        self.product.price = 200000.0
        self.assertEqual(self.product.price, 200000.0)

    @patch("builtins.input", return_value="n")
    def test_price_setter_decrease_with_decline(self, mock_input):
        current_price = self.product.price
        self.product.price = 170000.0
        self.assertEqual(self.product.price, current_price)

    @patch("builtins.input", return_value="y")
    def test_price_setter_decrease_with_confirmation(self, mock_input):
        self.product.price = 170000.0
        self.assertEqual(self.product.price, 170000.0)


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Товар 1", "Описание товара 1", 100, 10)
        self.product2 = Product("Товар 2", "Описание товара 2", 200, 2)

    def test_str(self):
        self.assertEqual(str(self.product1), "Товар 1, 100 руб. Остаток: 10 шт.")
        self.assertEqual(str(self.product2), "Товар 2, 200 руб. Остаток: 2 шт.")

    def test_add(self):
        self.assertEqual(self.product1 + self.product2, 1400)