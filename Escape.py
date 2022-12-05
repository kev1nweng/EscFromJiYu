# 此程序为Windows设计，在其它操作系统上会出现兼容性问题。

from utils.shortcuts import *
from utils.imports import *
from utils.functions import *

# 防止 Ctrl+C Traceback 并退出
def signal_handler(signal,frame):

    print('\n\n[!] 你按下了Ctrl+C，正在退出程序...')
    time.sleep(1)
    cls()
    sys.exit(0)

signal.signal(signal.SIGINT,signal_handler)

menu()