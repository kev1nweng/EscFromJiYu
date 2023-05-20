from utils.shortcuts import *
from utils.imports import *
from utils.func import *

stage = ["Release", "Nightly"][0]
version = "1.3.1"


def waitAndMenu():
    wait(2)
    menu()


def menu():
    funcChoice = ""
    run("mode con cols=60 lines=50")
    run("title>nul EscFromJiYu")
    run("cls")

    if stage == "Release":
        workingStatus = "(Stable)"
    else:
        workingStatus = "(Preview)"

    nameStr = "EscFromJiYu by kW"
    print(nameStr)
    print(stage, version, workingStatus)

    time.sleep(0.1)
    print("\n+菜单\n")
    print("1. 立即结束 极域 主进程")
    print("2. 置顶操作")
    print("+ 2.1 置顶窗口")
    print("+ 2.2 取消置顶")
    print("3. 对进程注入 DLL 文件")
    print("4. 立即蓝屏(可能不成功)")
    print("5. 解除教师断网")
    print("6. 解除U盘限制")
    print("7. 扫描局域网")
    print("8. 向 IP 地址发送消息")
    print("0. 退出")
    print("\n--- Danger Zone ---\n")
    print("X. UDP重放攻击 (by ht0Ruial)")
    print("\n按下 Alt+C 强制解除屏幕广播置顶。\n按下 Alt+X 立即结束极域进程。\n按下 Alt+Z 挂起极域。\n按下 Alt+A 恢复挂起的极域。\n* 此软件仅供学习交流使用，\n作者不对该软件造成的任何事情负责。")

    while True:
        try:
            funcChoiceRaw = input("\n请输入你要执行的功能序号：\n>> ")
            if funcChoiceRaw == "X":
                funcX()
                waitAndMenu()
            else:
                funcChoice = float(funcChoiceRaw)
            break
        except ValueError:
            print("\n[!] 非法输入值。")
            time.sleep(3)
            menu()

    if funcChoice == 0:
        print("\n[!] 正在退出程序...")
        time.sleep(1)
        cls()
        sys.exit(0)

    if funcChoice == 1:
        func1()
        waitAndMenu()

    if funcChoice == 2.1:
        func2_1()
        waitAndMenu()

    if funcChoice == 2.2:
        func2_2()
        waitAndMenu()

    if funcChoice == 3:
        func3()
        waitAndMenu()

    if funcChoice == 4:
        func4()
        waitAndMenu()

    if funcChoice == 5:
        func5()
        waitAndMenu()

    if funcChoice == 6:
        func6()
        waitAndMenu()

    if funcChoice == 7:
        func7()
        menu()

    if funcChoice == 8:
        func8()
        menu()

    menu()
