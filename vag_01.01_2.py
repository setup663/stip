import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLineEdit

def text_result():
    user_text = input_text.text()
    result_text = "Таблица умножения на "+ user_text + " : \n"
    for i in range(1, 11):

        result_text += f'{user_text} * {i} = {int(user_text)*i}\n' #таблица умножения
    result_text_idit.setText(result_text)

def kvadrat():
    user_text = input_text.text()
    kvadratik = int(user_text) * int(user_text)
    result_text = "Возведение числа " + user_text + " в квадрат : " + str(kvadratik)
    result_text_idit.setText(result_text)

def kub():
    user_text = input_text.text()
    kubik = int(user_text) * int(user_text) * int(user_text)
    result_text = "Возведение числа " + user_text + " в квадрат : " + str(kubik)
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
input_text.setPlaceholderText("Введите число : ")
layout.addWidget(input_text)

button1 = QPushButton("Вычислить произведение")
layout.addWidget(button1)
button1.clicked.connect(text_result)
central_widget.setLayout(layout)

button2 = QPushButton("Возвести в квадрат")
layout.addWidget(button2)
button2.clicked.connect(kvadrat)
central_widget.setLayout(layout)

button3 = QPushButton("Возвести в куб")
layout.addWidget(button3)
button3.clicked.connect(kub)
central_widget.setLayout(layout)

windows.show()
sys.exit(app.exec())