import os
from os import path
import shutil


def get_name_project():
    return "AAA"


def get_path_program():
    result_path = os.getcwd().split("\\")[0]
    if "Program Files" in os.listdir(result_path + "\\"):
        result_path += "\\Program Files\\" + get_name_project()
    else:
        result_path += "\\" + get_name_project()
    try:
        os.mkdir(result_path)
    except OSError:
        shutil.rmtree(result_path)
        os.mkdir(result_path)
        print(1)


print(get_path_program())
