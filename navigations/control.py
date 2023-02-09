from navigations.transition_stack import TransitionStack
from navigations.channels import UserChannels
from navigations.data_classes import *


set_button_builder = {
    'ButtonDefault': FactoryDefaultButton,
    'ButtonNewChannel': FactoryNewChannelButton,
    'ButtonEmpty': FactoryEmptyButton,

}


# def set_button_builder(button: (DefaultMenuButton, EmptyMenuButton)):
#     if isinstance(button, DefaultMenuButton):
#         return FactoryDefaultButton
#     if isinstance(button, EmptyMenuButton):
#         return FactoryEmptyButton



class Control:
    def __init__(self):
        self.stack = TransitionStack()
        self.channels = UserChannels()


controller = Control()
