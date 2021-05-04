from tkinter import *

# Window Settings
window = Tk()
window.title("Mile to Km converter")
window.minsize(width=200, height=100)
window.config(padx=25, pady=25)

OPTIONS = [
    "kilometer",
    "Meter",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Mile",
    "Yard",
    "Foot",
    "Inch",
    "Nautical Mile"
]

# choices = StringVar(window)
# choices.set(OPTIONS[0])

# choice_1 = OptionMenu(window, choices, *OPTIONS)
# choice_1.grid(column=0, row=0)

def convert_entry():
    miles = miles_input.get()
    kilometre = float(miles) * 1.609344
    output_result.config(text=round(kilometre, 2))


# Input
miles_input = Entry(width=10)
miles_input.insert(END, string=0)
miles_input.grid(column=1, row=0)


# Button config
button = Button(text="Calculate", command=convert_entry)
button.grid(column=1, row=2)


# Text on screen
label_1 = Label(text="Miles")
label_1.grid(column=2, row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=0, row=1)

output_result = Label(text=0)
output_result.grid(column=1, row=1)

label_3 = Label(text="Km")
label_3.grid(column=2, row=1)





window.mainloop()
