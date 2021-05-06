from tkinter import *
from decimal import Decimal

conversion_dictionary = {
    "meter": 1,
    "kilometer": 0.001,
    "Centimeter": 100,
    "Millimeter": 1000,
    "Micrometer": 1E+6,
    "Nanometer": 1E+9,
    "Yard": 1.09361,
    "Foot": 3.28,
    "Inch": 39.3701,
    "Mile": 0.000621,
    "Nautical mile": (1/1852),
}

# Window Settings
window = Tk()
window.title("Distance Converter")
window.config(padx=25, pady=25)

# Choose conversions (drop down list)
OPTIONS = [key for key in conversion_dictionary.keys()]

choices_1 = StringVar(window)
choices_1.set(OPTIONS[0])

choice_1 = OptionMenu(window, choices_1, *OPTIONS)
choice_1.grid(column=1, row=1)

choices_2 = StringVar(window)
choices_2.set(OPTIONS[0])

choice_2 = OptionMenu(window, choices_2, *OPTIONS)
choice_2.grid(column=3, row=1)



def convert_to_sci_notation(input):
    """Converts input to scientific notation if lower than 0.001 or greater than 1,000,000."""
    if 0.001 > input or input > 1000000:
        result = '%.2E' % Decimal(input)
    else:
        result = round(input, 3)
    return result


def calculate_result():
    """Calculates the result of the inputted number and selected conversions."""
    selection_1 = choices_1.get()
    selection_2 = choices_2.get()
    multiplyer = float(unit_input.get()) / conversion_dictionary[selection_1]
    result = conversion_dictionary[selection_2] * multiplyer
    final_result = convert_to_sci_notation(result)
    output_result.config(text=final_result)
    
# Input value to be converted
unit_input = Entry(width=10)
unit_input.insert(END, string=0)
unit_input.grid(column=2, row=1)


# Button config
button = Button(text="Calculate", command=calculate_result)
button.grid(column=2, row=3)

# Text on screen

output_result = Label(text=0)
output_result.grid(column=2, row=2)

# Blank space

blank_space_1 = Label(text=" ")
blank_space_1.grid(column=0, row=0)
blank_space_2 = Label(text=" ")
blank_space_2.grid(column=4, row=0)



window.mainloop()
