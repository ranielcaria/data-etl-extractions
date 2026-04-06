from api.core.base import BaseExtractor
from api.core.transformers import parse_date

class TransferenciaProdutosExtractor(BaseExtractor):
    file_path = 'api/input/Transferência de produtos.xls'

    table = 'transferencia_de_produtos'
    columns = ['produto', 'origem', 'destino', 'quantidade', 'data']
    conflict = '(produto, origem, destino, quantidade, data)'

    def transform(self, df):
        registros = []

        quantidade = data = produto = origem = destino = None

        for _, row in df.iterrows():

            # Produto
            if 'Produto' in str(row.iloc[5]): produto = str(row.iloc[5]).removeprefix('Produto').split(' - ')[-1].strip()

            # Quantidade
            if not 'nan' in str(row.iloc[18]): quantidade = str(row.iloc[18]).split(',')[0]

            # Data
            if not 'nan' in str(row.iloc[29]).lower(): data = parse_date(row.iloc[29])

            # Origem
            if not 'nan' in str(row.iloc[2]): origem = str(row.iloc[2]).removeprefix(' Unidade / C. de custo Origem: ')

            # Destino
            if not 'nan' in str(row.iloc[4]): destino = str(row.iloc[4]).removeprefix(' Unidade / C. custo destino: ')

            if data and quantidade:
                registros.append({
                        'produto': produto,
                        'quantidade': quantidade,
                        'data': data,
                        'origem': origem,
                        'destino': destino
                    })

            quantidade = None

        return registros


def run_transferencia_produtos(conn):
    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(TransferenciaProdutosExtractor, conn)
    pipe.run()