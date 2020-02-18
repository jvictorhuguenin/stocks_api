import get_data
from tkinter import *


# start the GUI
root = Tk()
root.title('Currencity Calculator')
# entry row
entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=1, column=1, columnspan=4, padx=5, pady=5)
Label(root, text='Amount:').grid(row=1, column=0, padx=1)


# get the data from get_data file
class Stocks:
    def USD_BRL(self):
        cotation = float(get_data.get_USD_BRL())
        return cotation

    def BTC_USD(self):
        cotation = float(get_data.get_BTC_USD())
        return cotation

    def EUR_BRL(self):
        cotation = float(get_data.get_EUR_BRL())
        return cotation


class Numpad(Stocks):

    # calculate the value and displays it
    def set_USD_BRL(self):
        value = float(entry.get())
        amount = value * super().USD_BRL()
        entry.delete(0, END)
        entry.insert(0, str(amount))

    def set_BTC_USD(self):
        value = float(entry.get())
        amount = value * super().BTC_USD()
        entry.delete(0, END)
        entry.insert(0, str(amount))

    def set_EUR_BRL(self):
        value = float(entry.get())
        amount = value * super().EUR_BRL()
        entry.delete(0, END)
        entry.insert(0, str(amount))

    # buttons functions
    def button_click(self, num):
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, str(current)+str(num))

    def button_clear(self):
        entry.delete(0, END)

    def button_delete(self):
        entry.delete(0, END)

    def set_button(self, num):
        return Button(root, text=f'{num}', padx=70, pady=20, command=lambda: numpad.button_click(num))


if __name__ == '__main__':
    numpad = Numpad()
    # creates 3 buttons to choose which currency we want
    # USD->BRL
    USD_BRL_button = Button(root, text='USD/BRL', padx=40,
                            command=numpad.set_USD_BRL).grid(row=0, column=0)
    # BTC->USD
    BTC_USD_button = Button(root, text='BTC/USD', padx=40,
                            command=numpad.set_BTC_USD).grid(row=0, column=1)
    # EUR->BRL
    EUR_BRL_button = Button(root, text='EUR/BRL', padx=40,
                            command=numpad.set_EUR_BRL).grid(row=0, column=2)

    # **numpad buttons**

    # define button
    numpad_1 = numpad.set_button(1)
    numpad_2 = numpad.set_button(2)
    numpad_3 = numpad.set_button(3)
    numpad_4 = numpad.set_button(4)
    numpad_5 = numpad.set_button(5)
    numpad_6 = numpad.set_button(6)
    numpad_7 = numpad.set_button(7)
    numpad_8 = numpad.set_button(8)
    numpad_9 = numpad.set_button(9)
    numpad_0 = numpad.set_button(0)
    numpad_clear = Button(root, text='Clear', padx=57,
                          pady=20, command=numpad.button_clear)
    numpad_delete = Button(root, text='Delete', padx=54,
                           pady=20, command=numpad.button_delete)

    # numpad grid

    numpad_1.grid(row=4, column=0)
    numpad_2.grid(row=4, column=1)
    numpad_3.grid(row=4, column=2)

    numpad_4.grid(row=3, column=0)
    numpad_5.grid(row=3, column=1)
    numpad_6.grid(row=3, column=2)

    numpad_7.grid(row=2, column=0)
    numpad_8.grid(row=2, column=1)
    numpad_9.grid(row=2, column=2)

    numpad_0.grid(row=5, column=0)
    numpad_clear.grid(row=5, column=1)
    numpad_delete.grid(row=5, column=2)

    # mainloop
    root.mainloop()
