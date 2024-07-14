
from tkinter import messagebox
import tkinter as tk

# Converter Calculations
def Celsius_to_Fahrenheit(Temperature):
    return round((Temperature * 9/5) + 32, 2)

def Celsius_to_Kelvin(Temperature):
    return round(Temperature + 273.15, 2)

def Fahrenheit_to_Celsius(Temperature):
    return round((Temperature - 32) * 5/9, 2)

def Fahrenheit_to_Kelvin(Temperature):
    return round((Temperature - 32) * 5/9 + 273.15, 2)

def Kelvin_to_Celsius(Temperature):
    return round(Temperature - 273.15, 2)

def Kelvin_to_Fahrenheit(Temperature):
    return round((Temperature - 273.15) * 9/5 + 32, 2)


# Converter
def show_message():
    Temperature = int(E1.get())
    Unit = E2.get()

    if Unit == 'C':
        Fahrenheit = Celsius_to_Fahrenheit(Temperature)
        Kelvin = Celsius_to_Kelvin(Temperature)
        messagebox.showinfo("Temperature", f"Fahrenheit = {Fahrenheit} F° \nKelvin = {Kelvin} K°")

    elif Unit == 'F':
        Celsius = Fahrenheit_to_Celsius(Temperature)
        Kelvin = Fahrenheit_to_Kelvin(Temperature)
        messagebox.showinfo("Temperature", f"Celsius = {Celsius} C° \nKelvin = {Kelvin} K°")

    elif Unit == 'K':
        Celsius = Kelvin_to_Celsius(Temperature)
        Fahrenheit = Kelvin_to_Fahrenheit(Temperature)
        messagebox.showinfo("Temperature", f"Celsius = {Celsius} C° \nFahrenheit = {Fahrenheit} F°")

    else:
        messagebox.showinfo("Input Error", "Enter a valid Unit (C, F, or K)!")

# Window
root = tk.Tk()
root.title('Temperature Converter')
root.geometry('450x200')
root.resizable(False, False)
FONT = ("Calibri", 12)

# Labels
L1 = tk.Label(root, text="Enter the Temperature Value:", font=FONT)
L1.place(x=20, y=45)
L2 = tk.Label(root, text="Enter the Temperature Unit:\n Enter (C/F/K)", font=FONT)
L2.place(x=20, y=85)

# Entry Box
E1 = tk.Entry(root)
E1.place(x=225, y=48)
E2 = tk.Entry(root)
E2.place(x=215, y=88)

# Button
B1 = tk.Button(root, text="Convert", font=FONT, command=show_message)
B1.place(x=350, y=140)

# Run
root.mainloop()
