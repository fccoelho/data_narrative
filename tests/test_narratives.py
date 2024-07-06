import pytest
import duckdb
from data_narrative.narratives import StructuralNarrative

con = duckdb.connect(database=":memory:")
con.execute('CREATE TABLE  dengue as select * from "tests/test_datasets/SE_dengue.csv.gz"')

def test_struct_narrative():
    SN = StructuralNarrative(con)
    narrative = SN.generate("dengue")
    assert "Table: dengue" in narrative
    assert "Columns: data_iniSE, SE" in narrative


