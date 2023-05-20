# 此程序为Windows设计，在其它操作系统上会出现兼容性问题。

from utils.shortcuts import *
from utils.imports import *
from utils.func import *
from utils.menu import *

ALT = False
Z = False
X = False
C = False
Z = False
A = False

jiYuHandle = win32gui.FindWindow(None, "屏幕广播")

def listenKeyboard():  # 键盘监听函数
    def on_press(key):
        global ALT, Z, X, C, Z, A
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            ALT = True
        if key == keyboard.KeyCode(char="c") or key == keyboard.KeyCode(char="C"):
            C = True
        if key == keyboard.KeyCode(char="x") or key == keyboard.KeyCode(char="X"):
            X = True
        if key == keyboard.KeyCode(char="z") or key == keyboard.KeyCode(char="Z"):
            Z = True
        if key == keyboard.KeyCode(char="a") or key == keyboard.KeyCode(char="A"):
            A = True

        if ALT and C:
            ALT = C = False
            disableJiyuPin()

        if ALT and X:
            ALT = X = False
            kill("StudentMain.exe")

        if ALT and Z:
            ALT = Z = False
            win32api.SendMessage(jiYuHandle, 0x0112, 0xF170, 2)

        if ALT and A:
            ALT = A = False
            win32api.SendMessage(jiYuHandle, 0x0112, 0xF170, -1)

    def on_release(key):
        global ALT, Z, X, C
        if (
            key == keyboard.Key.alt
            or key == keyboard.Key.alt_l
            or key == keyboard.Key.alt_r
        ):
            ALT = False
        if key == keyboard.KeyCode(char="c") or key == keyboard.KeyCode(char="C"):
            C = False
        if key == keyboard.KeyCode(char="x") or key == keyboard.KeyCode(char="X"):
            X = False
        if key == keyboard.KeyCode(char="z") or key == keyboard.KeyCode(char="Z"):
            Z = False
        if key == keyboard.KeyCode(char="a") or key == keyboard.KeyCode(char="A"):
            A = False

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


listenerThread = threading.Thread(target=listenKeyboard)
listenerThread.start()


# 防止 Ctrl+C Traceback 并退出
def signal_handler(signal, frame):
    print("\n\n[!] 你按下了Ctrl+C，正在退出程序...")
    time.sleep(1)
    cls()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

menu()
