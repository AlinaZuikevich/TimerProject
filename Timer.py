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

canvas.create_window((105, 100), anchor="nw", window=h_combo)
canvas.create_window((210, 100), anchor="nw", window=m_combo)
canvas.create_window((315, 100), anchor="nw", window=s_combo)

window.option_add("*TCombobox*Listbox*Background", "#EEEDF2")
window.option_add("*TCombobox*Listbox*Foreground", "#806E5A")
window.option_add("*TCombobox*Listbox*Font", "Arial 12")

combostyle = ttk.Style()
combostyle.theme_use("clam")
combostyle.configure('TCombobox', background="#EEEDF2", fieldbackground="#EEEDF2",
                     foreground="0", darkcolor="White", selectbackground="#635A52",
                     lightcolor="White")

h_text = canvas.create_text(190, 145, text='h', fill="Black", font="Arial 20")
m_text = canvas.create_text(300, 145, text='m', fill="Black", font="Arial 20")
s_text = canvas.create_text(400, 145, text='s', fill="Black", font="Arial 20")


def clear_date():
    hour.set("0")
    minute.set("0")
    second.set("0")


clear_butt = Image.open('img/clear.png')
clear_butt = ImageTk.PhotoImage(clear_butt .resize((150, 42)))
clear = Button(window, image=clear_butt, highlightthickness=0, bd=0, command=clear_date)
canvas.create_window((185, 265), anchor="nw", window=clear)

cancel_butt = Image.open("img/cancel.png")
cancel_butt = ImageTk.PhotoImage(cancel_butt.resize((160, 45)))

stop_butt = Image.open('img/stop.png')
stop_butt = ImageTk.PhotoImage(stop_butt.resize((66, 50)))

play_butt = Image.open('img/play.png')
play_butt = ImageTk.PhotoImage(play_butt.resize((66, 50)))

Timer_id = ''


def start_click():
    forg = [h_combo, m_combo, s_combo, start, clear]
    for i in forg:
        i.destroy()

    text = [h_text, m_text, s_text]
    for q in text:
        canvas.itemconfig(q, state='hidden')

    def cancel_timer():
        window.after_cancel(Timer_id)
        messagebox.showinfo('Time Countdown', 'Timer is off')
        window.quit()

    cancel = Button(window, image=cancel_butt, highlightthickness=0, bd=0, command=cancel_timer)
    canvas.create_window((185, 265), anchor="nw", window=cancel)

    h = int(hour.get())
    m = int(minute.get())
    s = int(second.get())

    lbl = canvas.create_text(265, 130, text='{:02d}:{:02d}:{:02d}'.format(h, m, s),
                             fill="Black", font="Arial 50")

    def countdown():
        global Timer_id
        nonlocal h, m, s

        window.update()

        if s != 0:
            s -= 1
        elif m != 0 and s == 0:
            m -= 1
            s += 59
        elif h != 0 and m == 0 and s == 0:
            h -= 1
            m += 59
            s += 59
        else:
            messagebox.showinfo('Time Countdown', 'Time is over')
            window.after_cancel(Timer_id)
            window.quit()

        canvas.itemconfigure(lbl, text='{:02d}:{:02d}:{:02d}'.format(h, m, s))
        Timer_id = window.after(1000, countdown)

    countdown()

    def stop_click():
        global Timer_id
        if Timer_id:
            window.after_cancel(Timer_id)
        stop.config(state=DISABLED)
        play.config(state=NORMAL)

    def play_click():
        stop.config(state=NORMAL)
        play.config(state=DISABLED)
        countdown()

    stop = Button(window, image=stop_butt, highlightthickness=0, bd=0, command=stop_click)
    play = Button(window, image=play_butt, highlightthickness=0, bd=0, command=play_click)

    canvas.create_window((195, 205), anchor="nw", window=stop)
    canvas.create_window((270, 205), anchor="nw", window=play)


start_butt = Image.open('img/start.png')
start_butt = ImageTk.PhotoImage(start_butt.resize((150, 42)))
start = Button(window, image=start_butt, highlightthickness=0, bd=0, command=start_click)
canvas.create_window((185, 215), anchor="nw", window=start)

window.mainloop()
