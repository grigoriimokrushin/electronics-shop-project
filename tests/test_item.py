"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_smartphone():
    return Item("Смартфон", 10000, 20)


def test_item_init(item_smartphone):
    assert item_smartphone.name == "Смартфон"
    assert item_smartphone.price == 10000
    assert item_smartphone.quantity == 20
    assert item_smartphone.pay_rate == 1.0


def test_calculate_total_price(item_smartphone):
    assert item_smartphone.calculate_total_price() == 200000


def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
