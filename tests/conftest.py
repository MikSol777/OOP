import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture
def category(product):
    products = [
        product,
        Product("Samsung Galaxy S23 Ultra", "256GB, Blue", 180000.0, 10),
    ]
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        products,
    )


@pytest.fixture
def product():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def sample_product():
    return Product(
        name="Xiaomi Redmi Note 11",
        description="1024GB, Синий",
        price=31000.0,
        quantity=14,
    )
