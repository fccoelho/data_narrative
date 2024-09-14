import jinja2
from regdbot.brain import dbtools as dbt
from base_agent.llminterface import LangModel
from typing import List


class StructuralNarrative:
    """
    A class to generate a structural narrative for a database table
    """

    def __init__(self, dburl: str, llm: str = "llama3.1"):
        self.dburl = dburl
        model = LangModel(llm)
        self.database = dbt.Database(dburl, model)

    def generate(self, table: str) -> str:
        sample = self.database._get_sample_rows(table)
        description = self.database.get_table_description(table)
        columns = [
            col.split(":")[1]
            for col in description.split("\n")
            if col.startswith("column")
        ]
        rows = sample
        return self.render(table, columns, rows)

    def render(self, table: str, columns: List, rows: List) -> str:
        template = jinja2.Template(
            """
            Table: {{ table }}
            Columns: {{ columns | join(', ') }}
            Rows: {{ rows | length }}
            """
        )
        return template.render(table=table, columns=columns, rows=rows)
