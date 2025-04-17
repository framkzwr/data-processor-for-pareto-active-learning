import pandas as pd

def load_excel(file_path):
    """加载xlsx文件"""
    return pd.read_excel(file_path, engine='openpyxl')

def save_excel(df, file_path):
    """保存DataFrame到xlsx文件"""
    df.to_excel(file_path, index=False, engine='openpyxl')
