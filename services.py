import os
import shutil
import zipfile
import ctypes
import sys
from win32com.client import Dispatch


def resource_path(relative):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative)


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def get_name_project():
    for i in os.listdir(resource_path("")):
        if i.endswith(".zip"):
            return i.rstrip(".zip")
    return None


def get_path_program():
    path = os.getcwd().split("\\")[0]
    if "Program Files" in os.listdir(path + "\\"):
        path += "\\Program Files\\"
    else:
        path += "\\"
    return path


def install_project(path, checked):
    name = get_name_project()
    if name in os.listdir(path):
        shutil.rmtree(path + name)
    os.mkdir(path + name)
    with zipfile.ZipFile(resource_path(name + ".zip"), "r") as zip_ref:
        zip_ref.extractall(path + name)
    if checked:
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(os.getcwd() + "\\" + name + ".lnk")
        shortcut.Targetpath = path + name + "\\" + name + ".exe"
        shortcut.WorkingDirectory = path
        shortcut.save()
