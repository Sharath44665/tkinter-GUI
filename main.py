# import tkinter
from tkinter import *

my_window = Tk()
my_window.title("Hello World")
my_window.minsize(width=500, height=300)

name_label = Label(text="Name:", font=("Arial", 12, "italic"))
# name_label.pack(side="left")
# name_label.pack(side="bottom")
# name_label.pack(expand=True)
name_label.pack()

user_input=Entry()
user_input.pack()


def on_click_button():
    # print("Wow, you cliked?!")
    # name_label["text"]="Change the name"
    # name_label.config(text="you clicked on Button")
    user_value= user_input.get()
    name_label.config(text=user_value)

click_button = Button(text="Click Me", command=on_click_button)

click_button.pack()
my_window.mainloop()
