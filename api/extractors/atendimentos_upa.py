from api.core.base import BaseExtractor
from api.core.transformers import parse_datetime as datetransform

class AtendimentosUpa(BaseExtractor):
    file_path = "api/input/Atendimentos por profissional csm.xls"
    table = "upa"
    columns = [
        "nome_unidade",
        "nome_paciente",
        "nome_profissional",
        "equipe",
        "data_hora",
        "motivo",
        "desfecho",
        "situacao",
    ]
    conflict = "(nome_unidade, nome_paciente, nome_profissional, data_hora, motivo)"

    def transform(self, df):
        registros = []
        unidade = medico = equipe = None

        for _, row in df.iterrows():
            paciente = motivo = desfecho = situacao = datahora = None
            
            # Unidade
            if 'Unidade:' in str(row.iloc[3]).strip():
                unidade = str(row.iloc[3]).replace('Unidade: ', '').strip().title()
                continue
            
            # Profissional e Equipe
            if 'Profissional:' in str(row.iloc[5]).strip():
                medico = str(row.iloc[5]).replace('Profissional: ', '').strip().title().split('-')[0]
                #equipe = 'Equipe ' + str(row.iloc[5]).title().split('Equipe: ')[-1].rstrip(' -')
                equipe = str(row.iloc[5]).title().split('Equipe: ')[-1].rstrip(' -')
                continue
                
            # Motivo
            if 'ATENDIMENTO' in str(row.iloc[24]).strip():
                motivo = str(row.iloc[24]).replace('ATENDIMENTO - ', '').strip().title()
            
            # Paciente
            if str(row.iloc[13]) not in ['nan', 'Nome do paciente']:
                paciente = str(row.iloc[13]).title()
            
            # Desfecho
            if str(row.iloc[30]).strip().lower() not in ['nan', 'desfecho', '']:
                desfecho = str(row.iloc[30]).strip().title()
                
            # Situação
            if str(row.iloc[33]).strip().lower() not in ['nan', 'Situação', '']:
                situacao = str(row.iloc[33]).strip().title()
            
            # Dia e Hora e Append
            if '/' in str(row.iloc[6]):
                datahora = datetransform(row.iloc[6])
                registros.append(
                    {
                        'data_hora': datahora,
                        'nome_unidade': unidade,
                        'nome_profissional': medico,
                        'equipe': equipe,
                        'nome_paciente': paciente,
                        'motivo': motivo,
                        'desfecho': desfecho,
                        'situacao': situacao
                    }
                )

        return registros


def run_atendimentos_upa(conn):
    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(AtendimentosUpa, conn)
    pipe.run()
