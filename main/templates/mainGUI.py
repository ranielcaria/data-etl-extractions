import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("MENU")
#root.geometry('600x400')
root.option_add("*tearOff", False)
style = ttk.Style(root)
root.tk.call("source", "main/themes/forest-dark.tcl")
style.theme_use("forest-dark")

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=0)


# Frame
reportsframe = ttk.Labelframe(root, text='Relatórios', padding=(15, 15))
reportsframe.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky="nsew")
reportsframe.columnconfigure(0, weight=1)
reportsframe.columnconfigure(1, weight=1)

# Relatórios (dentro do Frame)
# Row 0
atdupa = ttk.Button(reportsframe, text='Atendimentos Upa')
atdupa.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

dispvagas = ttk.Button(reportsframe, text='Disp. Vagas')
dispvagas.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

# Row 1
listespera = ttk.Button(reportsframe, text='Espera p/ Proc')
listespera.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

procprof = ttk.Button(reportsframe, text='Proc. p/ Prof')
procprof.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

# Row 2
vacinas = ttk.Button(reportsframe, text='Vacinas Aplicadas')
vacinas.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

transfprod = ttk.Button(reportsframe, text='Transf Produtos')
transfprod.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

# Input e Exit
inputbtn = ttk.Button(root, text='Insert File', style="Accent.TButton")
inputbtn.grid(row=1, column=0, padx=(20, 10), pady=20, sticky='ew')

exitbtn = ttk.Button(root, text='Exit', command=root.destroy)
exitbtn.grid(row=1, column=1, padx=(10, 20), pady=20, sticky='ew')

root.mainloop()