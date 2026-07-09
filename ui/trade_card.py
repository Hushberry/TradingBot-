"""
trade_card.py

Displays the highest quality trade 
found by KAI Bot.
"""
from colorama import Fore, Style
from ui import terminal_ui


def color_signal(signal):
    """
    Returns colored BUY / SELL / WAIT.
    """

    if "BUY" in signal:
        return Fore.GREEN + signal + Style.RESET_ALL
    
    elif "SELL" in signal:
        return Fore.RED + signal + Style.RESET_ALL
    
    return Fore.YELLOW + signal + Style.RESET_ALL


def confidence_bar(confidence):
    """
    Converts confidenec percentage
    into stars.
    """

    stars = round(confidence / 20)

    return "⭐" * stars + "☆" * (5 - stars)


def draw(trade):
    """
    Draw Trade Card
    """

    terminal_ui.section("Best Trade")

    print(f"{'Symbol':<18}: {trade['symbol']}")
    print(f"{'Signal':<18}: {color_signal(trade['signal'])}")

    print(
        f"{'Confidence':<18}:"
        f"{confidence_bar(trade['confidence'])}"
        f"({trade['confidence']}%)"
    )

    print(f"{'Trend':<18}: {trade['trend']}")
    print(f"{'Pattern':<18}: {trade['pattern']}")
    print(f"{'Structure':<18}: {trade['structure']}")
    print(f"{'Support':<18}: {trade['support']:.5f}")
    print(f"{'Resistance':<18}: {trade['resistance']:.5f}")
    print(f"{'Risk':<18}: {trade['risk']}")
    print(f"{'Reward':<18}: {trade['reward']}")

    terminal_ui.line