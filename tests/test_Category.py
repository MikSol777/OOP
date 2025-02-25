from src.Category import Category


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
    assert Category.product_count == 6
