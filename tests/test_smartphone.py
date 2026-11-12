from src.smartphone import Smartphone


def test_smartphone_init(xiaomi_13: Smartphone) -> None:
    assert xiaomi_13.name == "xiaomi 13"
    assert xiaomi_13.description == "supersmartphone"
    assert xiaomi_13.price == 25000
    assert xiaomi_13.quantity == 5
    assert xiaomi_13.efficiency == 5
    assert xiaomi_13.model == "xiaomi 13"
    assert xiaomi_13.memory == 256
    assert xiaomi_13.color == "green"
