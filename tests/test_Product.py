from src.Product import Product


def test_product_initialization():
    product = Product(
        name="Samsung Galaxy C23 Ultra",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert (
        product.description == "256GB, Серый цвет, 200MP камера"
    ), "Description should be initialized correctly"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_fixture(sample_product):
    assert sample_product.name == "Xiaomi Redmi Note 11"
    assert sample_product.description == "1024GB, Синий"
    assert sample_product.price == 31000.0
    assert sample_product.quantity == 14
