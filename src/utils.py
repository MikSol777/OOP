import json
from src.Product import Product
from src.Category import Category


def load_data_from_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            categories = []

            for category_data in data:
                products = []
                for product_data in category_data["products"]:
                    product = Product(
                        product_data["name"],
                        product_data["description"],
                        product_data["price"],
                        product_data["quantity"],
                    )
                    products.append(product)

                category = Category(category_data["name"], category_data["description"], products)
                categories.append(category)

            return categories
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка при чтении JSON файла {file_path}")
        return []
