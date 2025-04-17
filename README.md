# Data Pretreatment lib for pareto active learning

## 目录：

- [Data Pretreatment lib for pareto active learning](#data-pretreatment-lib-for-pareto-active-learning)
  - [目录：](#目录)
  - [前言：](#前言)
  - [功能：](#功能)
    - [文件目录](#文件目录)
    - [数据准备：](#数据准备)
  - [数学过程](#数学过程)
    - [归一化过程](#归一化过程)
      - [描述](#描述)
      - [作用](#作用)
    - [标准化过程](#标准化过程)
      - [描述](#描述-1)
      - [作用](#作用-1)
    - [数据合并过程](#数据合并过程)
      - [作用](#作用-2)
    - [数据扩展过程](#数据扩展过程)
      - [描述](#描述-2)
      - [作用](#作用-3)
    - [数据对比与删除重复过程](#数据对比与删除重复过程)
      - [描述](#描述-3)
  - [使用方法](#使用方法)
    - [安装依赖和环境](#安装依赖和环境)
    - [安装](#安装)
    - [测试代码](#测试代码)
      - [注意](#注意)

---

## 前言：

这个函数库用于预处理**pareto**主动学习的数据，分为特征数据和目标数据两部分。

模型训练要求对特征数据进行归一化处理，对目标数据进行标准化处理。

预测pareto前沿时需要备选数据空间，这个函数库能对特征数据进行扩展（自定义设置边界和步长），自动生成备选数据空间，并通过数据对比和清洗整理备选数据空间。

---

## 功能：

### 文件目录

```
📦 project-root
├── 📂 src
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

| 代码文件             | 功能           |
| -------------------- | -------------- |
| 📄 normalization.py   | 归一化处理     |
| 📄 standardization.py | 标准化处理     |
| 📄 combination.py     | 数据列组合处理 |
| 📄 data_expansion.py  | 数据扩展       |
| 📄 data_comparison.py | 数据对比       |
| 📄 data_removement.py | 删除数据重复   |
| 📄 utils.py           | 辅助模块       |

### 数据准备：

需要一个excel文件格式训练数据集，命名为**input.xlsx**，内容示例如下：

| num  | para 1 | para 2 | para 3   | obj 1 | obj 2 |
| ---- | ------ | ------ | -------- | ----- | ----- |
| 1    | 100    | 500    | 83.33333 | 942   | 10.7  |
| 2    | 100    | 550    | 75.75758 | 931   | 9.19  |
| 3    | 100    | 600    | 69.44444 | 904   | 8.98  |
| ...  | ...    | ...    | ...      | ...   | ...   |

---

## 数学过程

### 归一化过程

功能文件：```📄 normalization.py```

#### 描述

对于每个特征列：、
$$
X_{norm} = \frac{X-X_{min}}{X_{max}-X_{min}}
$$


这里默认将数据映射到$[0,1]$区间，$X_{max}$和$X_{min}$的取值为列数据的最大值和最小值。

#### 作用

* 保持特征间的原始分布形态。
* 消除量纲差异。
* 保留离群值敏感性。



### 标准化过程

功能文件：```📄 standardization.py```

#### 描述

对每个目标列：
$$
X_{std} = \frac{X-\mu}{\sigma}
$$


$\mu$为列数据均值，$\sigma$为标准差.

#### 作用

* 使不同量纲的目标变量具有可比性。
* 目标空间各维度权重相等。

### 数据合并过程

功能文件：```📄 combination.py```

#### 作用

把归一化后的特征列和标准化后的目标列数据合并在一个xlsx文件中，作为训练数据集。

### 数据扩展过程

功能文件：```📄 data_expansion.py```

#### 描述

通过设置下界、上界、步长，扩展特征列数据，示例如下：

| 列     | 下界 | 上界 | 步长 |
| ------ | ---- | ---- | ---- |
| para 1 | 2    | 3    | 1    |
| para 2 | 400  | 500  | 100  |
| para 3 | 60   | 80   | 20   |
| para 4 | 0.04 | 0.04 | 1    |
| para 5 | 0.05 | 0.06 | 0.01 |

扩展得到：

| para 1 | para 2 | para 3 | para 4 | para 5 |
| ------ | ------ | ------ | ------ | ------ |
| 2      | 400    | 60     | 0.04   | 0.05   |
| 2      | 400    | 60     | 0.04   | 0.06   |
| 2      | 400    | 80     | 0.04   | 0.05   |
| 2      | 400    | 80     | 0.04   | 0.06   |
| 2      | 500    | 60     | 0.04   | 0.05   |
| 2      | 500    | 60     | 0.04   | 0.06   |
| 2      | 500    | 80     | 0.04   | 0.05   |
| 2      | 500    | 80     | 0.04   | 0.06   |
| 3      | 400    | 60     | 0.04   | 0.05   |
| 3      | 400    | 60     | 0.04   | 0.06   |
| 3      | 400    | 80     | 0.04   | 0.05   |
| 3      | 400    | 80     | 0.04   | 0.06   |
| 3      | 500    | 60     | 0.04   | 0.05   |
| 3      | 500    | 60     | 0.04   | 0.06   |
| 3      | 500    | 80     | 0.04   | 0.05   |
| 3      | 500    | 80     | 0.04   | 0.06   |

#### 作用

通过数据扩展生成待选择的预测数据空间。

### 数据对比与删除重复过程

功能文件：```📄 data_comparison.py``` ```📄 data_removement.py```

#### 描述

逐行遍历**expanded**数据和**unlabeled_input**数据，对比进行扩展的列数据的单行内容是否完全一致（找到在**expanded**数据中出现的**labeled**数据），并删除。

如上文数据扩展中产生的**expanded**数据，当**labeled**数据中存在行：

| para 1 | para 2 | para 3 | para 4 | para 5 |
| ------ | ------ | ------ | ------ | ------ |
| 2      | 400    | 80     | 0.04   | 0.06   |

数据对比与删除重复过程后，**cleaned**数据为：

| para 1 | para 2 | para 3 | para 4 | para 5 |
| ------ | ------ | ------ | ------ | ------ |
| 2      | 400    | 60     | 0.04   | 0.05   |
| 2      | 400    | 60     | 0.04   | 0.06   |
| 2      | 400    | 80     | 0.04   | 0.05   |
| 2      | 500    | 60     | 0.04   | 0.05   |
| 2      | 500    | 60     | 0.04   | 0.06   |
| 2      | 500    | 80     | 0.04   | 0.05   |
| 2      | 500    | 80     | 0.04   | 0.06   |
| 3      | 400    | 60     | 0.04   | 0.05   |
| 3      | 400    | 60     | 0.04   | 0.06   |
| 3      | 400    | 80     | 0.04   | 0.05   |
| 3      | 400    | 80     | 0.04   | 0.06   |
| 3      | 500    | 60     | 0.04   | 0.05   |
| 3      | 500    | 60     | 0.04   | 0.06   |
| 3      | 500    | 80     | 0.04   | 0.05   |
| 3      | 500    | 80     | 0.04   | 0.06   |

剩余15个数据，重复行被删除，**num**列将被重置。

---

## 使用方法

### 安装依赖和环境

python版本：```python 3.10.16```

依赖函数库安装：

```bash
pip install numpy
pip install pandas
pip list
```

已安装list显示：				

| package           | version     |
| ----------------- | ----------- |
| 📦 numpy           | 2.2.4       |
| 📦 pandas          | 2.2.3       |
| 📦 pip             | 25.0        |
| 📦 python-datextil | 2.9.0.post0 |
| 📦 pytz            | 2025.2      |
| 📦 setuptools      | 75.8.0      |
| 📦 six             | 1.17.0      |
| 📦 tzdata          | 2025.2      |
| 📦 wheel           | 0.45.1      |

### 安装

```bash
cd ~/data_processor/
pip install -e .

pip list
```

显示除依赖包以外：

data-processor	1.0.0

### 测试代码

```python
from data_processor import (
    load_excel, save_excel,
    normalize_columns, standardize_columns,
    compare_and_deduplicate, remove_columns, 
    merge_excel_columns, generate_expanded_values,
    generate_parameter_combinations
)

# ====================== 全局配置 ======================
# 输入输出文件配置
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

# 列操作配置
NORMALIZE_COLS = ["para_1", "para_2", "para_3", "para_4", "para_5"]
STANDARDIZE_COLS = ["obj_1", "obj_2"]
COLUMNS_TO_REMOVE = ["date", "obj_1", "obj_2", "high_light"]

# 数据合并配置
MERGE_CONFIG = {
    "columns1": NORMALIZE_COLS,
    "columns2": ["num"] + STANDARDIZE_COLS,
    "column_order": ["num"] + NORMALIZE_COLS + STANDARDIZE_COLS
}

# 参数扩展配置（格式：列名: (start, end, step）)
# 列数和表头内容必须与NORMALIZE_COLS对应
EXPANSION_RANGES = {
    "para_1": (2, 3, 1),
    "para_2": (400, 500, 100),
    "para_3": (60, 80, 20),
    "para_4": (0.04, 0.04, 1),
    "para_5": (0.05, 0.06, 0.01)
}

# 数据对比配置
COMPARE_COLS = NORMALIZE_COLS

# ====================== 执行流程 ======================
if __name__ == "__main__":
    # 1. labeled归一化处理
    df = load_excel(INPUT_FILE)
    df = normalize_columns(df, NORMALIZE_COLS)
    save_excel(df, OUTPUT_FILES["normalized"])

    # 2. labeled标准化处理
    df = load_excel(INPUT_FILE)
    df = standardize_columns(df, STANDARDIZE_COLS)
    save_excel(df, OUTPUT_FILES["standardized"])

    # 3. 合并数据
    merge_excel_columns(
        file1_path=OUTPUT_FILES["normalized"],
        file2_path=OUTPUT_FILES["standardized"],
        columns1=MERGE_CONFIG["columns1"],
        columns2=MERGE_CONFIG["columns2"],
        column_order=MERGE_CONFIG["column_order"],
        output_path=OUTPUT_FILES["merged"]
    )

    # 4. 删除无用列
    df = load_excel(INPUT_FILE)
    df = remove_columns(df, COLUMNS_TO_REMOVE)
    save_excel(df, OUTPUT_FILES["unlabeled_input"])

    # 5. 参数扩展
    param_ranges = {
        col: generate_expanded_values(*params)
        for col, params in EXPANSION_RANGES.items()
    }
    df_expanded = generate_parameter_combinations(param_ranges)
    save_excel(df_expanded, OUTPUT_FILES["expanded"])

    # 6. 数据对比去重
    df1 = load_excel(OUTPUT_FILES["expanded"])
    df2 = load_excel(OUTPUT_FILES["unlabeled_input"])
    df_clean = compare_and_deduplicate(df1, df2, COMPARE_COLS, "num")
    save_excel(df_clean, OUTPUT_FILES["cleaned"])

    # 7. 清洗后归一化
    df = load_excel(OUTPUT_FILES["cleaned"])
    df = normalize_columns(df, NORMALIZE_COLS)
    save_excel(df, OUTPUT_FILES["unlabeled"])

    print("------------Data pretreatment finished------------")
```

#### 注意

* ```test.py```文件必须和输入输出的**xlsx**文件在同一目录下。
* ```EXPANSION_RANGES```必须标注所有的特征数据列，尽管可能存在不需要扩展的数据列，若某列不需要扩展，请模仿```test.py```中**para_4**的情况。
* 在```COLUMNS_TO_REMOVE```中请包含**unlabeled**数据中不需要出现的特征列数据（**obj_1**、**obj_2**）。



