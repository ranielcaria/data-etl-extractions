from api.core.insert import PostgresLoader
from tkinter import messagebox as msg
from shutil import move as move
import os

class ETLPipeline:
    def __init__(self, extractor, connection):
        self.extractor = extractor
        self.connection = connection
        self.loader = PostgresLoader()

    def move_file(self, extractor):
        from datetime import datetime
        try:
            move(extractor.file_path, \
                 extractor.file_path.replace("input", "archive")
                 .replace(".xls", \
                f" [{datetime.now().strftime('%d-%m-%Y %H-%M-%S')}].xls"))
        except FileNotFoundError:
            msg.showerror('File Not Found')
        except Exception:
            msg.showerror(f'Error: {Exception}')

    def run(self):
        extractor = self.extractor()
        rows = extractor.run()
        self.loader.insert(
            conn=self.connection,
            table=extractor.table,
            columns=extractor.columns,
            rows=rows,
            conflict=extractor.conflict
        )
        self.move_file(extractor)
