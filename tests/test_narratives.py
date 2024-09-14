from data_narrative.narratives import StructuralNarrative


dburl = "CSV:test_datasets/SE_dengue.csv.gz"


def test_struct_narrative():
    SN = StructuralNarrative(dburl)
    tables = SN.database.tables
    narrative = SN.generate(tables[0])
    assert f"Table: {tables[0]}" in narrative
    assert "Columns: data_iniSE" in narrative
    assert "geocodigo" in narrative
