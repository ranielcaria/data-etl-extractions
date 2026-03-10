from datetime import datetime

def parse_date(value: str) -> str | None:
    if not value or 'nan' in value.lower():
        return 'Valor Inválido'

    value = value.replace('Data: ', '').replace('/', '-')
    
    try: 
        return datetime.strptime(value, '%d-%m-%Y').strftime('%Y-%m-%d')
    except ValueError:
        return print('Value Error')
        
def parse_datetime(value: str) -> str | None:
    if not value or 'nan' in value.lower():
        return 'Valor Inválido'
        
    value = value.replace('Data: ', '').replace('/', '-')
    
    try:
        return datetime.strptime(value, '%d-%m-%Y - %H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return print('Value Error')

        
    
