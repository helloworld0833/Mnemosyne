import datetime

from PyQt5.QtWidgets import QPushButton

from utilities import write_word_to_file, update_file

class ButtonNext(QPushButton):
    def __init__(self, word_browser, meaning_browser, words_heap):
        super().__init__()

        self.word_browser = word_browser
        self.meaning_browser = meaning_browser
        self.words_heap = words_heap

        self.setText('Next')
        self.pressed.connect(self._next_word)

    def _next_word(self):
        if self.words_heap.data_list:
            top_element_list = self.words_heap.data_list[0].split(' ')

            if int(top_element_list[-1]) > 1:
                top_element_list[-1] = '{}\n'.format(int(top_element_list[-1])-1)

                self.words_heap.data_list[0] = ' '.join(top_element_list)

            self.words_heap.reheapify()

            data_line_split = self.words_heap.data_list[0].split(' ')
            word, meaning = data_line_split[0], data_line_split[1]
            self.word_browser.setText(word)
            self.meaning_browser.clear()

            update_file(self.words_heap.data_list, 'words.txt')
            update_file(self.words_heap.data_list, 'backup_words.txt')

class ButtonKnow(QPushButton):
    def __init__(self, word_browser, meaning_browser, words_heap):
        super().__init__()

        self.word_browser = word_browser
        self.meaning_browser = meaning_browser
        self.words_heap = words_heap

        self.setText('Know')
        self.pressed.connect(self._know)

    def _know(self):
        if self.words_heap.data_list:
            top_element_list = self.words_heap.data_list[0].split(' ')

            if int(top_element_list[-1]) > 1:
                top_element_list[-1] = '{}\n'.format(max(int(top_element_list[-1])//10, 1))

                self.words_heap.data_list[0] = ' '.join(top_element_list)

            self.words_heap.reheapify()

            data_line_split = self.words_heap.data_list[0].split(' ')
            word, meaning = data_line_split[0], data_line_split[1]
            self.word_browser.setText(word)
            self.meaning_browser.clear()

            update_file(self.words_heap.data_list, 'words.txt')
            update_file(self.words_heap.data_list, 'backup_words.txt')

class ButtonShowMeaning(QPushButton):
    def __init__(self, meaning_browser, words_heap):
        super().__init__()

        self.meaning_browser = meaning_browser
        self.words_heap = words_heap

        self.setText('Show Meaning')
        self.pressed.connect(self._show_meaning)

    def _show_meaning(self):
        if self.words_heap.data_list:
            self.meaning_browser.setText(self.words_heap.data_list[0].split(' ')[1])

class ButtonAdd(QPushButton):
    def __init__(self, word_text_edit, meaning_text_edit, words_heap):
        super().__init__()

        self.word_text_edit = word_text_edit
        self.meaning_text_edit = meaning_text_edit
        self.words_heap = words_heap

        self.setText('Add')
        self.pressed.connect(self._add)

    def _add(self):
        word = self.word_text_edit.toPlainText()
        meaning = self.meaning_text_edit.toPlainText()

        self.words_heap.append('{} {} 100\n'.format(word, meaning))

        write_word_to_file(word, meaning, 'words.txt')
        write_word_to_file(word, meaning, 'backup_words.txt')

        self.word_text_edit.clear()
        self.meaning_text_edit.clear()
