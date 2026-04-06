from api.core.base import BaseExtractor
from api.core.transformers import parse_datetime

class ProcedimentosPorProfissional(BaseExtractor):
    file_path = 'api/input/Procedimentos realizados por profissional - Analítico.xls'
    
    table = 'procedimentos_por_profissional'
    columns = ['unidade','profissional', 'especialidade', 'procedimento', 'quantidade', 'data_hora', 'sexo', 'idade']
    conflict = '(unidade, profissional, especialidade, procedimento, data_hora)'
    
    def transform(self, df):
        registros = []
        unidade = profissional = procedimento = data = quantidade = None
        
        for _, row in df.iterrows():
            if 'Unidade:' in str(row.iloc[1]):
                unidade = str(row.iloc[1]).replace('Unidade: ', '').title()
                
            if 'Profissional:' in str(row.iloc[4]):
                profissional = str(row.iloc[4]).replace('Profissional: ', '').title()
                
            if 'Procedimento:' in str(row.iloc[5]):
                procedimento = str(row.iloc[5]).title().split(' - ')[-1]
                
            if '/' in str(row.iloc[6]):
                data = parse_datetime(str(row.iloc[6]))
    
            if not data:
                continue
            
            registros.append({
                'unidade': unidade,
                'profissional': profissional,
                'procedimento': procedimento,
                'quantidade': str(row.iloc[45]) if 'nan' not in str(row.iloc[45]) else quantidade,
                'data_hora': data,
                'sexo': row.iloc[36],
                'idade': row.iloc[38]
            })

        return registros


def run_procedimentos_profissional(conn):
    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(ProcedimentosPorProfissional, conn)
    pipe.run()
