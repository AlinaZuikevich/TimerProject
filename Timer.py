import time
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk, Image

window = tk.Tk()
window.title("Timer")
window.resizable(width=False, height=False)
window.iconbitmap("img/timer-icon.ico")

image = Image.open("img/image.png")
width = 500
height = 322
image = ImageTk.PhotoImage(image.resize((width, height)))

canvas = tk.Canvas(window, width=width, height=height)
canvas.pack(side="top", fill="both", expand=0)

canvas.create_image(0, 0, anchor="nw", image=image)

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("0")
minute.set("0")
second.set("0")

opts = tuple(str(i) for i in range(60))

h_combo = ttk.Combobox(window, width=2, font=("Arial", 37), values=opts, textvariable=hour)
m_combo = ttk.Combobox(window, width=2, font=("Arial", 37), values=opts, textvariable=minute)
s_combo = ttk.Combobox(window, width=2, font=("Arial", 37), values=opts, textvariable=second)

canvas.create_window((90, 100), anchor="nw", window=h_combo)
canvas.create_window((200, 100), anchor="nw", window=m_combo)
canvas.create_window((310, 100), anchor="nw", window=s_combo)

window.option_add("*TCombobox*Listbox*Background", "#EEEDF2")
window.option_add("*TCombobox*Listbox*Foreground", "#806E5A")
window.option_add("*TCombobox*Listbox*Font", "Arial 12")

combostyle = ttk.Style()
combostyle.theme_use("clam")
combostyle.configure('TCombobox', background="#EEEDF2", fieldbackground="#EEEDF2",
                     foreground="0", darkcolor="White", selectbackground="#635A52",
                     lightcolor="White")

h_text = canvas.create_text(178, 145, text='h', fill="Black", font="Arial 20")
m_text = canvas.create_text(290, 145, text='m', fill="Black", font="Arial 20")
s_text = canvas.create_text(397, 145, text='s', fill="Black", font="Arial 20")


def countdown():

    forg = [h_combo, m_combo, s_combo, start, cancel]
    for i in forg:
        i.destroy()
    canvas.delete(h_text, m_text, s_text)

    cancel_time_butt = Image.open('img/canc_tm.png')
    cancel_time_butt = ImageTk.PhotoImage(cancel_time_butt.resize((200, 70)))
    cancel_time = Button(window, image=cancel_time_butt, highlightthickness=0, bd=0, command=window.destroy)
    canvas.create_window((165, 225), anchor="nw", window=cancel_time)

    h = int(hour.get())
    m = int(minute.get())
    s = int(second.get())

    lbl = canvas.create_text(255, 130, text='{:02d}:{:02d}:{:02d}'.format(h, m, s),
                             fill="Black", font="Arial 50")
    while h != 0 or m != 0 or s != 0:

        window.update()
        time.sleep(1)

        if s != 0:
            s -= 1
        elif m != 0 and s == 0:
            m -= 1
            s += 59
        elif h != 0 and m == 0 and s == 0:
            h -= 1
            m += 59
            s += 59

        canvas.itemconfigure(lbl, text='{:02d}:{:02d}:{:02d}'.format(h, m, s))

    messagebox.showinfo('Time Countdown', 'Время вышло')


start_butt = Image.open('img/start.png')
start_butt = ImageTk.PhotoImage(start_butt.resize((150, 52)))
start = Button(window, image=start_butt, highlightthickness=0, bd=0, command=countdown)
canvas.create_window((180, 205), anchor="nw", window=start)


def cancellation():
    hour.set("0")
    minute.set("0")
    second.set("0")


cancel_butt = Image.open('img/cancel.png')
cancel_butt = ImageTk.PhotoImage(cancel_butt.resize((150, 52)))
cancel = Button(window, image=cancel_butt, highlightthickness=0, bd=0, command=cancellation)
canvas.create_window((180, 265), anchor="nw", window=cancel)

window.mainloop()
