from navigations.menu_constructor.pages_constructor import DefaultPage, ProductPage
from navigations.data_classes import ButtonNewChannel, ButtonDefault

menu_pages = [
    # стартовая страница должна передаваться первой, для корректной работы кнопки "назад" в навигации.
    DefaultPage(
        page_name='start_menu',
        message_text='start_menu test text',
        buttons=[
            ButtonNewChannel(),
            ButtonDefault('Мои каналы.', 'my_channels'),
        ]
    ),
    ProductPage(
        page_name='my_channels',
        message_text='my_channels test text',

    ),
    DefaultPage(
        page_name='new_channel',
        message_text='new_channel test text',
        buttons=[

        ]
    ),
    DefaultPage(
        page_name='my_profile',
        message_text='my_profile test text',
        buttons=[

        ]
    ),

]
