from src.item import Item


class Language:
    """
    Класс-миксин для присвоения Item языка.
    """

    def __init__(self):
        """Инициализация по умолчанию EN."""
        self.__language = 'EN'

    @property
    def language(self):
        """Возвращает язык, к атрибуту можно обращаться без()."""
        return self.__language

    def change_lang(self):
        """Метод изменения языка."""
        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self


class Keyboard(Item, Language):
    """Класс для клавиатуры наследует от Item и класса-миксина для языка."""
    pass
