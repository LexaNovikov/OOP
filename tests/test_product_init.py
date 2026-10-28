from src.main import Product


def test_product_init() -> None:
    product1 = Product("realme airbuds 3", "Крутые наушники", 5000, 5)
    assert product1.name == "realme airbuds 3"
    assert product1.description == "Крутые наушники"
    assert product1.price == 5000
    assert product1.quantity == 5
