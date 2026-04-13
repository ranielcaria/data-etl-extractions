# 🗁 Extrator Excel ETL
Repositório com infraestrutura de código no design pattern formato ETL para extração de dados em excel e inserção em um banco de dados pré-pronto.

### ⬇ Estrutura
- **Extraction**: Extração dos dados em excel. onde acontece a extração dos seus dados que estão na planilha. 
- **Transform**: Onde seus dados são transformados e ficam prontos pra inserção no seu banco.
- **Load**: É a parte onde seus dados são inseridos no banco.

Aqui está uma representação gráfica simples do funcionamento do projeto:

```mermaid
graph TD;
GUI[Usuário insere arquivo via GUI] --> Extração;
Extração --> Transform[Transformação dos dados para inserção no banco];
Transform --> Load[Botão com o nome do seu relatório é selecionado e insere no banco];
Load --> Feedback[GUI mostra uma mensagem de feedback de sucesso]
```

Caso ocorra um erro na inserção, a seguinte lógica ocorre:

```mermaid
graph LR;
Load --> Feedback[GUI mostra uma mensagem de feedback negativo com Traceback];
Feedback --> Load[GUI] 
```

### ⏣ Instalação

Antes de prosseguir com a instalação, lembre-se de mudar o nome do arquivo ```db_config.example.json``` para somente ```db_config.json``` ou configurar seu ```.env```. 

Se for prosseguir com o arquivo json, aqui esta uma estrutura simples para conexão. 

```json
{
  "host": "localhost",
  "port": 5432,
  "database": "seu_banco",
  "user": "postgres",
  "password": "sua_senha"
}
```

1. **Clone o repositório em uma pasta de sua escolha**

```bash 
git clone https://github.com/ranielcaria/data-etl-extractions
cd data-etl-extractions
```

2. **Instale as dependências**

Utilize o terminal (Pode ser o da sua IDE) e entre na raiz do projeto. Depois, utilize este comando:

```bash 
python -m pip install . 
``` 

> Nota: Se você pretende utilizar o conteúdo deste repositório para desenvolvimento, você deve utilizar: 
```bash
pip install -e . 
```

Após, você está pronto para começar a utilizar! só execute o arquivo `` main.py `` e comece!


