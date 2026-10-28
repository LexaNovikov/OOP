import json
import os
from src.main import Category, Product

base = os.path.dirname(os.path.dirname(__file__))


def read_json(path: str = os.path.join(base, "data", "products.json")) -> list:
    with open(path) as json_file:
        categories = json.load(json_file)
        categories_list = []
        for category in categories:
            products = []
            for product in category["products"]:
                products.append(
                    Product(
                        product["name"],
                        product["description"],
                        product["price"],
                        product["quantity"],
                    )
                )
            categories_list.append(
                Category(
                    category["name"],
                    category["description"],
                    products,
                )
            )
    return categories_list
