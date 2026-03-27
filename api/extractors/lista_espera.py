from api.core.base import BaseExtractor
from api.core.transformers import parse_date

class ListaDeEsperaPorEspecialidade(BaseExtractor):
    file_path = 'api/input/Lista de espera por especialidade - Analítico.xls'
    
    table = 'lista_de_espera_por_especialidade'
    columns = [
        'especialidade',
        'data_hora',
        'prioridade',
        'situacao',
        'profissional',
        'unidade'
    ]
    conflict = '(especialidade, data_hora, prioridade, situacao, profissional, unidade)'
    
    def transform(self, df):
        registros = []
        especialidade = data = prioridade = situacao = unidade = profissional = None
        
        for _, row in df.iterrows():
            
            # Especialidade
            if 'Especialidade:' in str(row.iloc[1]):
                especialidade = str(row.iloc[1]).title()

            # Data
            if '/' in str(row.iloc[14]):
                data = parse_date(str(row.iloc[14]))

            # Prioridade
            if not 'Nan' in str(row.iloc[16]).title():
                prioridade = str(row.iloc[16]).title()
            
            # Situação
            if not 'nan' in str(row.iloc[19]):
                situacao = str(row.iloc[19])
                
            # Profissional
            if str(row.iloc[22]) not in ['nan', 'Profissional solicitante']:
                profissional = str(row.iloc[22]).title()

            # Unidade
            if str(row.iloc[24]).lower() not in ['nan', 'unidade solicitante']:
                unidade = str(row.iloc[24]).title()

            if not data:
                continue
                
            registros.append({
                'especialidade': especialidade,
                'data_hora': data,
                'prioridade': prioridade,
                'situacao': situacao,
                'profissional': profissional,
                'unidade': unidade
            })
        
        return registros
        
if __name__ == "__main__":
    extractor = ListaDeEsperaPorEspecialidade()
    
    dados_finais = extractor.run()
    
    print('--- header ---')
    
    for r in dados_finais[:5]:
        print(r)
    
    print(f"--- fim, {len(dados_finais)} registros ---")
