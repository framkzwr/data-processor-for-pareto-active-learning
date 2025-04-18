# Data Pretreatment Library for Pareto Active Learning

## Table of Contents

- [Table of Contents](##Table-of-Contents)
- [Introduction](##Introduction)
- [Features](##Features)
    - [File Directory](###File-Directory)
    - [Data Preparation](###Data-Preparation)
- [Mathematical Processes](##Mathematical-Processes)
    - [Normalization Process](###Normalization-process)
        - [Description](####Description)
        - [Purpose](####Purpose)
    - [Standardization Process](###Standardization-Process)
        - [Description](####Description)
        - [Purpose](####Purpose)
    - [Data Merging Process](###Data-merging-Process)
        - [Purpose](####Purpose)
    - [Data Expansion Process](###Data-expansion-Process)
        - [Description](####Description)
        - [Purpose](####Purpose)
    - [Data Comparison & Deduplication Process](###Data-Comparison--Deduplication-process)
        - [Description](####Description)
- [Usage](##Usage)
    - [Dependency Installation & Environment Setup](###Dependency-Installation--Environment-setup)
    - [Installation](###Installation)
    - [Test Code](###Test-Code)
        - [Notes](####Notes)

---

## Introduction

This library is designed for preprocessing data for **Pareto Active Learning**, handling both feature data and target data.

Model training requires:
- Normalization for feature data
- Standardization for target data

For predicting Pareto frontiers, candidate data space preparation is needed. This library can:
- Expand feature data (custom boundaries and step sizes)
- Automatically generate candidate data space
- Clean and organize candidate data space through data comparison

---

## Features

### File Directory

```text
📦 data-processor
├── 📂 data-processor
│   ├── 📄 __init__.py
│   ├── 📄 normalization.py
│   ├── 📄 standardization.py
│   ├── 📄 combination.py
│   ├── 📄 data_expansion.py
│   ├── 📄 data_comparison.py
│   ├── 📄 data_removement.py
│   ├── 📄 utils.py
├── ⚙️ pyproject.toml
└── 📄 README.md
```

| Code File              | Functionality                 |
|------------------------|-------------------------------|
| 📄 __init__.py         | Define interface              |
| 📄 normalization.py    | Normalization processing      |
| 📄 standardization.py  | Standardization processing    |
| 📄 combination.py      | Column combination processing |
| 📄 data_expansion.py   | Data expansion                |
| 📄 data_comparison.py  | Data comparison               |
| 📄 data_removement.py  | Data deduplication            |
| 📄 utils.py            | Utility module                |

### Data Preparation

Requires an Excel training dataset named **input.xlsx** with the following format:

| num  | para 1 | para 2 | para 3   | obj 1 | obj 2 |
| ---- | ------ | ------ | -------- | ----- | ----- |
| 1    | 100    | 500    | 83.33333 | 942   | 10.7  |
| 2    | 100    | 550    | 75.75758 | 931   | 9.19  |
| 3    | 100    | 600    | 69.44444 | 904   | 8.98  |
| ...  | ...    | ...    | ...      | ...   | ...   |

---

## Mathematical Processes

### Normalization Process

Implementation File: ```📄 normalization.py```

#### Description

For each feature column:
```math
X_{norm} = \frac{X-X_{min}}{X_{max}-X_{min}}
```

Maps data to $[0,1]$ range by default, where $X_{max}$ and $X_{min}$ are column max/min values.

#### Purpose

* Preserves original distribution of features
* Eliminates scale differences
* Maintains sensitivity to outliers

### Standardization Process

Implementation File: ```📄 standardization.py```

#### Description

For each target column:
```math
X_{std} = \frac{X-\mu}{\sigma}
```

Where $\mu$ is column mean and $\sigma$ is standard deviation.

#### Purpose

* Enables comparison between different target dimensions
* Equalizes weights across target space dimensions

### Data Merging Process

Implementation File: ```📄 combination.py```

#### Purpose

Combines normalized feature columns and standardized target columns into a single XLSX file as training dataset.

### Data Expansion Process

Implementation File: ```📄 data_expansion.py```

#### Description

Expand feature columns by setting lower/upper bounds and step sizes:

| Column   | Lower Bound | Upper Bound | Step Size |
|---------|-------------|-------------|-----------|
| para 1  | 2           | 3           | 1         |
| para 2  | 400         | 500         | 100       |
| para 3  | 60          | 80          | 20        |
| para 4  | 0.04        | 0.04        | 1         |
| para 5  | 0.05        | 0.06        | 0.01      |

Expanded results:

| para 1 | para 2 | para 3 | para 4 | para 5 |
|--------|--------|--------|--------|--------|
| 2      | 400    | 60     | 0.04   | 0.05   |
| 2      | 400    | 60     | 0.04   | 0.06   |
| ...    | ...    | ...    | ...    | ...    |

#### Purpose

Generates candidate prediction data space through combinatorial expansion.

### Data Comparison & Deduplication Process

Implementation Files: ```📄 data_comparison.py``` ```📄 data_removement.py```

#### Description

Row-by-row comparison between **expanded** data and **unlabeled_input** data. Remove duplicates from expanded data that exist in labeled data.

Example: If labeled data contains:
| para 1 | para 2 | para 3 | para 4 | para 5 |
|--------|--------|--------|--------|--------|
| 2      | 400    | 80     | 0.04   | 0.06   |

After deduplication (**cleaned** data):
| para 1 | para 2 | para 3 | para 4 | para 5 |
|--------|--------|--------|--------|--------|
| 2      | 400    | 60     | 0.04   | 0.05   |
| 2      | 400    | 60     | 0.04   | 0.06   |
| ...    | ...    | ...    | ...    | ...    |

---

## Usage

### Dependency Installation & Environment Setup

Python Version: ```python 3.10.16```

Install dependencies:
```bash
pip install numpy
pip install pandas
pip list
```

Expected installed packages:

| Package | Version |
|---------|---------|
| 📦 numpy | 2.2.4 |
| 📦 pandas | 2.2.3 |
| 📦 pip | 25.0 |
|📦 python-dateutil | 2.9.0.post0 |
| 📦 pytz | 2025.2 |
| 📦 setuptools | 75.8.0 |
| 📦 six | 1.17.0 |
| 📦 tzdata | 2025.2 |
| 📦 wheel | 0.45.1 |
### Installation
```bash
cd ~/data_processor/
pip install -e .
pip list
```
Should show:
data-processor	1.0.0

### Test Code
```python
from data_processor import (
    load_excel, save_excel,
    normalize_columns, standardize_columns,
    compare_and_deduplicate, remove_columns, 
    merge_excel_columns, generate_expanded_values,
    generate_parameter_combinations
)
# ====================== Global Configuration ======================
# Input/output file configuration
INPUT_FILE = "input.xlsx"
OUTPUT_FILES = {
    "normalized": "normalized.xlsx",
    "standardized": "standardized.xlsx",
    "merged": "labeled.xlsx",
    "unlabeled_input": "unlabeled_input.xlsx",
    "expanded": "expanded.xlsx",
    "cleaned": "cleaned.xlsx",
    "unlabeled": "unlabeled.xlsx"
}
# Column operations configuration
NORMALIZE_COLS = ["para_1", "para_2", "para_3", "para_4", "para_5"]
STANDARDIZE_COLS = ["obj_1", "obj_2"]
COLUMNS_TO_REMOVE = ["date", "obj_1", "obj_2", "high_light"]
# Data merging configuration
MERGE_CONFIG = {
    "columns1": NORMALIZE_COLS,
    "columns2": ["num"] + STANDARDIZE_COLS,
    "column_order": ["num"] + NORMALIZE_COLS + STANDARDIZE_COLS
}
# Parameter expansion configuration (format: column: (start, end, step))
# Must match NORMALIZE_COLS in quantity and headers
EXPANSION_RANGES = {
    "para_1": (2, 3, 1),
    "para_2": (400, 500, 100),
    "para_3": (60, 80, 20),
    "para_4": (0.04, 0.04, 1),
    "para_5": (0.05, 0.06, 0.01)
}
# Data comparison configuration
COMPARE_COLS = NORMALIZE_COLS
# ====================== Execution Flow ======================
if __name__ == "__main__":
    # 1. Labeled data normalization
    df = load_excel(INPUT_FILE)
    df = normalize_columns(df, NORMALIZE_COLS)
    save_excel(df, OUTPUT_FILES["normalized"])
    # 2. Labeled data standardization
    df = load_excel(INPUT_FILE)
    df = standardize_columns(df, STANDARDIZE_COLS)
    save_excel(df, OUTPUT_FILES["standardized"])
    # 3. Data merging
    merge_excel_columns(
        file1_path=OUTPUT_FILES["normalized"],
        file2_path=OUTPUT_FILES["standardized"],
        columns1=MERGE_CONFIG["columns1"],
        columns2=MERGE_CONFIG["columns2"],
        column_order=MERGE_CONFIG["column_order"],
        output_path=OUTPUT_FILES["merged"]
    )
    # 4. Remove unused columns
    df = load_excel(INPUT_FILE)
    df = remove_columns(df, COLUMNS_TO_REMOVE)
    save_excel(df, OUTPUT_FILES["unlabeled_input"])
    # 5. Parameter expansion
    param_ranges = {
        col: generate_expanded_values(*params)
        for col, params in EXPANSION_RANGES.items()
    }
    df_expanded = generate_parameter_combinations(param_ranges)
    save_excel(df_expanded, OUTPUT_FILES["expanded"])
    # 6. Data deduplication
    df1 = load_excel(OUTPUT_FILES["expanded"])
    df2 = load_excel(OUTPUT_FILES["unlabeled_input"])
    df_clean = compare_and_deduplicate(df1, df2, COMPARE_COLS, "num")
    save_excel(df_clean, OUTPUT_FILES["cleaned"])
    # 7. Cleaned data normalization
    df = load_excel(OUTPUT_FILES["cleaned"])
    df = normalize_columns(df, NORMALIZE_COLS)
    save_excel(df, OUTPUT_FILES["unlabeled"])
    print("------------Data pretreatment finished------------")
```
#### Notes
* test.py must be in the same directory as input/output **xlsx** files
* `EXPANSION_RANGES` must include all feature columns. For non-expanding columns, follow the **para_4** example in `test.py`
* Include columns to be removed from unlabeled data (e.g., obj_1, obj_2) in `COLUMNS_TO_REMOVE`



