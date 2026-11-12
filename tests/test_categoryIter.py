from src.category_iter import CategoryIter
from src.classes import Category


def test_category_iter(smartphones: Category) -> None:
    smartphonesiter = CategoryIter(smartphones)
    assert smartphonesiter.index == -1
    assert next(smartphonesiter).name == "Samsung Galaxy S23 Ultra"
    assert next(smartphonesiter).name == "Iphone 16"
    assert next(smartphonesiter).name == "Xiaomi Redmi Note 11"
