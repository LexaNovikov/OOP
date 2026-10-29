from src.main import Category, Product

samsung = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
smartphones = Category(
    "Смартфоны",
    "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    [],
)


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
    assert headphones.category_count == 2
    assert headphones.product_count == 3


def test_add_product() -> None:

    smartphones.add_product(samsung)
    assert smartphones._products[0].name == "Samsung Galaxy S23 Ultra"
    assert smartphones._products[0].description == "256GB, Серый цвет, 200MP камера"
    assert smartphones._products[0].price == 180000.0
    assert smartphones._products[0].quantity == 5


def test_get_all_categories() -> None:
    categories = Category.get_all_categories()
    assert categories[0].name == "Смартфоны"
    assert (
        categories[0].description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert categories[0]._products[0].name == "Samsung Galaxy S23 Ultra"
    assert categories[0]._products[0].description == "256GB, Серый цвет, 200MP камера"
    assert categories[0]._products[0].price == 180000.0
    assert categories[0]._products[0].quantity == 5


def test_get_products() -> None:
    assert smartphones.products == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
