from tkinter import *

window = Tk()

window.title("miles to km")
window.minsize(width=200,height=200)
window.config(bg="white")


#Labels
miles_label = Label(text="Miles", font=("Arial", 12))
km_label = Label(text="Km", font=("Arial", 12))
iet_label = Label(text="Is equal to", font=("Arial", 12))
answer_label = Label(text="0", font=("Arial", 12))
miles_label.config(bg="white")
km_label.config(bg="white")
iet_label.config(bg="white")
answer_label.config(bg="white")

#inputs
input = Entry(width=10)



#buttons
def button_click():
    try:
        new_text = float(input.get()) * 1.609344
        answer_label.config(text = f"{new_text:.2f}")
    except ValueError:
        answer_label.config(text = f"Invalid input")


button = Button(text="convert", command=button_click)
button.config(bg="white",width=5, height=1)



button.grid(row=2,column=1,padx=0,pady=0)
input.grid(row=0,column=1,padx=0,pady=0)
miles_label.grid(row=0,column=2,padx=0,pady=0)
km_label.grid(row=1,column=2,padx=0,pady=0)
iet_label.grid(row=1,column=0,padx=0,pady=0)
answer_label.grid(row=1,column=1,padx=0,pady=0)

window.mainloop()