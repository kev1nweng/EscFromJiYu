# Designed for Windows. MAY NOT work on other operating systems.

import sys
import time
from os import system

r = system

stage = "Pre-Alpha"
version = "0.1.0"

r("cls")
time.sleep(1)
print("====================\n >> Escape <<\n====================")
print(stage, version)