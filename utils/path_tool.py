"""
为整个工程提供统一的绝对路径
"""
import os

def get_project_root():
    """
    获取工程所在的根目录
    """
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取工程的根目录
    project_root = os.path.dirname(os.path.dirname(current_file))

    return project_root

def get_abs_path(relative_path)