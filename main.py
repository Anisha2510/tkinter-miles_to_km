from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.689
    km_result.config(text=f"{km}")


window = Tk()
window.title("Miles to km Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="Is equal to: ")
is_equal_to.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

cal_button = Button(text="Calculate", command=miles_to_km)
cal_button.grid(column=1, row=2)

window.mainloop()
