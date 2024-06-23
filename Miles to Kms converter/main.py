from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    kms_result_label.config(text=f'{km}')

window = Tk()   
window.title("Miles to Kms Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 10, "normal"))
miles_label.grid(column=2, row=0)

is_equal_to = Label(text="is equal to",font=("Arial", 10, "normal"))
is_equal_to.grid(column=0, row=1)

kms_result_label = Label(text="0",font=("Arial", 10, "normal"))
kms_result_label.grid(column=1, row=1)

kms_label = Label(text="Km",font=("Arial", 10, "normal"))
kms_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km, font=("Arial", 11, "normal"))
calculate_button.grid(column=1, row=2)



window.mainloop()
