"""
 open_positions.py

 Displays all currently 
 open postitions.
"""

from colorama import Fore, Style
from ui import terminal_ui

def color_profit(profit):
    """
    Returns profit with color.
    """
    if profit > 0:
        return Fore.GREEN + f"${profit:2f}" + Style.RESET_ALL
    
    elif profit < 0:
        return Fore.RED + f"${profit:.2f}" + Style.RESET_ALL
    
    return Fore.YELLOW + f"${profit:.2f}" + Style.RESET_ALL


def color_type(order_type):
    """
    BUY -> Green
    SELL -> Red
    """

    if order_type.upper() == "BUY":
        return Fore.GREEN + "BUY" + Style.RESET_ALL
    
    return Fore.RED + "SELL" + Style.RESET_ALL


def draw(positions):
    """
    Draw all open positions.

    positions = List of dictionaries
    """

    terminal_ui.section("OPEN POSITIONS")

    if len(positions) == 0:
        print(Fore.YELLOW + "No Open Positions." + Style.RESET_ALL)
        terminal_ui.line()
        return
    
    print(
        f"{'Symbol':<12}"
        f"{'Type':<10}"
        f"{'Lot':<10}"
        f"{'Open Price':<16}"
        f"{'Profit':<15}"
    )

    terminal_ui.line()

    for pos in positions:
        trade_type = color_type(pos["type"])

        profit = color_profit(pos["profit"])

        print(
            f"{pos['symbol']:<12}"
            f"{trade_type:<18}"
            f"{pos['lot']:<10.2f}"
            f"{pos['price']:<16.5f}"
            f"{profit}"
        )

        terminal_ui.line()