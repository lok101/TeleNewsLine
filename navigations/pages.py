nav = {
    # Позиция "start_menu" должна всегда оставаться первой (название менять можно).
    # В методе delete_last_position класса TransitionStack используется обращение по индексу [0].
    'start_menu': {
        'current_menu': 'start_menu',
        'text': 'start_menu test text',
        'buttons': {
            'Добавить канал': 'new_channel',
            'Мои каналы': 'my_channel',
        }
    },
    'my_channel': {
        'current_menu': 'my_channel',
        'text': 'my_channel test text',
        'buttons': {
            'one_channel': 'one_channel',
            'two_channel': 'two_channel',
            'three_channel': 'three_channel',
        }
    }
}
