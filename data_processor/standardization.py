def standardize_columns(df, columns):
    """对指定列进行标准化处理（Z-Score）"""
    for col in columns:
        if col not in df.columns:
            raise ValueError(f"列 {col} 不存在于数据框中")
        mean_val = df[col].mean()
        std_val = df[col].std()
        if std_val != 0:
            df[col] = (df[col] - mean_val) / std_val
        else:
            df[col] = 0  # 处理常数列
    return df
