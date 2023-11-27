import tkinter as tk

from display import Display
from buttons import Buttons


class Calculator():

    BUTTONS = ['1', '2', '3', '+', '4', '5', '6',
               '-', '7', '8', '9', '*', '0', '.', 'AC', '/']
    OPERATION_BUTTONS = ['+', '-', '*', '/', 'AC']

    def __init__(self, window):
        self.window = window
        self.display = Display(self.window)

        buttons = Buttons(
            self.window, self.BUTTONS, self.OPERATION_BUTTONS, columns=4, rows=4, button_click=self.button_click)

        self.clear_func()

    def set_value(self, value):
        self.value = value
        self.display.show(self.value)

    def button_click(self, button_text):
        if button_text == '=':
            self.equal_func()
        elif button_text == 'AC':
            self.clear_func()
        elif button_text in self.OPERATION_BUTTONS:
            self.operation_func(button_text)
        else:
            self.number_func(button_text)

    def operation_func(self, operation):
        self.operation = operation
        if not self.finished:
            self.mem_value = self.value

        self.finished = False
        self.set_value("0")

    def number_func(self, number):
        if (self.finished):
            self.clear_func()
        self.set_value(number if self.value == "0" else self.value+number)

    def equal_func(self):
        operation = self.operation
        num1 = float(self.mem_value)
        num2 = float(self.value)
        if (operation == '+'):
            self.display.show(num1+num2)
        elif (operation == '-'):
            self.display.show(num1-num2)
        elif (operation == '*'):
            self.display.show(num1*num2)
        elif (operation == '/'):
            self.display.show(num1/num2)

        self.mem_value = self.display.getValue()
        self.finished = True

    def clear_func(self):
        self.operation = ''
        self.mem_value = '0'
        self.set_value("0")
        self.finished = False
