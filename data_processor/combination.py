import pandas as pd
from typing import List, Optional

def merge_excel_columns(
    file1_path: str,
    file2_path: str,
    columns1: List[str],
    columns2: List[str],
    column_order: List[str],
    output_path: str,
    sheet_name1: Optional[str] = 0,  # 默认读取第一个Sheet
    sheet_name2: Optional[str] = 0,  # 默认读取第一个Sheet
    engine: str = "openpyxl"
) -> None:
    """
    修复版：合并两个Excel文件的指定列并按自定义顺序输出。
    """
    # 检查列名冲突
    common_columns = set(columns1) & set(columns2)
    if common_columns:
        raise ValueError(f"列名冲突：{common_columns} 在两个文件中重复，请确保唯一性。")

    # 读取Excel文件（确保返回DataFrame）
    def safe_read_excel(path: str, sheet: Optional[str] = 0) -> pd.DataFrame:
        data = pd.read_excel(path, sheet_name=sheet, engine=engine)
        if isinstance(data, dict):
            if not data:
                raise ValueError(f"文件 {path} 中未找到Sheet: {sheet}")
            return data[next(iter(data))]  # 返回第一个Sheet的DataFrame
        return data

    df1 = safe_read_excel(file1_path, sheet_name1)
    df2 = safe_read_excel(file2_path, sheet_name2)

    # 验证列是否存在
    for col in columns1:
        if col not in df1.columns:
            raise ValueError(f"文件1中不存在列 '{col}'")
    for col in columns2:
        if col not in df2.columns:
            raise ValueError(f"文件2中不存在列 '{col}'")

    # 合并并保存
    combined_df = pd.concat([df1[columns1], df2[columns2]], axis=1)
    
    if set(column_order) != set(combined_df.columns):
        missing = set(combined_df.columns) - set(column_order)
        extra = set(column_order) - set(combined_df.columns)
        error_msg = []
        if missing: error_msg.append(f"缺少列：{missing}")
        if extra: error_msg.append(f"多余列：{extra}")
        raise ValueError(f"列顺序错误：{'；'.join(error_msg)}")

    combined_df[column_order].to_excel(output_path, index=False, engine=engine)
