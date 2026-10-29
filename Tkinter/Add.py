import tkinter as tk

window = tk.Tk()

def add():
    a = int(e1.get())
    b = int(e2.get())
    label.config(text=a + b)

e1 = tk.Entry(window)
e1.pack()

e2 = tk.Entry(window)
e2.pack()

button = tk.Button(window, text="Add", command=add)
button.pack()

label = tk.Label(window, text="")
label.pack()

window.mainloop()

##entry box
import tkinter as tk

window = tk.Tk()

entry = tk.Entry(window)
entry.pack()

window.mainloop()


##label  
import tkinter as tk

window = tk.Tk()

label = tk.Label(window, text="Hello World")
label.pack()

window.mainloop()


##window 
import tkinter as tk

window = tk.Tk()

window.title("My Window")
window.geometry("420x300")

window.mainloop()