from navigations.menu_constructor.pages_constructor import Page
from navigations.menu_constructor.products_constructor import Product
from menu_structure.user_pages import menu_pages
from menu_structure.user_products import products


class BotMenu(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_pages(menu_pages)
        self.add_products(products)
        pass

    def add_pages(self, pages: list[Page]):
        for page in pages:
            self.update(page.get_page())

    def add_products(self, products: dict[Product]):
        for product_button_list in products.values():
            for product in product_button_list:
                self.update(product.get_product())