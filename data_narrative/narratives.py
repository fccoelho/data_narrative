import jinja2
from regdbot.brain import dbtools as dbt
from base_agent.llminterface import LangModel
from typing import List


class StructuralNarrative:
    """
    A class to generate a structural narrative for a database table
    """

    def __init__(self, dburl: str, llm: str = "llama3.2"):
        self.dburl = dburl
        model = LangModel(llm)
        self.database = dbt.Database(dburl, model)

    def generate(self, table: str) -> str:
        rows = self.database._get_sample_rows(table)
        description = self.database.get_table_description(table, raw=True)
        return self.render(table, description, rows)

    def render(
        self, table: str, columns: List, rows: List, save_to_file: bool = True
    ) -> str:
        template = jinja2.Template(
            """
# Structural Narrative for database table {{ table }}
## Table Summary
{% for col in columns -%}
{%- if loop.first -%}
| Name | type | description |
|:-----|:----:|:-----------:|
{% endif %}
{{- col[0] }} | {{ col[1] }} | {{ col[2] }} |
{% endfor %}
### Sample Rows
{% for row in rows -%}
{{- row }}
{% endfor %}
"""
        )
        report = template.render(table=table, columns=columns, rows=rows)
        if save_to_file:
            with open(f"{table}.md", "w") as f:
                f.write(report)
        return report
