import json


def load_data_from_json(file_path: str):
    """открываем json. Путь data/products.json"""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data
