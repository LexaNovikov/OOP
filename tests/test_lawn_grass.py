from src.lawngrass import LawnGrass


def test_smartphone_init(green_grass: LawnGrass) -> None:
    assert green_grass.name == "grass"
    assert green_grass.description == "default grass"
    assert green_grass.price == 5000
    assert green_grass.quantity == 5
    assert green_grass.country == "Russia"
    assert green_grass.germination_period == 1
    assert green_grass.color == "green"
