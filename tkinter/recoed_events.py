# _*_ coding:utf-8 _*_

import tkinter as tk
from tkinter import ttk
import datetime
import winsound

one_cm = 40


# --------------------------------------------------------------------------- window
window = tk.Tk()
window.title('Phika (Python Club)')

up_text = "Save your daily events" \
          "\n" \
          "ثبت وقایع و خاطرات روزانه"
up_label = ttk.Label(window, text=up_text).pack()


# --------------------------------------------------------------------------- exit btn
def exit_():
    window.destroy()


def submit():
    d = day.get()
    mo = month.get()
    y = year.get()
    ho = h.get()
    mi = m.get()
    status = am_pm.get()

    my_date = d, mo, y, ' --- ', ho, ':', mi, status
    print(my_date)

    cd = datetime.datetime.now()
    data = tb.get('1.0', 'end')
    print(cd, data)

    for i in range(3):
        winsound.Beep(400, 200)


def clear_textbox():
    tb.delete('1.0', '2.3 + 1 char')		# 1 char = \n


# --------------------------------------------------------------------------- datetime
year = tk.StringVar()
month = tk.StringVar()
day = tk.StringVar()
h = tk.StringVar()
m = tk.StringVar()
am_pm = tk.StringVar()

date_label = tk.Label(window, text='تاریخ')
date_label.place(x=380, y=8 * one_cm)

day = ttk.Combobox(window, textvariable=day)
day.place(x=20, y=8 * one_cm, width=100)

month = ttk.Combobox(window, textvariable=month)
month.place(x=130, y=8 * one_cm, width=100)

year = ttk.Combobox(window, textvariable=year)
year.place(x=240, y=8 * one_cm, width=100)

time_label = tk.Label(window, text='ساعت')
time_label.place(x=375, y=9 * one_cm)

h = ttk.Combobox(window, textvariable=h)
h.place(x=20, y=9 * one_cm, width=100)
m = ttk.Combobox(window, textvariable=m)
m.place(x=130, y=9 * one_cm, width=100)

am = ttk.Radiobutton(window, text='AM', variable=am_pm, value='AM').place(x=250, y=9 * one_cm)
pm = ttk.Radiobutton(window, text='PM', variable=am_pm, value='PM').place(x=300, y=9 * one_cm)


year.config(values=list(range(2019, 2030)))
month.config(values=['فروردین', 'اردیبهشت', 'خرداد',
                     'تیر', 'مرداد', 'شهریور',
                     'October', 'November', 'December',
                     'January', 'February', 'March'])
day.config(values=list(range(1, 32)))
h.config(values=list(range(24)))
m.config(values=list(range(60)))

# --------------------------------------------------------------------------- textbox
y = 2.3 * one_cm
tb_label = ttk.Label(text="What's up?")
tb_label.place(x=20, y=y)

tb = tk.Text(window, width=48, height=10)
y = 3 * one_cm
tb.place(x=20, y=y)
tb.config(wrap='word')
tb.insert('1.0', 'Write here ...')

y = 10.5 * one_cm
confirm_btn = ttk.Button(window, text='Submit', command=submit).place(x=20, y=y, width=250)
clear_btn = ttk.Button(window, text='Clear', command=clear_textbox).place(x=280, y=y, width=70)
exit_btn = ttk.Button(window, text='Exit', command=exit_).place(x=360, y=y, width=50)
# ---------------------------------------------------------------------------
window.mainloop()
