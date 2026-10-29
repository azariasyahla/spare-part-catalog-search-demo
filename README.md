# Spare Part Catalog Search (Data Dummy)

A small portfolio case study based on a real workflow challenge: spare-part master data is partial, customer questions use mixed Indonesian and English terms, and repeated lookups can create duplicate records.

This public demo uses **synthetic sample records and fictional prices only**. It does not contain the source pricelists, live prices, or internal customer-group data. The production app and its Windows packaging remain separate from this demonstration.

## What this demo shows

- Bilingual keyword search (for example, `battery` / `baterai`, `tire` / `ban`).
- Partial and typo-tolerant matching (for example, `batt`, `tirre`).
- Exact duplicate checks using normalized part number, description, and unit.
- Missing-field visibility to flag information that still needs confirmation.
- A notebook-ready workflow using pandas and Python's standard library.

## Repository layout

- `notebooks/spare_part_catalog_search.ipynb` — standalone Kaggle-compatible notebook with synthetic data generated in the notebook.
- `data/synthetic_parts_catalog.csv` — sample dataset for local exploration.
- `src/catalog_demo.py` — reusable search and duplicate-check functions.

## Run locally

```bash
python -m pip install pandas
python - <<'PY'
import pandas as pd
from src.catalog_demo import search_catalog
df = pd.read_csv('data/synthetic_parts_catalog.csv').fillna('')
print(search_catalog(df, 'batt')[['pn', 'description_en', 'description_id']])
PY
```

## Current status

This repository is a sanitized portfolio demo, not a release of the internal application. The in-app spreadsheet interaction and standalone Windows EXE are still being validated.
