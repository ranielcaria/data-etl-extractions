import os
import shutil
from tkinter import filedialog, messagebox

def input_file():
    home_dir = os.path.expanduser('~')
    downloads_dir = os.path.join(home_dir, 'Downloads')

    source_file = filedialog.askopenfilename(
        initialdir=downloads_dir,
        title='Selecione um Relatório',
        filetypes=[('Excel File', '*.xls *.xlsx')]
    )

    if not source_file or source_file == '':
        return
    
    destination_folder = './api/input'
    filename = os.path.basename(source_file)
    destination_folder = os.path.join(destination_folder, filename)

    try:
        shutil.move(source_file, destination_folder)
        messagebox.showinfo('Sucesso!')
    except shutil.Error as e:
        messagebox.showerror(f'Falha! Erro: {e}')
    except OSError as e:
        messagebox.showerror(f'Falha! Erro: {e}')