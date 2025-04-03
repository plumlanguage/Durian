import link
import os

path_root = "./durianData"

class Class:
    @staticmethod
    def new(class_name):
        """
        创建类
        :param class_name: 类的名字（数组）
        :return:True | False
        """
        new_class_path = f"{path_root}/{class_name}"
        # 检查文件夹是否存在
        if os.path.exists(new_class_path):
            # 确保路径是一个文件夹而不是文件
            if os.path.isdir(new_class_path):
                link.logger.warning("也许这个类名已经被占用了")
                return False
            else:
                link.logger.warning("也许这个类名已经被占用了")
                return False
        else:
            os.makedirs(new_class_path)
            link.logger.info("类创建成功！")
            return True

    @staticmethod
    def newClasses(classes_name):
        """
        创建多个类
        :param classes_name: 类名组（数组）
        :return:True | False
        """
        if isinstance(classes_name, list):
            for class_name in classes_name:
                Class.new(class_name)
            return True
        else:
            return False

    @staticmethod
    def delClass(class_name):
        """
        删除单个类
        :param class_name: 类名
        :return: True | False
        """
        pass
        # 先pass，因为我不会~

    @staticmethod
    def delClasses(classes_name):
        """
        删除多个类
        :param classes_name: 类名
        :return: True | False
        """
        if isinstance(classes_name, list):
            for i in classes_name:
                link.Data.Class.delClass(i)
                return True
        else:
            return False