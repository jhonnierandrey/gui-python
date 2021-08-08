from tkinter import *
from datetime import datetime

App = Tk()
App.title('Age Calculator')
App.geometry('300x200')

lbl = Label(App, text='Enter your birthday')
lbl.grid(row=0, column=0, columnspan=6, padx=25, pady=5)

day_lbl = Label(App, text='Day: ')
day_entry = Entry(App, width=2)

month_lbl = Label(App, text='Month: ')
month_entry = Entry(App, width=2)

year_lbl = Label(App, text='Year: ')
year_entry = Entry(App, width=4)

day_lbl.grid(row=1, column=0)
day_entry.grid(row=1, column=1)

month_lbl.grid(row=1, column=2)
month_entry.grid(row=1, column=3)

year_lbl.grid(row=1, column=4)
year_entry.grid(row=1, column=5)

# functions

def find_days():
    date = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    dob = datetime(day=date, month=month, year=year)

    time_now = datetime.now()

    time_diff = time_now - dob

    days = Label(App, text='You lived ' + str(time_diff.days) + ' days!')
    days.grid(row=3, column=0, columnspan=3, padx=25, pady=5)

def find_seconds():
    date = int(day_entry.get())
    month = int(month_entry.get())
    year = int(year_entry.get())

    dob = datetime(day=date, month=month, year=year)

    time_now = datetime.now()
    time_diff = time_now - dob

    scs = Label(App, text='You lived ' + str(time_diff.total_seconds()) + ' seconds!')
    scs.grid(row=4, column=0, columnspan=6, padx=25, pady=5)

# buttons

days_btn = Button(App, text='Total days', command=find_days)
seconds_btn = Button(App, text='Total seconds', command=find_seconds)

days_btn.grid(row=2, column=0, columnspan=3, padx=25, pady=5)
seconds_btn.grid(row=2, column=3, columnspan=3, padx=25, pady=5)


App.mainloop()
