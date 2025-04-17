import pandas as pd
import numpy as np
from itertools import product

def generate_parameter_combinations(param_ranges):
    """
    直接生成参数的笛卡尔积组合，完全独立于原始数据
    - param_ranges: 字典格式 {列名: 扩展值列表}
    示例：
    param_ranges = {
        "scan_speed": [400, 500],
        "laser_power": [60, 80],
        "hatch_space": [0.05, 0.06]
    }
    """
    # 生成所有参数的笛卡尔积
    param_names = list(param_ranges.keys())
    value_combinations = list(product(*param_ranges.values()))
    
    # 构建DataFrame
    df = pd.DataFrame(value_combinations, columns=param_names)
    
    # 添加固定列（如果存在非扩展列）
    # df["TiBvol%"] = 2  # 根据需求添加固定值
    
    # 生成num列
    df.reset_index(drop=True, inplace=True)
    df["num"] = df.index + 1
    
    return df

# 辅助函数：生成数值序列（解决浮点精度问题）
def generate_expanded_values(start, end, step, decimals=2):
    values = np.arange(start, end + 1e-9, step)
    return np.round(values, decimals=decimals).tolist()
