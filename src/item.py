import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity

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
    def instantiate_from_csv(cls):
        """Инициализирует экземпляры класса Item данными из файла src/items.csv"""
        with open('C:\\Users\\tanya\\PycharmProjects\\electronics-shop-project\\src\\items.csv') as csv_file:
            reader = csv.DictReader(csv_file)
            for line in reader:
                cls.all.append(cls(line['name'], line['price'], line['quantity']))



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