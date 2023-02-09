from utils.imports import *


def run(inputCommand):
    system(inputCommand)


def cls():
    run("cls")


def wait(waitTime):
    time.sleep(waitTime)


def kill(programName):
    try:
        command = "taskkill >nul /f /im " + programName + " 2>nul"
        run(command)
    except Exception:
        print("\n[!] 执行出现错误。请检查输入内容是否正确后重试。")
