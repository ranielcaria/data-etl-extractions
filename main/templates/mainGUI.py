import tkinter as tk
from tkinter import ttk, messagebox
from api.core.input import input_file
from api.core.conn import postgres_connection
from api.core.pipeline import ETLPipeline

from api.extractors.atendimentos_upa import AtendimentosUpa
from api.extractors.disponibilidade_vagas import disponibilidade_vagas
from api.extractors.lista_espera import ListaDeEsperaPorEspecialidade
from api.extractors.procedimentos_profissional import ProcedimentosPorProfissional
from api.extractors.vacinas import VacinasAplicadas
from api.extractors.transferencia_produtos import TransferenciaProdutosExtractor

DB_CONFIG = "db_config.json"


def run_etl(extractor_cls, name: str):
    with postgres_connection(DB_CONFIG) as conn:
        pipe = ETLPipeline(extractor_cls, conn)
        pipe.run()
    messagebox.showinfo("Sucesso", f"ETL concluído para {name}")


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
atdupa = ttk.Button(
    reportsframe,
    text='Atendimentos Upa',
    command=lambda: run_etl(AtendimentosUpa, "Atendimentos UPA")
)
atdupa.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

dispvagas = ttk.Button(
    reportsframe,
    text='Disp. Vagas',
    command=lambda: run_etl(disponibilidade_vagas, "Disponibilidade de Vagas")
)
dispvagas.grid(row=0, column=1, padx=5, pady=5, sticky='ew')

# Row 1
listespera = ttk.Button(
    reportsframe,
    text='Espera p/ Proc',
    command=lambda: run_etl(ListaDeEsperaPorEspecialidade, "Lista de Espera")
)
listespera.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

procprof = ttk.Button(
    reportsframe,
    text='Proc. p/ Prof',
    command=lambda: run_etl(ProcedimentosPorProfissional, "Procedimentos por Profissional")
)
procprof.grid(row=1, column=1, padx=5, pady=5, sticky='ew')

# Row 2
vacinas = ttk.Button(
    reportsframe,
    text='Vacinas Aplicadas',
    command=lambda: run_etl(VacinasAplicadas, "Vacinas Aplicadas")
)
vacinas.grid(row=2, column=0, padx=5, pady=5, sticky='ew')

transfprod = ttk.Button(
    reportsframe,
    text='Transf Produtos',
    command=lambda: run_etl(TransferenciaProdutosExtractor, "Transferência de Produtos")
)
transfprod.grid(row=2, column=1, padx=5, pady=5, sticky='ew')

# Input e Exit
inputbtn = ttk.Button(root, command=input_file, text='Insert File', style="Accent.TButton")
inputbtn.grid(row=1, column=0, padx=(20, 10), pady=20, sticky='ew')

exitbtn = ttk.Button(root, text='Exit', command=root.destroy)
exitbtn.grid(row=1, column=1, padx=(10, 20), pady=20, sticky='ew')

root.mainloop()
