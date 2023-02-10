from navigations.transition_stack import TransitionStack
from navigations.data_classes import *

from db.channels_methods import ChannelsDBController

set_button_builder = {
    'ButtonDefault': FactoryDefaultButton,
    'ButtonNewChannel': FactoryNewChannelButton,
    'ButtonEmpty': FactoryEmptyButton,

}


class Control:
    def __init__(self):
        self.stack = TransitionStack()
        self.channels = ChannelsDBController()


controller = Control()
