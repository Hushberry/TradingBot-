"""
market_watch.py

Professional Market Watch
for KAI Bot
"""

from colorama import Fore, Style
from ui import terminal_ui

def color_signal(signal):
    """
    Returns a colored BUY/SELL/WAIT signal.
    """

    if "BUY" in signal:
        return Fore.GREEN + signal + Style.RESET_ALL
    
    elif "SELL" in signal:
        return Fore.RED + signal + Style.RESET_ALL
    
    return Fore.YELLOW + signal + Style.RESET_ALL

def color_confidence(confidence):
    """
    Color confidence level.
    """

    if confidence >= 80:
        return Fore.GREEN + f"{confidence}%"
    
    elif confidence >= 60:
        return Fore.CYAN + f"{confidence}%"
    
    elif confidence >= 40:
        return Fore.YELLOW + f"{confidence}%"
    
    return Fore.RED + f"{confidence}%"

def draw(data):
    """
    Draws the professional Market Watch table.
    """

    terminal_ui.section("MARKET WATCH")

    print(
        f"{'Symbol':<12}"
        f"{'Trend':<18}"
        f"{'Signal':<14}"
        f"{'Confidence':<15}"
        f"{'Spread':<12}"
        f"{'Status'}"
    )

    terminal_ui.line()

    for row in data:
        signal = color_signal(row["signal"])

        confidence = color_confidence(row["confidence"])

        spread = row["spread"]

        if spread <= 20:
            status = Fore.GREEN + "GOOD"

        elif spread <= 60:
            status = Fore.YELLOW + "NORMAL"

        else:
            status = Fore.RED + "HIGH"

        status += Style.RESET_ALL

        print(
            f"{row['symbol']:<12}"
            f"{row['trend']:<18}"
            f"{signal:<22}"
            f"{confidence:<18}"
            f"{spread:<12.1f}"
            f"{status}"
        )
    terminal_ui.line()

