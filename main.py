import tkinter as tk
from calculator import Calculator


class main():
    def __init__(self):
        self.window = tk.Tk()
        self.cal = Calculator(self.window)
        self.window.title("Calculator")
        self.window.geometry("300x400")
        self.window.mainloop()


main()
