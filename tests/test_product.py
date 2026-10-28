from unittest.mock import MagicMock, patch

from src.main import Category, Product


def test_product_init() -> None:
    product1 = Product("realme airbuds 3", "Крутые наушники", 5000, 5)
    assert product1.name == "realme airbuds 3"
    assert product1.description == "Крутые наушники"
    assert product1.price == 5000
    assert product1.quantity == 5


@patch("builtins.input")
@patch("builtins.print")
def test_new_product(mock_print: MagicMock, mock_input: MagicMock) -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    smartphones = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    mock_input.side_effect = ["ошибочный_ввод", "y"]
    iphone = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 200000.0, "quantity": 8}
    result = Product.new_product(iphone)
    assert result.name == "Iphone 15"
    assert result.description == "512GB, Gray space"
    assert result.price == 200000.0
    assert result.quantity == 16
    assert smartphones._products[1].name == "Iphone 15"
    assert smartphones._products[1].description == "512GB, Gray space"
    assert smartphones._products[1].price == 200000.0
    assert smartphones._products[1].quantity == 16
    mock_print.assert_called_once_with(
        "Некорректный ввод. Введите y или n\n"
        "Новая цена 200000.0 меньше предыдущей 210000.0\n"
        "Поменять цену на новую? (Y/n)"
    )


@patch("builtins.input")
@patch("builtins.print")
def test_new_product_no(mock_print: MagicMock, mock_input: MagicMock) -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    smartphones = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )
    mock_input.side_effect = ["ошибочный_ввод", "n"]
    iphone = {"name": "Iphone 15", "description": "512GB, Gray space", "price": 200000.0, "quantity": 8}
    result = Product.new_product(iphone)
    assert result.name == "Iphone 15"
    assert result.description == "512GB, Gray space"
    assert result.price == 210000.0
    assert result.quantity == 32
    assert smartphones._products[1].name == "Iphone 15"
    assert smartphones._products[1].description == "512GB, Gray space"
    assert smartphones._products[1].price == 210000.0
    assert smartphones._products[1].quantity == 32
    mock_print.assert_called_once_with(
        "Некорректный ввод. Введите y или n\n"
        "Новая цена 200000.0 меньше предыдущей 210000.0\n"
        "Поменять цену на новую? (Y/n)"
    )


def test_setter() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product1.price = 200000.0
    assert product1.price == 200000.0


@patch("builtins.print")
def test_setter_error(mock_print: MagicMock) -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product1.price = -20
    mock_print.assert_called_once_with("Цена не должна быть нулевая или отрицательная")
    assert product1.price == 180000.0
