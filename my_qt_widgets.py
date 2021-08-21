from PyQt5.QtWidgets import QHBoxLayout, QWidget, QTextBrowser, QTextEdit

class MyQHBoxLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)

class MyQWidget(QWidget):
    def __init__(self, layout=None):
        super().__init__()

        self.setContentsMargins(0, 0, 0, 0)

        if layout:
            self.setLayout(layout)

class MyQTextBrowser(QTextBrowser):
    def __init__(self, text=''):
        super().__init__()

        if text:
            self.setText(text)

class MyQTextEdit(QTextEdit):
    def __init__(self, maximum_height=27, place_holder_text='', text=''):
        super().__init__(maximumHeight=maximum_height)

        if place_holder_text:
            self.setPlaceholderText(place_holder_text)

        if text:
            self.setText(text)
