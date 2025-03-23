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

    def test_first_product_property(self):
        first_product = self.category.products[0]
        expected_output = f"Смартфоны, {first_product.price} руб. Остаток: {first_product.quantity} шт."
        self.assertEqual(self.category.first_product, expected_output)


class TestCategory(unittest.TestCase):
    def setUp(self):
        Category.category_count = 0
        Category.products_count = 0

        self.product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
        self.product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
        self.product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

        self.category = Category(
            "Смартфоны",
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
            [self.product1, self.product2, self.product3],
        )

    def test_category_creation(self):
        self.assertEqual(self.category.name, "Смартфоны")
        self.assertEqual(
            self.category.description,
            "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        )
        self.assertEqual(len(self.category.products), 3)
        self.assertEqual(self.category.products_count, 3)
        self.assertEqual(Category.category_count, 1)
        self.assertEqual(Category.products_count, 3)

    def test_category_add_product(self):
        new_product = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        self.category.add_product(new_product)
        self.assertEqual(len(self.category.products), 4)
        self.assertEqual(self.category.products_count, 3)
        self.assertEqual(Category.products_count, 3)

    def test_category_add_invalid_product(self):
        with self.assertRaises(TypeError):
            self.category.add_product("Not a product")

    def test_category_first_product(self):
        expected = "Смартфоны, 180000.0 руб. Остаток: 5 шт."
        self.assertEqual(self.category.first_product, expected)

    def test_category_str(self):
        expected = "Смартфоны, количество продуктов: 27 шт."
        self.assertEqual(str(self.category), expected)

    def test_multiple_categories(self):
        product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
        category2 = Category(
            "Телевизоры",
            "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
            [product4],
        )

        self.assertEqual(Category.category_count, 2)
        self.assertEqual(Category.products_count, 4)  # 3 from first category + 1 from second

    def test_category_products_property(self):
        products = self.category.products
        self.assertEqual(len(products), 3)
        self.assertEqual(products[0].name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(products[1].name, "Iphone 15")
        self.assertEqual(products[2].name, "Xiaomi Redmi Note 11")

    def test_middle_price_with_products(self):
        # Average of 180000.0, 210000.0, and 31000.0
        expected_average = (180000.0 + 210000.0 + 31000.0) / 3
        self.assertEqual(self.category.middle_price(), expected_average)

    def test_middle_price_empty_category(self):
        empty_category = Category("Пустая категория", "Категория без продуктов", [])
        self.assertEqual(empty_category.middle_price(), 0)

    def test_middle_price_single_product(self):
        single_product_category = Category("Один продукт", "Категория с одним продуктом", [self.product1])
        self.assertEqual(single_product_category.middle_price(), self.product1.price)


if __name__ == "__main__":
    unittest.main()
