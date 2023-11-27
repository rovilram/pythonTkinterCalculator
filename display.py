import tkinter as tk


class Display():
    def __init__(self, window):
        self.window = window
        self.__value = tk.StringVar(self.window, '0')

        self.entry = tk.Entry(window,
                              state='normal',
                              disabledbackground='white',
                              width=25,
                              justify='right',
                              textvariable=self.__value)
        self.entry.place(x=10, y=10)
        self.entry.pack(anchor=tk.CENTER, pady=10)

    def show(self, text):
        self.__value.set(str(text))

    def getValue(self):
        return self.__value.get()
