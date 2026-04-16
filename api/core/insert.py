class PostgresLoader:
    def insert(self, conn, table, columns, rows, conflict):
        if not rows:
            return

        cols = ", ".join(columns)
        placeholders = ", ".join(["%s"] * len(columns))

        sql = f"INSERT INTO pms.{table} ({cols}) VALUES ({placeholders})"

        if conflict:
            sql += f'ON CONFLICT {conflict} DO NOTHING;'

        sql += ';'

        values = [tuple(row[col] for col in columns) for row in rows]

        with conn.cursor() as cur:
            cur.executemany(sql, values)