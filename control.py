from navigations.transition_stack import TransitionStack
from navigations.data_classes import *

from db.DB_methods import DBController

set_button_builder = {
    'ButtonDefault': FactoryDefaultButton,
    'ButtonNewChannel': FactoryNewChannelButton,
    'ButtonEmpty': FactoryEmptyButton,

}


class Control:
    def __init__(self):
        self.stack = TransitionStack()
        self.db = DBController()


controller = Control()
