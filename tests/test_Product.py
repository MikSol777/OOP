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
        self.product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 1.5, "Model X", 128, "Black")
        self.lawn_grass = LawnGrass("Test Grass", "Test Description", 500.0, 10, "Russia", "2 weeks", "Green")

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(self.product.description, "256GB, Серый цвет, 200MP камера")
        self.assertEqual(self.product.price, 180000.0)
        self.assertEqual(self.product.quantity, 5)

    @patch("builtins.input", return_value="y")
    def test_product_price_setter(self, mock_input):
        # Test price increase
        self.product.price = 190000.0
        self.assertEqual(self.product.price, 190000.0)

        self.product.price = 170000.0
        self.assertEqual(self.product.price, 170000.0)

        self.product.price = -100
        self.assertEqual(self.product.price, 170000.0)  # Price should remain unchanged

    def test_product_addition(self):
        product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        total_value = self.product + product2
        expected_value = (180000.0 * 5) + (31000.0 * 14)  # 900000 + 434000 = 1334000
        self.assertEqual(total_value, expected_value)

    def test_product_str(self):
        expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
        self.assertEqual(str(self.product), expected)

    def test_new_product_classmethod(self):
        products = []
        product_dict = {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }

        product = Product.new_product(product_dict, products)
        self.assertEqual(len(products), 1)
        self.assertEqual(product.name, product_dict["name"])

        product_dict["quantity"] = 3
        product_dict["price"] = 190000.0
        updated_product = Product.new_product(product_dict, products)
        self.assertEqual(len(products), 1)  # Should not create new product
        self.assertEqual(updated_product.quantity, 8)  # 5 + 3
        self.assertEqual(updated_product.price, 190000.0)  # Higher price should be set

        def test_product_creation_with_zero_quantity(self):
            with self.assertRaises(ValueError) as context:
                Product("Test Product", "Description", 1000.0, 0)
            self.assertEqual(str(context.exception), "Товар с нулевым количеством не может быть добавлен")

        def test_product_creation_with_valid_quantity(self):
            product = Product("Test Product", "Description", 1000.0, 1)
            self.assertEqual(product.quantity, 1)


class TestProductInheritance(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("iPhone 15", "512GB, Gray space", 210000.0, 8, 1.5, "Model X", 128, "Black")
        self.lawn_grass = LawnGrass(
            "Газонная трава", "Элитная трава для газона", 500.0, 20, "Russia", "2 weeks", "Green"
        )
        self.product = Product("Test Product", "Test Description", 100.0, 10)

    def test_smartphone_initialization(self):
        self.assertEqual(self.smartphone.name, "iPhone 15")
        self.assertEqual(self.smartphone.efficiency, 1.5)
        self.assertEqual(self.smartphone.model, "Model X")
        self.assertEqual(self.smartphone.memory, 128)
        self.assertEqual(self.smartphone.color, "Black")

    def test_lawn_grass_initialization(self):
        self.assertEqual(self.lawn_grass.name, "Газонная трава")
        self.assertEqual(self.lawn_grass.country, "Russia")
        self.assertEqual(self.lawn_grass.germination_period, "2 weeks")
        self.assertEqual(self.lawn_grass.color, "Green")

    def test_product_addition(self):
        smartphone2 = Smartphone(
            name="Samsung Galaxy S23",
            description="256GB, Blue",
            price=180000.0,
            quantity=5,
            efficiency=95.5,
            model="S23",
            memory=256,
            color="Blue",
        )
        lawn_grass2 = LawnGrass(
            name="Газонная трава 2",
            description="Выносливая трава",
            price=450.0,
            quantity=15,
            country="США",
            germination_period="5 дней",
            color="Темно-зеленый",
        )

        self.assertEqual(self.smartphone + smartphone2, 210000.0 * 8 + 180000.0 * 5)
        self.assertEqual(self.lawn_grass + lawn_grass2, 500.0 * 20 + 450.0 * 15)


class TestSmartphone(unittest.TestCase):
    def setUp(self):
        self.smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 1.5, "Model X", 128, "Black")

    def test_smartphone_creation(self):
        self.assertEqual(self.smartphone.name, "Iphone 15")
        self.assertEqual(self.smartphone.description, "512GB, Gray space")
        self.assertEqual(self.smartphone.price, 210000.0)
        self.assertEqual(self.smartphone.quantity, 8)
        self.assertEqual(self.smartphone.efficiency, 1.5)
        self.assertEqual(self.smartphone.model, "Model X")
        self.assertEqual(self.smartphone.memory, 128)
        self.assertEqual(self.smartphone.color, "Black")


class TestLawnGrass(unittest.TestCase):
    def setUp(self):
        self.lawn_grass = LawnGrass("Test Grass", "Test Description", 500.0, 10, "Russia", "2 weeks", "Green")

    def test_lawn_grass_creation(self):
        self.assertEqual(self.lawn_grass.name, "Test Grass")
        self.assertEqual(self.lawn_grass.description, "Test Description")
        self.assertEqual(self.lawn_grass.price, 500.0)
        self.assertEqual(self.lawn_grass.quantity, 10)
        self.assertEqual(self.lawn_grass.country, "Russia")
        self.assertEqual(self.lawn_grass.germination_period, "2 weeks")
        self.assertEqual(self.lawn_grass.color, "Green")


if __name__ == "__main__":
    unittest.main()
