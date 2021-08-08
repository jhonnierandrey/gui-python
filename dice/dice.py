from tkinter import *
from typing import Collection

die = {
    0 : '🎲',
    1 : '⚀',
    2 : '⚁',
    3 : '⚂',
    4 : '⚃',
    5 : '⚄',
    6 : '⚅'
}

App = Tk()

App.title('Dice')
App.geometry('300x200')

App['background'] = 'black'

dice = Label(App, text=die[0], font=('Times', 100), background='black', width=5)
dice.grid(row=0, column=0, padx=25, pady=5)

def roll():
    from random import randint
    i = randint(1, 6)
    msg = Label(App, text=die[i], font=('Times', 100), background='black', foreground='white', width=5)
    msg.grid(row=0, column=0, padx=25, pady=5)

btn = Button(App, text='    Roll    ', command=roll)
btn.grid(row=1, column=0, columnspan=2)

App.mainloop()