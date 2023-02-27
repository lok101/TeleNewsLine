from navigations.data_classes import ButtonNewChannel, ButtonDefault, ButtonEmpty
from navigations.data_classes import MenuPage

menu_pages = [
    # стартовая страница должна передаваться первой, для корректной работы кнопки "назад" в навигации.
    MenuPage(
        page_name='start_menu',
        message_text='start_menu test text',
        buttons=[
            ButtonNewChannel(),
            ButtonDefault('Мои каналы.', 'my_channels'),
            ButtonEmpty(),
            ButtonEmpty(),
            ButtonDefault('Мой профиль.', 'my_profile'),
        ]
    ),
    MenuPage(
        page_name='my_channels',
        message_text='my_channels test text',
        buttons=[
            ButtonDefault('one_channel', 'one_channel'),
            ButtonDefault('two_channel', 'two_channel'),
            ButtonEmpty(),
            ButtonEmpty(),
        ]
    ),
    MenuPage(
        page_name='new_channel',
        message_text='new_channel test text',
        buttons=[
            ButtonEmpty(),
        ]
    ),
    MenuPage(
        page_name='my_profile',
        message_text='my_profile test text',
        buttons=[
            ButtonEmpty(),
            ButtonEmpty(),
            ButtonEmpty(),
            ButtonEmpty(),
        ]
    ),

]
