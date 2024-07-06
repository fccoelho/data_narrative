# Usage

To use Data Narrative in a project

```python
import duckdb # or any other database library
from data_narrative.narratives import StructuralNarrative

# Connect to the database
con = duckdb.connect(database=":memory:")
con.execute('CREATE TABLE  dengue as select * from "tests/test_datasets/SE_dengue.csv.gz"')

# Create a narrative
SN = StructuralNarrative(con)
# Generate the narrative for a table
SN.generate("dengue")
```
