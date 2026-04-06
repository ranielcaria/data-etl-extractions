from api.core.base import BaseExtractor
from api.core.transformers import parse_date

class disponibilidade_vagas(BaseExtractor):
    file_path = 'api/input/Disponibilidade de vagas para consulta - CSM.xls'
    
    table = 'disponibilidade_de_vagas_por_consulta'
    columns = [
        'unidade',
        'profissional',
        'especialidade',
        'vagas',
        'agendadas',
        'disponiveis',
        'data'
    ]
    conflict = '(unidade, profissional, especialidade, data)'
    
    def transform(self, df):
        registros = []
        data = unidade = profissional = especialidade = vagas = agendadas = disponiveis = None
        
        for _, row in df.iterrows():
            
            # Data
            if '/' in str(row.iloc[3]):
                data = parse_date(str(row.iloc[3]))
                #registros.append(data)
            
            # Unidade
            if 'Unidade: ' in str(row.iloc[5]):
                unidade = row.iloc[5].replace('Unidade: ', '').title()
                #registros.append(unidade)
            
            # Profissional
            if str(row.iloc[6]).lower() not in ['nan', 'Nome do Profissional']:
                profissional = row.iloc[6].title()
                #registros.append(profissional)
            
            # Especialidade
            if str(row.iloc[14]).lower() not in ['nan', 'Especialidade']:
                especialidade = row.iloc[14].title()
                #registros.append(especialidade)
        
            # Vagas
            if not 'nan' in str(row.iloc[20]).strip():
                vagas = int(row.iloc[20]) 
                #registros.append(vagas)
                
            # Agendadas
            if not 'nan' in str(row.iloc[28]).strip():
                agendadas = int(row.iloc[28])
                #registros.append(agendadas)
            
            # Disponíveis
            if not 'nan' in str(row.iloc[36]).strip():
                disponiveis = int(row.iloc[36])
                #registros.append(disponiveis)
        
            if profissional not in ['Nome Do Profissional'] and profissional != None and unidade and data:
                registros.append({
                    "unidade": unidade,
                    "profissional": profissional,
                    "especialidade": especialidade,
                    "vagas": vagas,
                    "agendadas": agendadas,
                    "disponiveis": disponiveis,
                    "data": data,
                })

        return registros


def run_disponibilidade_vagas(conn):
    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(disponibilidade_vagas, conn)
    pipe.run()
