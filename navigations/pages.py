from navigations.data_classes import DefaultMenuButton, EmptyMenuButton

nav = {
    # Позиция "start_menu" должна всегда оставаться первой (название менять можно).
    # В методе delete_last_position класса TransitionStack используется обращение по индексу [0].
    'start_menu': {
        'current_menu': 'start_menu',
        'text': 'start_menu test text',
        'buttons': [
            DefaultMenuButton('Добавить канал', 'new_channel'),
            DefaultMenuButton('Мои каналы', 'my_channel'),
            EmptyMenuButton(),
            EmptyMenuButton(),
            EmptyMenuButton(),
        ]
    },
    'my_channel': {
        'current_menu': 'my_channel',
        'text': 'my_channel test text',
        'buttons': [
            DefaultMenuButton('one_channel', 'one_channel'),
            DefaultMenuButton('two_channel', 'two_channel'),
            EmptyMenuButton(),
            EmptyMenuButton(),
        ]
    },
    'new_channel': {
        'current_menu': 'new_channel',
        'text': 'new_channel test text',
        'buttons': [

        ]
    },
    'my_profile': {
        'current_menu': 'my_profile',
        'text': 'my_profile test text',
        'buttons': [
            EmptyMenuButton(),
            EmptyMenuButton(),
            EmptyMenuButton(),
            EmptyMenuButton(),
        ]
    },
}
