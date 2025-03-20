import json
from pathlib import Path
from typing import Any

from src.classes import Category, Product

ROOT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT_DIR / "data"


def load_json_file_with_classes(open_file: Any) -> Any:
    """Принимает на вход имя JSON-файла по пути ./data/ и
    классы Category и Product из модуля src.classes"""
    try:
        with open(f"{DATA_DIR}\\{open_file}.json", "r", encoding="utf-8") as jf:
            try:
                json_obj = json.load(jf)
                if json_obj:
                    categories = []
                    for category_data in json_obj:
                        category_name = category_data["name"]
                        category_description = category_data["description"]
                        products_data = category_data["products"]

                        products = []
                        for product_data in products_data:
                            product_name = product_data["name"]
                            product_description = product_data["description"]
                            product_price = product_data["price"]
                            product_quantity = product_data["quantity"]

                            product = Product(product_name, product_description, product_price, product_quantity)
                            products.append(product)

                        category = Category(category_name, category_description, products)
                        categories.append(category)

                    return categories
                else:
                    print("Файл содержит пустой список")
                    return []
            except json.JSONDecodeError:
                print("Объект не является JSON или JSON имеет неверный формат")
                return []
    except FileNotFoundError:
        print("Файл не найден")
        return []
