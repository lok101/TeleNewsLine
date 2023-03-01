from navigations.bot_navigation_menu import MenuPage
from navigations.data_classes import ButtonNewChannel, ButtonDefault, ButtonEmpty

menu_pages = [
    # стартовая страница должна передаваться первой, для корректной работы кнопки "назад" в навигации.
    MenuPage(
        page_name='start_menu',
        message_text='start_menu test text',
        buttons=[
            ButtonNewChannel(),
            ButtonDefault('Мои каналы.', 'my_channels'),
        ]
    ),
    MenuPage(
        page_name='my_channels',
        message_text='my_channels test text',

    ),
    MenuPage(
        page_name='new_channel',
        message_text='new_channel test text',
        buttons=[

        ]
    ),
    MenuPage(
        page_name='my_profile',
        message_text='my_profile test text',
        buttons=[

        ]
    ),

]
