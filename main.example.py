import traceback
import tkinter as tk
from tkinter import ttk, messagebox
from api.core.input import input_file
from api.core.conn import postgres_connection
from api.core.pipeline import ETLPipeline
from api.core.docker_up import run_docker_up 
from api.extractors.example_extractor import example_extractor

DB_CONFIG = "db_config.json"

def run_etl(extractor_cls, name: str):
    try:
        with postgres_connection(DB_CONFIG) as conn:
            pipe = ETLPipeline(extractor_cls, conn)
            pipe.run()
        messagebox.showinfo("Sucesso", f"ETL concluído para {name}")
    except Exception:
        messagebox.showerror("Erro", traceback.format_exc())

root = tk.Tk()
docker_status = tk.BooleanVar(value=False)
root.title("MENU")
#root.geometry('600x400')
root.option_add("*tearOff", False)
style = ttk.Style(root)
root.tk.call("source", "themes/forest-dark.tcl")
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
example_button = ttk.Button(
    reportsframe,
    text='Exemplo',
    command=lambda: run_etl(example_extractor, "example_extractor")
)
example_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

example_button2 = ttk.Button(
    reportsframe,
    text='',
    command=''
    #command=lambda: run_etl(your_extraction_class_here, "the_name_of_your_class")
)
example_button2.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

# Row 1
example_button3 = ttk.Button(
    reportsframe,
    text='',
    command=''
    #command=lambda: run_etl(your_extraction_class_here, "the_name_of_your_class")
)
example_button3.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

example_button4 = ttk.Button(
    reportsframe,
    text='',
    command=''
    #command=lambda: run_etl(your_extraction_class_here, "the_name_of_your_class")
)
example_button4.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

# Row 2
example_button5 = ttk.Button(
    reportsframe,
    text='',
    command=''
    #command=lambda: run_etl(your_extraction_class_here, "the_name_of_your_class")
)
example_button5.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

example_button6 = ttk.Button(
    reportsframe,
    text='',
    command=''
    #command=lambda: run_etl(your_extraction_class_here, "the_name_of_your_class")
)
example_button6.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

# Input, Docker Up e Exit
dockerbtn = ttk.Checkbutton(root, text='OFF/ON', style='Switch', 
                            variable=docker_status,
                            command=lambda:run_docker_up(docker_status))
dockerbtn.grid(row=1, column=0, padx=(20), pady=(10, 0), sticky='w')

inputbtn = ttk.Button(root, command=input_file, text='Inserir arquivo', style="Accent.TButton")
inputbtn.grid(row=2, column=0, padx=(20, 10), pady=20, sticky='ew')

exitbtn = ttk.Button(root, text='Fechar Programa', command=root.destroy)
exitbtn.grid(row=2, column=1, padx=(10, 20), pady=20, sticky='ew')

root.mainloop()
