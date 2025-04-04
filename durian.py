import os
import sys
from pathlib import Path

import link
import link.chk
import link.Data as data

def main():
    print(f"WorkPath -> {os.getcwd()}")
    # print(os.system("dir"))
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
                link.Data.X.newX(x[3], x[4] + ".x")
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
                new_test = "".join(x[5::])
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
                # link.Data.X.delX(f"{link.path_root}/{class_name}",  "/" + x_name + ".x" )
                try:
                    os.remove(Path(link.path_root, class_name, x_name + ".x"))
                    link.logger.info(f"成功删除单值文件 => {Path(link.path_root, class_name, x_name + '.x')}")
                except Exception as e:
                    link.logger.error(f"单值文件删除错误 => {e}")

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