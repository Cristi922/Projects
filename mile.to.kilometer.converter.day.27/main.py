from tkinter import *

def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

window = Tk()
window.title("Mile to kilometer converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

#Label equal to
equal_label = Label(text="is qual to:")
equal_label.grid(column=0, row=1)

#Label Miles
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label calculated
kilometer_result_label = Label(text="0")
kilometer_result_label.grid(column=1, row=1)

#Label Km
km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Entry
miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)

# Button Calculate
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)






window.mainloop()