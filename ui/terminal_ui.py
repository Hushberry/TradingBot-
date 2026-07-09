"""
terminal_ui.py

Professional Terminal UI
for KAI Bot
"""

import os
import shutil
from colorama import Fore, Style, init

init(autoreset=True)

#=======================================
# TERMINAL SIZE
#=======================================

def width():
    return shutil.get_terminal_size().columns


# =======================================
# CLEAR SCREEN
# =======================================

def clear():
    os.system("cls" if os.name == "nt" else "clear")


# =======================================
#  HORIZONTAL LINE
# =======================================

def line(char="-"):
    print(char * width())


# =======================================
# TITLE BAR
# =======================================

def title(text):

    w = width()

    print("┌" + "─" * (w - 2) + "┐")
    print("│" + text.center(w - 2) + "│")
    print("└" + "─" * (w - 2) + "┘")

# =======================================
# SECTION HEADER
# =======================================

def section(text):

    w = width()

    print()
    print("┌" + "─" * (w - 2) + "┐")
    print("│ " + text.ljust(w - 4) + " │")
    print("└" + "─" * (w - 2) + "┘")


# =======================================
#     INFO ROW
# =======================================

def info(label, value):

    print(f"{label:<18}: {value}")

# ======================================
#    SUCCESS
# ======================================

def success(text):
    print(Fore.GREEN + "✔ " + text)


# =====================================
#    WARNING
# =====================================

def warning(text):
    print(Fore.YELLOW + "▲ " + text)


# ====================================
#    ERROR
# ====================================

def error(text):
    print(Fore.RED + "✖ " + text)


# ====================================
#    FOOTER
# ====================================

def footer(runtime):
    line()

    print(
        f"Runtime : {runtime:.2f}s".ljust(width())
    )