from api.core.conn import postgres_connection
from api.core.insert import PostgresLoader


class ETLPipeline:
    def __init__(self, extractor, connection):
        self.extractor = extractor
        self.connection = connection
        self.loader = PostgresLoader()

    def run(self):
        rows = self.extractor.run()
        self.loader.insert(
            conn=self.connection,
            table=self.extractor.table,
            columns=self.extractor.columns,
            rows=rows,
            conflict=self.extractor.conflict,
        )