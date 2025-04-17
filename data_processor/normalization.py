def normalize_columns(df, columns):
    """对指定列进行归一化处理（Min-Max）"""
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"列 {col} 不存在于数据框中")
        min_val = df[col].min()
        max_val = df[col].max()
        if max_val - min_val != 0:
            df[col] = (df[col] - min_val) / (max_val - min_val)
        else:
            df[col] = 0  # 处理常数列
    return df
