from tkinter import *
from decimal import Decimal

# Window Settings
window = Tk()
window.title("Distance Converter")
window.minsize(width=325, height=150)
window.config(padx=25, pady=25)

# Choose conversions (drop down list)
OPTIONS = [
    "kilometer",
    "meter",
    "Centimeter",
    "Millimeter",
    "Micrometer",
    "Nanometer",
    "Yard",
    "Foot",
    "Inch",
]

choices_1 = StringVar(window)
choices_1.set(OPTIONS[0])

choice_1 = OptionMenu(window, choices_1, *OPTIONS)
choice_1.grid(column=1, row=1)

choices_2 = StringVar(window)
choices_2.set(OPTIONS[0])

choice_2 = OptionMenu(window, choices_2, *OPTIONS)
choice_2.grid(column=3, row=1)


# Convert Units to feet and to meters and scientific notation

def feet_meters_conversions(input, conversion):

    if conversion == "to_feet":
        input *= 3.281
        return input
    if conversion == "to_meters":
        input /= 3.281
        return input


def meters_conversions(input, selection, conversion):
    meters = float(input)
    
    if conversion == "to_meters":
        if selection == "kilometer":
            meters *= 1000

        if selection == "Centimeter":
            meters *= 0.01

        if selection == "Millimeter":
            meters *= 0.001

        if selection == "Micrometer":
            meters *= 1e-6

        if selection == "Nanometer":
            meters *= 1e-9

 
    if conversion == "from_meters":
        if selection == "kilometer":
            meters /= 1000

        elif selection == "Centimeter":
            meters /= 0.01

        elif selection == "Millimeter":
            meters /= 0.001

        elif selection == "Micrometer":
            meters /= 1e-6

        elif selection == "Nanometer":
            meters /= 1e-9
        elif selection == ("Yard" or "Feet" or "Inch"):
            meters = feet_meters_conversions(meters, conversion="to_feet")
            
              
    return meters


def foot_conversions(input, selection, conversion):
    feet = float(input)
    if conversion == "to_feet":
        if selection == "Yard":
            feet *= 3
            
        if selection == "Inch":
            feet /= 12
    
    if conversion == "from_feet":
        if selection == "Yard":
            feet /= 3

        elif selection == "Inch":
            feet *= 12
        
        elif "meter" in selection:
            feet = feet_meters_conversions(feet, conversion="to_meters")
        
   
    return feet


def convert_to_sci_notation(input):
    if 0.001 > input or input > 1000000:
        result = '%.2E' % Decimal(input)
    else:
        result = round(input, 2)
    return result


# Calculate the result of the given input

def input_to_base():
    selection_1 = choices_1.get()
    if "meter" in selection_1:
        base_unit = meters_conversions(unit_input.get(), selection_1, conversion="to_meters")
        return base_unit

    else:
        base_unit = foot_conversions(unit_input.get(), selection_1, conversion="to_feet")
        return base_unit


def calculate_result():
    selection_1 = choices_1.get()
    selection_2 = choices_2.get()
    base_units = input_to_base()
    
    if "meter" in selection_1 and "meter" in selection_2:
    
        from_meters = meters_conversions(base_units, selection_2, conversion="from_meters")
        meters_result = convert_to_sci_notation(from_meters)
        output_result.config(text=meters_result)
        
    elif (selection_2 == ("Yard" or "Foot" or "Inch")) and (selection_1 == ("Yard" or "Foot" or "Inch")):
        to_from_feet = foot_conversions(base_units, selection_2, conversion="from_feet")
        feet_result = convert_to_sci_notation(to_from_feet)
        output_result.config(text=feet_result)
    else:
        if "meter" not in selection_1 and "meter" in selection_2:
            from_feet = feet_meters_conversions(base_units, conversion="to_meters")
            to_unit = meters_conversions(from_feet, selection_2, conversion="from_meters")
            result = convert_to_sci_notation(to_unit)
            output_result.config(text=result)
        else:
            from_meters = feet_meters_conversions(base_units, conversion="to_feet")
            to_unit = foot_conversions(from_meters, selection_2, conversion="from_feet")
            result = convert_to_sci_notation(to_unit)
            output_result.config(text=result)
            





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
