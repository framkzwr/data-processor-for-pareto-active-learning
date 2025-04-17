def compare_and_deduplicate(df1, df2, compare_columns, row_id_column):
    """对比两个数据集并删除重复行，确保行号列在第一列"""
    # 标记重复行
    merged = df1.merge(df2[compare_columns], on=compare_columns, how='left', indicator=True)
    duplicate_mask = (merged['_merge'] == 'both')
    
    # 删除重复行并重置索引
    df_cleaned = df1[~duplicate_mask].reset_index(drop=True)
    
    # 更新行号列
    if row_id_column not in df_cleaned.columns:
        raise ValueError(f"行号列 {row_id_column} 不存在")
        
    # 强制将行号列移动到第一列
    df_cleaned[row_id_column] = df_cleaned.index + 1
    cols = [row_id_column] + [col for col in df_cleaned.columns if col != row_id_column]
    df_cleaned = df_cleaned[cols]
    
    return df_cleaned
