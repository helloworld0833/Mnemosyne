# mnemosyne

Mnemosyne is a PyQt based task management tool. It is used for customarily memorize words.

[PyQt](https://pypi.org/project/PyQt5/) is a set of Python bindings for Qt, which is a set of cross-platform C++ libraries that can be easily used to create UIs.

![demo image](https://github.com/helloworld0833/mnemosyne/blob/master/demo.png?raw=true)

First of all, input a single word in the input box "word" and corresponding meaning(s) in the input box "meaning(s)", then single click on the button "Add". After that, Mnemosyne assigns this word meaning pair with priority number 100 implicitly.

After a single click on the "Next" button, Mnemosyne subtracts 1 from the priority number of the current word, then shows the next word, which can be another word or the current word, depending on who has the highest priority.

If feeling trouble with recalling the meaning(s), single click on the "Show Meaning" button, Mnemosyne will show the meaning(s) as you wish.

After a single click on the "Know" button, Mnemosyne divides the priority number of the current word by 10 and shows the next word, which can be another word or the current word, depending on which word has the highest priority.
