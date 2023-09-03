import pytest
from src.keyboard import Keyboard


@pytest.fixture
def item_keyboard():
    """Зададим фикстуру с экземпляром класса Keyboard."""
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_item_init(item_keyboard):
    """Проверим все атрибуты класса на соотведствие."""
    assert item_keyboard.name == "Dark Project KD87A"
    assert item_keyboard.price == 9600
    assert item_keyboard.quantity == 5
    assert item_keyboard.language == "EN"


def test_cnange_lang(item_keyboard):
    """Проверим как меняется язык."""
    item_keyboard.change_lang()
    assert item_keyboard.language == "RU"
    item_keyboard.change_lang()
    assert item_keyboard.language == "EN"

