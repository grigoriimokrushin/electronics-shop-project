import csv
import os.path


class InstantiateCSVError(Exception):
    """Исключение выбрасывается, если файл item.csv поврежден (например, отсутствует одна из колонок данных)."""

    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара (приватный).
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def __repr__(self):
        """Магический метод для отладки разработчиком."""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Магический метод для нашего пользователя."""
        return f"{self.__name}"

    def __add__(self, other):
        """Метод сложения для классов Item и Phone с проверкой."""
        if isinstance(other, Item):
            return self.quantity + other.quantity

    @property
    def name(self):
        """Возвращает название товара, к атрибуту можно обращаться без()."""
        return self.__name

    @name.setter
    def name(self, name):
        """
        Метод срабатывает при операции присваивания,
        проверяет, что длинна имени не больше 10 знаков.
        """
        if len(name) < 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, file_name='items.csv'):
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""
        try:
            ITEMS_CSV_PATH = os.path.join(os.path.dirname(__file__), file_name)
            with open(ITEMS_CSV_PATH) as csv_file:
                reader = csv.DictReader(csv_file)
                for line in reader:
                    if 'name' in line and 'price' in line and 'quantity' in line:
                        cls.all.append(cls(line['name'], line['price'], line['quantity']))
                    else:
                        raise InstantiateCSVError
        except FileNotFoundError:
            print('Отсутствует файл items.csv')
        except InstantiateCSVError as e:
            print(e)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @staticmethod
    def string_to_number(line: str) -> int:
        """Возвращает число из числа-строки"""
        return int(float(line))
