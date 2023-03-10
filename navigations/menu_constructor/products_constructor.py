from slugify import slugify

from navigations.data_classes import ButtonProduct


class Product:
    def __init__(self, page_name: str, price: int, located_in_menu: str):
        self.page_name = page_name
        self.price = price
        self.located_in_menu = located_in_menu
        self.buttons = []

    def get_product(self) -> dict:
        return {f'{self.located_in_menu}-{slugify(self.page_name)}': self.__dict__}

    def get_product_button(self) -> ButtonProduct:
        return ButtonProduct(
            name=f'{self.page_name}-{self.price}',
            callback=f'{self.located_in_menu}-{slugify(self.page_name)}'
        )
