from src.item import Item


class Phone(Item):
    """Класс для товара 'телефон' в магазине."""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """Инициализация свойствами Item и добавляем количество симкарт."""
        super().__init__(name, price, quantity)
        if number_of_sim > 0 and number_of_sim % 1 == 0:
            self.__number_of_sim = number_of_sim
        else:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")

    @property
    def number_of_sim(self):
        """Возвращает количество симкарт, к атрибуту можно обращаться без()."""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        """
        Метод срабатывает при операции присваивания,
        проверяет, что количество симкарт больше 0.
        """
        if number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            print("ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __repr__(self):
        """Магический метод для отладки разработчиком."""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

