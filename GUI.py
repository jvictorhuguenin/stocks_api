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
def USD_BRL():
    value = entry.get()
    amount = float(value) * float(get_data.get_USD_BRL())
    entry.delete(0, END)
    entry.insert(0, str(amount))


def BTC_USD():
    value = entry.get()
    amount = float(value) * float(get_data.get_BTC_USD())
    entry.delete(0, END)
    entry.insert(0, str(amount))


def EUR_BRL():
    value = entry.get()
    amount = float(value) * float(get_data.get_EUR_BRL())
    entry.delete(0, END)
    entry.insert(0, str(amount))


if __name__ == '__main__':
    # creates 3 buttons to choose which currency we want
    # USD->BRL
    USD_BRL_button = Button(root, text='USD/BRL', padx=40,
                            command=USD_BRL).grid(row=0, column=0)
    # BTC->USD
    BTC_USD_button = Button(root, text='BTC/USD', padx=40,
                            command=BTC_USD).grid(row=0, column=1)
    # EUR->BRL
    EUR_BRL_button = Button(root, text='EUR/BRL', padx=40,
                            command=EUR_BRL).grid(row=0, column=2)

    # **numpad buttons**

    def button_click(num):
        current = entry.get()
        entry.delete(0, END)
        entry.insert(0, str(current)+str(num))

    def button_clear():
        entry.delete(0, END)

    def button_delete():
        entry.delete(0, END)

    # define button
    numpad_1 = Button(root, text='1', padx=70, pady=20,
                      command=lambda: button_click(1))
    numpad_2 = Button(root, text='2', padx=70, pady=20,
                      command=lambda: button_click(2))
    numpad_3 = Button(root, text='3', padx=70, pady=20,
                      command=lambda: button_click(3))
    numpad_4 = Button(root, text='4', padx=70, pady=20,
                      command=lambda: button_click(4))
    numpad_5 = Button(root, text='5', padx=70, pady=20,
                      command=lambda: button_click(5))
    numpad_6 = Button(root, text='6', padx=70, pady=20,
                      command=lambda: button_click(6))
    numpad_7 = Button(root, text='7', padx=70, pady=20,
                      command=lambda: button_click(7))
    numpad_8 = Button(root, text='8', padx=70, pady=20,
                      command=lambda: button_click(8))
    numpad_9 = Button(root, text='9', padx=70, pady=20,
                      command=lambda: button_click(9))
    numpad_0 = Button(root, text='0', padx=70, pady=20,
                      command=lambda: button_click(0))
    numpad_clear = Button(root, text='Clear', padx=57,
                          pady=20, command=button_clear)
    numpad_delete = Button(root, text='Delete', padx=54,
                           pady=20, command=button_delete)

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
