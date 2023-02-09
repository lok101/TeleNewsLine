from navigations.data_classes import ButtonDefault, ButtonEmpty, ButtonNewChannel

nav = {
    # Позиция "start_menu" должна всегда оставаться первой (название менять можно).
    # В методе delete_last_position класса TransitionStack используется обращение по индексу [0].
    'start_menu': {
        'current_menu': 'start_menu',
        'text': 'start_menu test text',
        'buttons': [
            ButtonNewChannel(),
            ButtonDefault('Мои каналы.', 'my_channels'),
            ButtonEmpty(),
            ButtonEmpty(),
            ButtonDefault('Мой профиль.', 'my_profile'),
        ]
    },
    'my_channels': {
        'current_menu': 'my_channels',
        'text': 'my_channel test text',
        'buttons': [
            ButtonDefault('one_channel', 'one_channel'),
            ButtonDefault('two_channel', 'two_channel'),
            ButtonEmpty(),
            ButtonEmpty(),
        ]
    },
    'new_channel': {
        'current_menu': 'new_channel',
        'text': 'new_channel test text',
        'buttons': [
            ButtonEmpty(),
        ]
    },
    'my_profile': {
        'current_menu': 'my_profile',
        'text': 'my_profile test text',
        'buttons': [
            ButtonEmpty(),
            ButtonEmpty(),
            ButtonEmpty(),
            ButtonEmpty(),
        ]
    },
}
