import os
import shutil
import logging

# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def copy_files(source_dir, destination_dir, excluded_dirs=None, excluded_extensions=None):
    """
    递归地将文件从源目录复制到目标目录，同时排除指定的目录和文件类型。

    :param source_dir: 源目录的路径。
    :param destination_dir: 目标目录的路径。
    :param excluded_dirs: 一个包含要排除的目录名称的列表。
    :param excluded_extensions: 一个包含要排除的文件扩展名的列表。
    """
    if excluded_dirs is None:
        excluded_dirs = []
    if excluded_extensions is None:
        excluded_extensions = []

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        logging.info(f"创建目标目录: {destination_dir}")

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        if os.path.isdir(source_item):
            if item not in excluded_dirs:
                copy_files(source_item, destination_item, excluded_dirs, excluded_extensions)
            else:
                logging.info(f"跳过排除的目录: {source_item}")
        else:
            if not any(item.endswith(ext) for ext in excluded_extensions):
                shutil.copy2(source_item, destination_item)
                logging.info(f"已复制文件: {source_item} 到 {destination_item}")
            else:
                logging.info(f"跳过排除的文件: {source_item}")
