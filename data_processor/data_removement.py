def remove_columns(df, columns_to_remove):
    """
    删除指定的列
    
    参数:
    - df: 输入的DataFrame
    - columns_to_remove: 需要删除的列名列表
    
    返回:
    - 删除列后的新DataFrame
    
    异常:
    - 如果指定的列不存在，抛出ValueError
    """
    # 检查列是否存在
    missing_columns = [col for col in columns_to_remove if col not in df.columns]
    if missing_columns:
        raise ValueError(f"以下列不存在: {', '.join(missing_columns)}")
    
    # 删除列并返回新DataFrame
    return df.drop(columns=columns_to_remove, axis=1)