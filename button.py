import tkinter as tk


class Button():
    def __init__(self, window, text, command, type, row, column, columnspan=1):
        color = "blue" if type == "operation" else "black"
        self.window = window
        self.button = tk.Button(
            window, text=text, command=command, fg=color, width=3, height=2)
        self.button.grid_configure(padx=2, pady=2)
        self.button.grid(column=column, row=row, columnspan=columnspan)
