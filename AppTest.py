import tkinter as tk
from tkinter import ttk

# Creating the main window for the application
window = tk.Tk()

# Setting the title of the window
frame1 = tk.Frame(master=window, height=200, bg='gray', border=3).pack(side=tk.LEFT, fill=tk.X)

# Getting user entry using an Entry widget
frame2 = tk.Frame(master=window, height=50, bg='red').pack(side=tk.BOTTOM, fill=tk.BOTH)

# Adding a button to the window
frame3 = tk.Frame(master=window, height=50, bg='blue').pack(side=tk.TOP, fill=tk.BOTH)


# Starting the application
window.mainloop()