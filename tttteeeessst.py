import imp
import sys
from  importlib import  reload
def  filepath_final1 (filePath):
    path = sys.path[0]
    filepath_final = path + '\\' + filePath
    return filepath_final

import os
import re

cls_name_list = []
def get_dir(path):
    try:
        file_list = os.listdir(path)
    except:
        file_list = []
        print("the path is not dir")
    if file_list:
        for file in file_list:
            file = os.path.join(path, file)
            # print(file)
            if os.path.isdir(file):
                get_dir(file)
            else:
                if not file.__contains__('__init__'):
                    if file.endswith(".py"):
                        print(file)
                        with open(file, encoding="utf-8") as f:
                            for line in f.readlines():
                                # print(line +'%%%%%%%')
                                cls_match = re.match(r"class\s(.*?)[\(:]", line)
                                if cls_match:
                                    cls_name = cls_match.group(1)
                                    try:
                                        module = imp.load_source('mycl', file)
                                        cls_a = getattr(module, cls_name)
                                        if cls_a:
                                            print(cls_name+'   @@@@@')
                                            cls_name_list.append(cls_name)
                                            print('1******************')
                                    except:
                                        pass

if __name__ == '__main__':
    # print(filepath_final1('PageLocators'))
    path = filepath_final1('PageLocators')
    get_dir(path)
    print(cls_name_list)
