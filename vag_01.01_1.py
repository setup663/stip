import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit

def text_result():
    user_text = input_text.text()
    user_text2 = input_text2.text()
    result_text = "Входящий вызов " + user_text2 + " от " + user_text
    result_text_idit.setText(result_text)

app = QApplication(sys.argv)
windows = QMainWindow()

central_widget = QWidget()
windows.setCentralWidget(central_widget)

layout = QVBoxLayout()

result_text_idit = QTextEdit()
result_text_idit.setReadOnly(True)
layout.addWidget(result_text_idit)

input_text = QLineEdit()
input_text.setPlaceholderText("как вас зовут?")
layout.addWidget(input_text)

input_text2 = QLineEdit()
input_text2.setPlaceholderText("введите ваш номер")
layout.addWidget(input_text2)

button1 = QPushButton("Ответить на звонок")
layout.addWidget(button1)
button1.clicked.connect(text_result)
central_widget.setLayout(layout)

windows.show()
sys.exit(app.exec())