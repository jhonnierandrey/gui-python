from tkinter import *
from tkinter.filedialog import test
from typing import Collection

App = Tk()
App.title('Ico converter')

def open_img():
    from PIL import Image
    from tkinter import filedialog
    global img

    App.img_dir = filedialog.askopenfilename(initialdir='.', title='Select your image', filetypes=(
        ('PNG Images', '*.png'), ('JPG Images', '*.jpg'), ('All Files', '*.*')
    ))

    img = Image.open(App.img_dir)

def conv_img():
    from PIL import Image
    img.save(f'{ico_name.get()}.ico', format='ICO', sizes=[(ico_size.get(), ico_size.get())])

    success = Toplevel()
    success.title('Success')

    msg = Label(success, text='Conversion completed.')
    msg.pack()

    success.mainloop()

def preview():
    prev = Toplevel()
    prev.title('Icon preview')

    prev.iconbitmap(f'{ico_name.get()}.ico')

    prev_lbl = Label(prev, text='Preview your ico.')
    prev_lbl.pack()

    prev.mainloop()

choose_lbl = Label(App, text='Select your image: ')
choose_lbl.grid(row=0, column=0, padx=25, pady=5)

choose_btn = Button(App, text='Choose', command=open_img)
choose_btn.grid(row=0, column=1, padx=25, pady=5)

size_lbl = Label(App, text='Select a size for your ico')
size_lbl.grid(row=1, column=0, padx=25, pady=5)

ico_size = IntVar()
sizes_options = [ 16, 24, 32, 48, 64, 128, 256]
ico_size.set(sizes_options[2])

size_menu = OptionMenu(App, ico_size, *sizes_options)
size_menu.grid(row=1, column=1, padx=25, pady=5)

fname_lbl = Label(App, text='Enter the ico name: ')
fname_lbl.grid(row=2, column=0, padx=25, pady=5)

ico_name = Entry(App)
ico_name.grid(row=2, column=1, padx=25, pady=5)

convert_btn = Button(App, text='Convert', command=conv_img)
convert_btn.grid(row=3, column=0, padx=25, pady=5)

preview_btn = Button(App, text='Preview', command=preview)
preview_btn.grid(row=3, column=1, padx=25, pady=5)

App.mainloop()