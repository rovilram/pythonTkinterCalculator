from button import Button
import tkinter as tk


class Buttons():

    def __init__(self, window, BUTTONS, OPERATION_BUTTONS, rows, columns, button_click):

        self.BUTTONS = BUTTONS
        self.OPERATION_BUTTONS = OPERATION_BUTTONS
        self.rows = rows
        self.columns = columns
        self.button_click = button_click

        self.window = window

        self.frame = tk.Frame(window)
        self.frame.pack(anchor=tk.CENTER)

        self.normal_buttons_frame = tk.Frame(self.frame)
        self.normal_buttons_frame.pack(anchor=tk.CENTER, pady=10)

        i = 0
        buttons = []
        for button_text in self.BUTTONS:
            button = Button(window=self.normal_buttons_frame,
                            text=button_text,
                            command=lambda x=button_text: self.button_click(
                                x),
                            type="operation" if button_text in self.OPERATION_BUTTONS else "number",
                            row=int(i/self.rows),
                            column=i % self.columns
                            )
            buttons.append(button)
            i += 1

        self.equal_frame = tk.Frame(self.frame)
        self.equal_frame.pack(anchor=tk.CENTER)
        Button(window=self.equal_frame, text="=", command=lambda: self.button_click('='),
               type="operation", row=0, column=0, columnspan=4)

    def button_click(self, button_text):
        self.button_clicked_func(button_text)
