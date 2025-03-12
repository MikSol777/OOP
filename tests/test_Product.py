import unittest
from unittest.mock import patch

from src.Product import Product, Smartphone, LawnGrass


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


class TestProductInheritance(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone(
            name="iPhone 15",
            description="512GB, Gray space",
            price=210000.0,
            quantity=8,
            efficiency=98.2,
            model="15",
            memory=512,
            color="Gray space"
        )
        self.lawn_grass = LawnGrass(
            name="Газонная трава",
            description="Элитная трава для газона",
            price=500.0,
            quantity=20,
            country="Россия",
            germination_period="7 дней",
            color="Зеленый"
        )
        self.base_product = Product(
            name="Test Product",
            description="Test Description",
            price=100.0,
            quantity=10
        )

    def test_smartphone_initialization(self):
        # Проверка базовых атрибутов
        self.assertEqual(self.smartphone.name, "iPhone 15")
        self.assertEqual(self.smartphone.description, "512GB, Gray space")
        self.assertEqual(self.smartphone.price, 210000.0)
        self.assertEqual(self.smartphone.quantity, 8)

        # Проверка специфичных атрибутов
        self.assertEqual(self.smartphone.efficiency, 98.2)
        self.assertEqual(self.smartphone.model, "15")
        self.assertEqual(self.smartphone.memory, 512)
        self.assertEqual(self.smartphone.color, "Gray space")

        # Проверка наследования
        self.assertIsInstance(self.smartphone, Product)

    def test_lawn_grass_initialization(self):
        # Проверка базовых атрибутов
        self.assertEqual(self.lawn_grass.name, "Газонная трава")
        self.assertEqual(self.lawn_grass.description, "Элитная трава для газона")
        self.assertEqual(self.lawn_grass.price, 500.0)
        self.assertEqual(self.lawn_grass.quantity, 20)

        # Проверка специфичных атрибутов
        self.assertEqual(self.lawn_grass.country, "Россия")
        self.assertEqual(self.lawn_grass.germination_period, "7 дней")
        self.assertEqual(self.lawn_grass.color, "Зеленый")

        # Проверка наследования
        self.assertIsInstance(self.lawn_grass, Product)

    def test_product_addition(self):
        smartphone2 = Smartphone(
            name="Samsung Galaxy S23",
            description="256GB, Blue",
            price=180000.0,
            quantity=5,
            efficiency=95.5,
            model="S23",
            memory=256,
            color="Blue"
        )
        lawn_grass2 = LawnGrass(
            name="Газонная трава 2",
            description="Выносливая трава",
            price=450.0,
            quantity=15,
            country="США",
            germination_period="5 дней",
            color="Темно-зеленый"
        )

        # Тест сложения одинаковых типов
        self.assertEqual(self.smartphone + smartphone2, 210000.0 * 8 + 180000.0 * 5)
        self.assertEqual(self.lawn_grass + lawn_grass2, 500.0 * 20 + 450.0 * 15)

        # Тест сложения разных типов
        with self.assertRaises(TypeError):
            self.smartphone + self.lawn_grass

        # Тест сложения с не-Product объектом
        with self.assertRaises(ValueError):
            self.smartphone + "not a product"

        # Тест сложения с None
        with self.assertRaises(ValueError):
            self.smartphone + None

        # Тест сложения с нулевым количеством
        smartphone_zero = Smartphone(
            name="Test",
            description="Test",
            price=100.0,
            quantity=0,
            efficiency=95.0,
            model="Test",
            memory=128,
            color="Black"
        )
        self.assertEqual(self.smartphone + smartphone_zero, 210000.0 * 8 + 100.0 * 0)
