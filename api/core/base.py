from abc import ABC, abstractmethod

class BaseExtractor(ABC):
    file_path: str
    spreadsheet: str
    columns: list[str]
    conflict: str | None = None

    def extract(self):
        import pandas as pd
        
        return pd.read_excel(self.file_path)
        
    @abstractmethod
    def transform(self, df) -> list[dict]:
        pass
    
    def run(self) -> list[dict]:
        return self.transform(self.extract())