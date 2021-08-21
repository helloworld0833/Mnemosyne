from PyQt5.QtWidgets import QMainWindow, QVBoxLayout

from my_qt_widgets import MyQHBoxLayout, MyQWidget, MyQTextBrowser, MyQTextEdit
from push_button import ButtonNext, ButtonKnow, ButtonShowMeaning, ButtonAdd
from heap import Heap

from utilities import read_words_from_file

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('my board')

        main_vertical_box_layout = QVBoxLayout()

        words_heap = Heap(read_words_from_file('words.txt'))

        horizontal_box_layout = MyQHBoxLayout()
        word_browser = MyQTextBrowser(words_heap.data_list[0].strip().split(' ')[0]) if words_heap.data_list else MyQTextBrowser()
        meaning_browser = MyQTextBrowser()
        horizontal_box_layout.addWidget(word_browser)
        horizontal_box_layout.addWidget(meaning_browser)
        widget = MyQWidget(horizontal_box_layout)
        main_vertical_box_layout.addWidget(widget)

        horizontal_box_layout = MyQHBoxLayout()
        button_next = ButtonNext(word_browser, meaning_browser, words_heap)
        button_know = ButtonKnow(word_browser, meaning_browser, words_heap)
        button_show_meaning = ButtonShowMeaning(meaning_browser, words_heap)
        horizontal_box_layout.addWidget(button_next)
        horizontal_box_layout.addWidget(button_know)
        horizontal_box_layout.addWidget(button_show_meaning)
        widget = MyQWidget(horizontal_box_layout)
        main_vertical_box_layout.addWidget(widget)

        horizontal_box_layout = MyQHBoxLayout()
        word_text_edit = MyQTextEdit(maximum_height=27, place_holder_text='word')
        meaning_text_edit = MyQTextEdit(maximum_height=27, place_holder_text='meaning(s)')
        horizontal_box_layout.addWidget(word_text_edit)
        horizontal_box_layout.addWidget(meaning_text_edit)
        widget = MyQWidget(horizontal_box_layout)
        main_vertical_box_layout.addWidget(widget)

        horizontal_box_layout = MyQHBoxLayout()
        button_add = ButtonAdd(word_text_edit, meaning_text_edit, words_heap)
        horizontal_box_layout.addWidget(button_add)
        widget = MyQWidget(horizontal_box_layout)
        main_vertical_box_layout.addWidget(widget)

        widget = MyQWidget(main_vertical_box_layout)
        self.setCentralWidget(widget)
