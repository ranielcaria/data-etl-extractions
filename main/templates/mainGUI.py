import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Forest")
root.option_add("*tearOff", False)

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

# Create a style
style = ttk.Style(root)

# Import the tcl file
root.tk.call("source", "./themes/forest-dark.tcl")

# Set the theme with the theme_use method
style.theme_use("forest-dark")