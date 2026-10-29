import tkinter as tk

window = tk.Tk()

def show():
    name = entry.get()
    label.config(text=name)

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Submit", command=show)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()