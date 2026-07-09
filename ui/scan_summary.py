"""
scan_summary.py

Displays scan statistics
for KAI Bot.
"""

from colorama import Fore, Style
from ui import terminal_ui

def draw(total, buy, sell, wait):
    """
    Draw Scan Summary.

    Parameters
    ----------
    total : int
    buy   : int
    sell  : int
    wait  : int
    """

    terminal_ui.section("SCAN SUMMARY")

    print(f"{'Pairs Scanned':<25}: {total}")

    print(
        f"{'BUY Signal':<25}:"
        f"{Fore.GREEN}{buy}{Style.RESET_ALL}"
    )

    print(
        f"{'SELL Signals':<25}:"
        f"{Fore.RED}{sell}{Style.RESET_ALL}"
    )

    print(
        f"{'WAIT Signals':<25}:"
        f"{Fore.YELLOW}{wait}{Style.RESET_ALL}"
    )

    terminal_ui.line()
