from src.mixin import Mixin
from src.classes import Product, BaseProduct

new_prod = Product("product", "description", 4000, 5)


def test_init():
    assert new_prod.name == "product"
    assert new_prod.description == "description"
    assert new_prod.price == 4000
    assert new_prod.quantity == 5
def test_repr():
    assert new_prod.__repr__() == "Product('product', 'description', 4000, 5)"