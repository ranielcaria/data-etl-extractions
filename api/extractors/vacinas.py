from api.core.base import BaseExtractor
from api.core.transformers import parse_date
from datetime import datetime

class VacinasAplicadas(BaseExtractor):
    file_path = 'api/input/Vacinas aplicadas - Analítico.xls'
    table = 'vacinas_aplicadas'
    columns = ['vacina, profissional, local_aplicacao, data_aplicacao, dose, tipo, genero, gestante, estrategia']
    conflict = '(vacina, dose, tipo, estrategia)'

    def transform(self, df):
        registros = []
        local_aplicacao = None

        for _, row in df.iterrows():
            # Data e Idade
            data = idade = vacina = profissional = dose = tipo = genero = gestante = estrategia = None
            if str(row.iloc[2]) not in ['nan', ''] and '/' in str(row.iloc[2]): data = parse_date(str(row.iloc[2])); data = data if data is not None else data
            nascimento = str(row.iloc[11])
            if '/' in nascimento: idade = datetime.today().year - int(nascimento.split('/')[-1]); nascimento = nascimento if nascimento is not None else nascimento
            #if idade is not None: print(data, idade)
            
            # Vacina
            if not 'nan' in str(row.iloc[17]): vacina = str(row.iloc[17])#; print(vacina)

            # Profissional 'Aplicante'
            if not 'nan' in str(row.iloc[25]): profissional = str(row.iloc[25])#; print(profissional) 

            # Local Aplicação
            if 'Estabelecimento' in str(row.iloc[1]): local_aplicacao = str(row.iloc[1]).removeprefix(' Estabelecimento: ')
            
            # Data Aplicação
            data_aplicacao = data

            # Dose
            if str(row.iloc[23]) not in ['nan', 'Dose']: dose = str(row.iloc[23]).strip()#; print(dose)

            # Tipo
            if str(row.iloc[24]) not in ['nan', 'Tipo']: tipo = str(row.iloc[24]).strip()#; print(tipo)

            # Genero
            if str(row.iloc[12]) not in ['nan', 'Sexo']: genero = str(row.iloc[12]).strip()#; print(genero)

            # Gestante
            if str(row.iloc[13]) not in ['nan', 'Gestante']: gestante = str(row.iloc[13]).strip()#; print(gestante)

            # Estratégia
            if str(row.iloc[22]) not in ['nan', 'Estratégia']: estrategia = str(row.iloc[22]).strip()#; print(estrategia)

            if data:
                registros.append({
                    'vacina': vacina,
                    'profissional': profissional,
                    'local_aplicacao': local_aplicacao,
                    'data_aplicacao': data_aplicacao,
                    'dose': dose,
                    'tipo': tipo,
                    'genero': genero,
                    'gestante': gestante,
                    'estrategia': estrategia,
                    'idade': idade
                })

        return registros


def run_vacinas_aplicadas(conn):
    from api.core.pipeline import ETLPipeline
    pipe = ETLPipeline(VacinasAplicadas, conn)
    pipe.run()