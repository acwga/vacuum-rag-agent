"""
为整个工程提供统一的绝对路径
"""
import os

def get_project_root():
    """
    获取工程所在的根目录
    :return: 工程根目录的绝对路径
    """
    # 获取当前文件的绝对路径
    current_file = os.path.abspath(__file__)
    # 获取工程的根目录
    project_root = os.path.dirname(os.path.dirname(current_file))

    return project_root

def get_abs_path(relative_path):
    """
    将相对路径转换为绝对路径
    :param relative_path: 相对路径
    :return: 绝对路径
    """
    project_root = get_project_root()
    return os.path.join(project_root, relative_path)

if __name__ == "__main__":
    print(get_abs_path('config/config.txt'))