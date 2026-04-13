from api.core.base import BaseExtractor

class example_extractor(BaseExtractor):
    file_path = 'api/input/example.xls'
    table = 'example'
    columns = ['example']

    def transform(self, df):
        registros = []

        for _, row in df.iterrows():
            coluna1 = str(row.iloc[0]).strip()

            registros.append({
                'example': coluna1 
            })

        return registros
    
def run_example(conn):
    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(example_extractor, conn)
    pipe.run()
