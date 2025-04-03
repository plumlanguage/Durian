import os
import sys
from pathlib import Path

import link
import link.Data as data

def main():
    # 获取命令行数据
    x = sys.argv[1::]
    # 判断对应功能
    if x[0] == "NEW":  # 功能分支-创建
        if x[1] == "CLASS":  # 功能分支-类
            data.Class.new(x[2])
        elif x[1] == "CLASSES": # 功能分支-多个类
            data.Class.newClasses(x[2::])
        elif x[1] == "X": # 功能分支-单值
            if x[2] == "-F": # 配置-来自<类>   durian NEW X -F <类名> <x文件名>
                link.Data.X.newX(Path(link.path_root, x[3], x[4] + ".x"))
            else:
                link.logger.warning("命令输入出现缺失")
                print("这里支持输入的命令:\n-F")
        else:
            link.logger.error(f"输入了位置命令 => {''.join(x)}")
            print("ERR")

    elif x[0] == "FIX":
        if x[1] == "X":
            if x[2] == "-F": # durian FIX X -F <类名> <x文件名> <新内容>
                class_name = x[3]
                x_name = x[4] + ".x"
                new_test = x[5]
                link.Data.X.fixX(Path(link.path_root, class_name, x_name), new_test)
            else:
                link.logger.error(f"输入了位置命令 => {''.join(x)}")
                print("ERR")
        else:
            link.logger.error(f"输入了位置命令 => {''.join(x)}")
            print("ERR")

    elif x[0] == "GET":
        if x[1] == "X":
            class_name = ""
            mb = ""
            if x[2] == "-F":
                class_name = x[3]
                if x[4] == "-T":
                    if x[5] == "SHELL":
                        mb = "SHELL"
                        x_name = x[6]
                        link.Data.X.getXTextToShell(Path(link.path_root, class_name, x_name + ".x"))
                    elif x[5] == "RET":
                        mb = "RET"
                        x_name = x[6]
                        link.Data.X.getXTextToRet(Path(link.path_root, class_name, x_name + ".x"))


    elif x[0] == "DEL": # 功能分支-删除
        if x[1] == "CLASS": # 功能分支-类
            link.Data.Class.delClass(x[2])
        elif x[1] == "CLASSES":
            link.Data.Class.delClasses(x[2::])
        elif x[1] == "X":
            if x[2] == "-F":
                class_name = x[3]
                x_name = x[4]
                while True:
                    us_input = input(f"确定删除{x_name}?[t/f]:")
                    if us_input == "t" or us_input == "T":
                        link.Data.X.delX(Path(link.path_root, class_name, x_name + ".x"))
                        link.logger.info(f"删除单值文件 => {x_name}")
                    elif us_input == "f" or us_input == "F":
                        link.logger.info("取消删除单值文件")

        else:
            link.logger.error(f"输入了位置命令 => {''.join(x)}")
            print("ERR")

    elif x[0] == "INIT":  # 功能分支-初始化
        # 初始化仓库
        link.Init()
        link.Logger.info("初始化仓库完成！")

    else:
        link.logger.error(f"输入了位置命令 => {''.join(x)}")
        print("ERR!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        link.logger.error(f"主线程崩溃！=> {str(e)}")