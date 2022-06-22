import tkinter

my_window=tkinter.Tk()
my_window.title("Hello World")
my_window.minsize(width=500,height=300)

name_label=tkinter.Label(text="Name:", font=("Arial",12,"italic"))
# name_label.pack(side="left")
# name_label.pack(side="bottom")
# name_label.pack(expand=True)
name_label.pack()

my_window.mainloop()