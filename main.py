from tkinter import messagebox
import tkinter as tk

# Converter Calculations
def Celcius_to_Farenhiet(Temperature):
    global Farenhiet
    Farenhiet = round((Temperature * (9 / 5)) + 32, 2)


def Celcius_to_Kelvin(Temperature):
    global Kelvin
    Kelvin = round(Temperature + 273.15, 2)


def Farenhiet_to_Celcius(Temperature):
    global Celcius
    Celcius = round((Temperature - 32) * (5 / 9), 2)


def Farenhiet_to_Kelvin(Temperature):
    global Kelvin
    Kelvin = round(((Temperature - 32) * (5 / 9)) + 273.15, 2)


def Kelvin_to_Celcius(Temperature):
    global Celcius
    Celcius = round(Temperature - 273.15, 2)


def Kelvin_to_Farenhiet(Temperature):
    global Farenhiet
    Farenhiet = round(((Temperature - 273.15) * (9 / 5)) + 32, 2)


# Converter
def show_message():
    Temperature = int(E1.get())
    Unit = E2.get()

    if Unit == 'C':
        Celcius_to_Farenhiet(Temperature)
        Celcius_to_Kelvin(Temperature)
        messagebox.showinfo("Temperature", f"Farenhiet = {Farenhiet} F° \nKelvin = {Kelvin} K°")

    elif Unit == 'F':
        Farenhiet_to_Celcius(Temperature)
        Farenhiet_to_Kelvin(Temperature)
        messagebox.showinfo("Temperature", f"Celcius = {Celcius} C° \nKelvin = {Kelvin} K°")

    elif Unit == 'K':
        Kelvin_to_Celcius(Temperature)
        Kelvin_to_Farenhiet(Temperature)
        messagebox.showinfo("Temperature", f"Celcius = {Celcius} C° \nFarenhiet = {Farenhiet} F°")

    else:
        messagebox.showinfo("Input Error", "Enter a valid Unit!")

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
