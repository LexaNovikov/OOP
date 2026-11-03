import pytest

from src.main import Category, Product
@pytest.fixture
def smartphones() -> Category:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 16", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    smartphones = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    return smartphones
@pytest.fixture
def samsung() -> Product:
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
@pytest.fixture
def xiaomi() -> Product:
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
@pytest.fixture
def headphones() -> Category:
    product1 = Product("realme airbuds 3", "Крутые наушники", 5000, 5)
    product2 = Product("lynacy louder", "Крутые наушники от бустера", 12000, 3)
    product3 = Product("sony wh 1000", "Крутые наушники от sony", 15000, 12)
    headphones = Category(
        "Наушники",
        "Штуки, которые надел и никого не слышишь",
        [product1, product2, product3],
    )
    return headphones