# Updates Based on Days

## Day 1
- Learned about Series
- Worked with Series operations
- Explored methods and constructors used with Series
- Fixed a local Pylance issue                                                      

## Day 2
- Learned about DataFrames
- Worked with DataFrame operations
- Added new rows and columns to DataFrames
- Explored DataFrame-related concepts
- Learned to import CSV and JSON files
- Used basic methods to display CSV and JSON data

## Day 3 — Series (details)
- Constructed `Series` from lists and dictionaries
- Used custom indexes and understood index vs value display
- Accessed and assigned with `.loc` (label) and `.iloc` (integer position)
- Performed boolean filtering on `Series` (e.g., `series[series >= 101]`)

## Day 4 — DataFrame creation & mutation
- Built `DataFrame` from a `dict` and set custom `index`
- Added columns (`df["col"] = ...`) and appended rows using `pd.concat`
- Learned that missing columns/values become `NaN` when concatenating

## Day 5 — Selecting & indexing
- Selected columns with `df["col"]` and multiple columns with `df[[...]]`
- Selected rows and values using `df.loc[...]`, `df.iloc[...]`, slicing and step sizes
- Used `index_col` to make a column the DataFrame index for label-based access
- Built a simple interactive lookup with `input()` and `try/except` to handle `KeyError` (`selecting/prog.py`)

## Day 6 — Filtering
- Filtered rows with boolean masks (`df[df["Height"] >= 2]`)
- Combined conditions with `|` (OR) and `&` (AND), remembering to parenthesize each condition

## Day 7 — Importing data
- Imported CSV and JSON with `pd.read_csv()` and `pd.read_json()` (file name or full path)
- Used `.head()`, `.tail()` and `.to_string()` when inspecting large datasets

## Day 8 — Aggregation & grouping
- Used aggregations: `mean()`, `min()`, `max()`, `sum()`, `count()` (use `numeric_only=True` when needed)
- Grouped data with `df.groupby("Type1")` and applied aggregations per group (e.g., `group["Height"].mean()`)

## Notes
- Worked mainly with the Pokémon CSV/JSON datasets present in each folder
- Representative scripts: [series/series.py](series/series.py), [data-frames/data-frame.py](data-frames/data-frame.py), [selecting/select.py](selecting/select.py), [selecting/prog.py](selecting/prog.py), [filtering/filter.py](filtering/filter.py), [import/import.py](import/import.py), [aggregation/aggregation.py](aggregation/aggregation.py)
