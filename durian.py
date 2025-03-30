import sys
import link
import link.Data as data

def main():
    # 获取命令行数据
    x = sys.argv[1::]
    # 判断对应功能
    if x[0] == "NEW":  # 功能分支-创建
        if x[1] == "CLASS":  # 功能分支-类
            # 数据（完整）：
            # NEW CLASS <类的名字>
            #  0     1      2
            data.Class.new(x[2])
        elif x[1] == "CLASSES": # 功能分支-多个类
            pass

    elif x[0] == "INIT":  # 功能分支-初始化
        # 初始化仓库
        link.Init()
        link.Logger.info("初始化仓库完成！")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        link.logger.error(f"主线程崩溃！=> {str(e)}")