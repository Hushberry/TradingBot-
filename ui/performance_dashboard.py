"""
performance_dashboard.py

Displays overall trading
performance statistics.
"""

from colorama import Fore, Style
from ui import terminal_ui


def color_money(value):
    """
    Green if profit.
    Red if loss.
    """

    if value >= 0:
        return Fore.GREEN + f"${value:,.2f}" + Style.RESET_ALL

    return Fore.RED + f"${value:,.2f}" + Style.RESET_ALL


def color_percentage(value):
    """
    Green if >= 50%
    Red otherwise.
    """

    if value >= 50:
        return Fore.GREEN + f"{value:.2f}%" + Style.RESET_ALL

    return Fore.RED + f"{value:.2f}%" + Style.RESET_ALL


def draw(stats):
    """
    Draw performance dashboard.
    """

    terminal_ui.section("PERFORMANCE DASHBOARD")

    print(f"{'Total Trades':<25}: {stats['total_trades']}")

    print(f"{'Winning Trades':<25}: {stats['wins']}")

    print(f"{'Losing Trades':<25}: {stats['losses']}")

    print(f"{'Win Rate':<25}: {color_percentage(stats['win_rate'])}")

    print(f"{'Profit Factor':<25}: {stats['profit_factor']:.2f}")

    print(f"{'Net Profit':<25}: {color_money(stats['net_profit'])}")

    print(f"{'Largest Win':<25}: {color_money(stats['largest_win'])}")

    print(f"{'Largest Loss':<25}: {color_money(stats['largest_loss'])}")

    print(f"{'Average Reward':<25}: {stats['average_rr']:.2f} R")

    print(f"{'Current Streak':<25}: {stats['current_streak']}")

    print(f"{'Best Pair':<25}: {stats['best_pair']}")

    print(f"{'Worst Pair':<25}: {stats['worst_pair']}")

    terminal_ui.line()


