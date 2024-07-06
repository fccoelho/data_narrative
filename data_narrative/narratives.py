import duckdb
import jinja2

class StructuralNarrative:
    '''
    A class to generate a structural narrative for a database table
    '''
    def __init__(self, conn: duckdb.DuckDBPyConnection):
        self.conn = conn

    def generate(self, table: str) -> str:
        query = f"SELECT * FROM {table}"
        result = self.conn.execute(query)
        columns = [col[0] for col in result.description]
        rows = result.fetchall()
        return self.render(table, columns, rows)

    def render(self, table: str, columns: list, rows: list) -> str:
        template = jinja2.Template(
            """
            Table: {{ table }}
            Columns: {{ columns | join(', ') }}
            Rows: {{ rows | length }}
            """
        )
        return template.render(table=table, columns=columns, rows=rows)
