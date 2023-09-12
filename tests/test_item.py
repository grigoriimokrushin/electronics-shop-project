import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def item_smartphone():
    """Зададим фикстуру с экземпляром класса."""
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def iphone():
    """Зададим фикстуру с экземпляром класса."""
    return Phone("Смартфон", 10000, 20, 2)


def test_item_init(item_smartphone):
    """Проверим все атрибуты класса на соотведствие."""
    assert item_smartphone.name == "Смартфон"
    assert item_smartphone.price == 10000
    assert item_smartphone.quantity == 20
    assert item_smartphone.pay_rate == 1.0


def test_calculate_total_price(item_smartphone):
    """Проверим метод для подсчета общей суммы остатка в магазине."""
    assert item_smartphone.calculate_total_price() == 200000


def test_apply_discount():
    """Проверим метод для реализации скидки."""
    item1 = Item("Смартфон", 10000, 20)
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_name(item_smartphone):
    """
    Проверяем как записывается name через setter
    и идет обращение через getter.
    """
    item_smartphone.name = '123'
    assert item_smartphone.name == '123'
    item_smartphone.name = 'СуперСмартфон'
    assert item_smartphone.name == 'СуперСмарт'


def test_string_to_number():
    """
    Проверяем как работает статический
    метод для вывода числа из числа-строки.
    """
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_instantiate_from_csv():
    """
    Проверяем как работает метод для
    инициализации экзепляров из csv-фаил.
    """

    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_raises_csv():
    """Проверяем класс InstantiateCSVError и отработку исключения."""
    with pytest.raises(InstantiateCSVError, match="Файл items.csv поврежден"):
        Item.instantiate_from_csv(file_name="items_test.csv")
    with pytest.raises(FileNotFoundError, match="Отсутствует файл items.csv"):
        Item.instantiate_from_csv(file_name="test")


def test_repr(item_smartphone):
    """Проверяем наш магический метод."""
    assert repr(item_smartphone) == "Item('Смартфон', 10000, 20)"


def test_str(item_smartphone):
    """Проверяем наш магический метод."""
    assert str(item_smartphone) == 'Смартфон'


def test_add(item_smartphone, iphone):
    """Проверяем как складываются экземпляры классов."""
    assert item_smartphone + iphone == 40
