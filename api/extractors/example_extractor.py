from api.core.base import BaseExtractor

class example_extractor(BaseExtractor):

    # Toda classe nova DEVE ter essas três variáveis
    # sendo 'file_path' o caminho do arquivo excel que você vai extrair os dados,
    # 'table' o nome da tabela que você pretende inserir no banco de dados.
    # e por último, 'columns' que são as colunas da sua tabela
    # OBS: os nomes são case-sensitive, então escreva o nome de sua tabela, path e coluna
    # exatamente da forma como estão. 

    file_path = 'api/input/example.xls'
    table = 'example'
    columns = ['example']

    def transform(self, df):
        # Aqui vai ir a lógica da sua extração. 
        # Não se esqueça que essa função PRECISA retornar algo. de preferẽncia,
        # uma lista

        registros = []

        for _, row in df.iterrows():
            coluna1 = str(row.iloc[0]).strip()

            registros.append({
                'example': coluna1 
            })

        return registros
    
def run_example(conn):
    # Aqui temos um import do pipeline. só ponha o nome da sua classe
    # dentro da função chamada, e chame o arquivo 'conn' junto.

    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(example_extractor, conn)
    pipe.run()
