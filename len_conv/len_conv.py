from tkinter import *

App = Tk()
App.title('Length Converter')
# App.geometry('300x150')

scales = ['Meters', 'Inches', 'Foot']

from_ = StringVar()

from_menu = OptionMenu(App, from_, *scales)
from_menu.grid(row=0, column=0, padx=25, pady=5)
from_.set(scales[0])

lbl = Label(App, text=' convert to ')
lbl.grid(row=0, column=1, padx=25, pady=5)

to_ = StringVar()
to_menu = OptionMenu(App, to_, *scales)
to_menu.grid(row=0, column=2, padx=25, pady=5)
to_.set(scales[1])

enter_lbl = Label(App, text='Enter your length:')
enter_lbl.grid(row=1, column=0, padx=25, pady=5)

num_entry = Entry(App)
num_entry.grid(row=1, column=1, padx=25, pady=5)

def converter():
    c_from = from_.get()
    c_to = to_.get()
    c_num = int(num_entry.get())

    if c_from == 'Meters' and c_to == 'Inches':
        conv_num = c_num * 39.37
    elif c_from == 'Meters' and c_to == 'Foot':
        conv_num = c_num * 3.28
    elif c_from == 'Inches' and c_to == 'Meters':
        conv_num = c_num / 39.37
    elif c_from == 'Inches' and c_to == 'Foot':
        conv_num = c_num / 12
    elif c_from == 'Foot' and c_to == 'Meters':
        conv_num = c_num / 3.28
    elif c_from == 'Foot' and c_to == 'Inches':
        conv_num = c_num * 12
    else:
        conv_num = c_num

    num = Label(App, text=round(conv_num, 2), width=10)
    num.grid(row=1, column=2, padx=25, pady=5)

convert_btn = Button(App, text='CONVERT', command=converter, width=20)
convert_btn.grid(row=2, column=0, columnspan=3, padx=25, pady=5)

App.mainloop()
