from .{{ main_window_module }} import Ui_{{ widget_name }}
from PyQt5.QtWidgets import QDialog

class {{ widget_name }}(QDialog):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.ui = Ui_{{ widget_name }}()
        self.ui.setupUi(self)
        self.connections()

    def connections(self):
        pass
