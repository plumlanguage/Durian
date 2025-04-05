import datetime
import os

path_root = "./durianData"

class Class:
    @staticmethod
    def new(class_name):
        """
        创建类
        :param class_name:
        :return:
        """
        new_class_path = f"{path_root}/{class_name}"
        # 检查文件夹是否存在
        if os.path.exists(new_class_path):
            # 确保路径是一个文件夹而不是文件
            if os.path.isdir(new_class_path):
                logger.warning("也许这个类名已经被占用了")
                return "F"
            else:
                logger.warning("也许这个类名已经被占用了")
                return "F"
        else:
            os.makedirs(new_class_path)
            logger.info("类创建成功！")
            return "T"

class Logger:
    def __init__(self, log_file_path="app.log"):
        self.log_file_path = log_file_path
        # 确保日志文件存在
        if not os.path.exists(log_file_path):
            with open(log_file_path, 'w', encoding='utf-8') as f:
                pass  # 创建空文件

    def log(self, message, log_type="INFO"):
        """记录日志"""
        # 获取当前时间
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 格式化日志内容
        log_entry = f"[{current_time}] [{log_type}] {message}\n"
        # 写入日志文件，指定编码为 UTF-8
        with open(self.log_file_path, 'a', encoding='utf-8') as f:
            f.write(log_entry)
        print(log_entry, end='')  # 同时打印到控制台

    def info(self, message):
        """记录信息日志"""
        self.log(message, "INFO")

    def warning(self, message):
        """记录警告日志"""
        self.log(message, "WARNING")

    def error(self, message):
        """记录错误日志"""
        self.log(message, "ERROR")

    def test(self, message):
        """记录测试日志"""
        self.log(message, "TEST")
# 创建全局的日志实例
logger = Logger("./app.log")

def Init():
    """
    初始化仓库
    :return: T:String F:String
    """
    logger.info("初始化数据库")
    folder_path = path_root
    # 检查文件夹是否存在
    if os.path.exists(folder_path):
        # 确保路径是一个文件夹而不是文件
        if os.path.isdir(folder_path):
            logger.warning("初始化数据库的路径有问题！")
            return "F"
        else:
            logger.warning("初始化数据库的路径有问题！")
            return "F"
    else:
        os.makedirs(folder_path)
        logger.info("初始化数据库成功！")
        return "T"
