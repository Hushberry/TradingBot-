"""
trade_history.py

Displays recently closed trades
for KAI Bot.
"""

from colorama import Fore, Style
from ui import  terminal_ui


def color_profit(value):
    """
    Colors profit/loss.

    Profit -> Green
    Loss -> Red
    """

    if value >= 0:
        return Fore.GREEN + f"${value:.2f}" + Style.RESET_ALL

    return Fore.RED + f"${value:.2f}" + Style.RESET_ALL


def draw(history):
    """
    Draw Trade History table.
    """

    terminal_ui.section("TRADE HISTORY")

    print(
        f"{'Ticket':<12}"
        f"{'Symbol':<12}"
        f"{'Type':<10}"
        f"{'Lots':<10}"
        f"{'Profit':<15}"
    )

    terminal_ui.line()

    for trade in history:

        profit = color_profit(trade["profit"])

        print(
            f"{trade['ticket']:<12}"
            f"{trade['symbol']:<12}"
            f"{trade['type']:<10}"
            f"{trade['lots']:<10.2f}"
            f"{profit}"
        )

    terminal_ui.line()