from src.main import Category, Product


def test_category_init() -> None:
    product1 = Product("realme airbuds 3", "Крутые наушники", 5000, 5)
    product2 = Product("lynacy louder", "Крутые наушники от бустера", 12000, 3)
    product3 = Product("sony wh 1000", "Крутые наушники от sony", 15000, 12)
    headphones = Category(
        "Наушники",
        "Штуки, которые надел и никого не слышишь",
        [product1, product2, product3],
    )
    assert headphones.name == "Наушники"
    assert headphones.description == "Штуки, которые надел и никого не слышишь"
    assert headphones.category_count == 1
    assert headphones.product_count == 3
