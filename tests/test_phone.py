import pytest
from src.phone import Phone


@pytest.fixture
def item_smartphone():
    """Зададим фикстуру с экземпляром класса Phone."""
    return Phone("iPhone 14", 120_000, 5, 2)


def test_item_init(item_smartphone):
    """Проверим все атрибуты класса на соотведствие."""
    assert item_smartphone.name == "iPhone 14"
    assert item_smartphone.price == 120_000
    assert item_smartphone.quantity == 5
    item_smartphone.number_of_sim = 0
    assert item_smartphone.number_of_sim == 2
    item_smartphone.number_of_sim = 4
    assert item_smartphone.number_of_sim == 4


def test_init():
    with pytest.raises(AttributeError):
        repr(Phone("iPhone 14", 120_000, 5, 0))


def test_repr(item_smartphone):
    """Проверяем наш магический метод."""
    assert repr(item_smartphone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(item_smartphone):
    """Проверяем наш магический метод."""
    assert str(item_smartphone) == 'iPhone 14'


def test_add(item_smartphone):
    """Проверяем как складываются экземпляры."""
    assert item_smartphone + item_smartphone == 10
