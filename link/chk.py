import os.path
from pathlib import Path

import link

class Class:
    @staticmethod
    def chkClass(class_name) -> bool:
        """
        检查类是否存在
        :param class_name: 类的名字
        :return:
        """
        folder_path = Path(link.path_root, class_name)
        if os.path.exists(folder_path):
            link.logger.info(f"路径存在 => {folder_path}")
            return True
        else:
            link.logger.warning(f"路径不存在 => {folder_path}")
            return False

class X:
    @staticmethod
    def chkX(class_name, x_name) -> bool:
        """
        检查类是否存在
        :param class_name: 类的名字
        :param x_name: 单值文件的名字
        :return:
        """
        folder_path = Path(link.path_root, class_name, x_name)
        if os.path.isfile(folder_path):
            link.logger.info(f"单值路径存在 => {folder_path}")
            return True
        else:
            link.logger.warning(f"单值路径不存在 => {folder_path}")
            return False



