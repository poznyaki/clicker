import sys

print("Hello world")
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.init__ui()
        self.show()

    def init_ui(self):
        self.button.clicked.connect(self.on_click)
        self.hello_button.clicked.connect(self.hello)
        self.love_button.clicked.connect(self.love)
        self.eval_button.clicked.connect(self.eval_click)
        self.setLayout(self.layout)






app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec_())