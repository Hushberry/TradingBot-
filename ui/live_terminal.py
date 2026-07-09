"""
live_terminal.py

Main dashboard renderer
for KAI Bot.
"""

from ui import  terminal_ui
from ui import  account_overview
from ui import  market_watch
from ui import  trade_card
from ui import  open_positions
from ui import  trade_history
from ui import  performance_dashboard
from ui import  scan_summary


def render(
    account,
    market,
    best_trade,
    positions,
    history,
    performance,
    summary,
):
    """
    Draws the complete KAI Dashboard.
    """

    terminal_ui.clear()

    terminal_ui.title("KAI BOT AI TRADING TERMINAL")

    account_overview.draw(account)

    print()

    market_watch.draw(market)

    print()

    trade_card.draw(best_trade)

    print()

    open_positions.draw(positions)

    print()

    trade_history.draw(history)

    print()

    performance_dashboard.draw(performance)

    print()

    scan_summary.draw(
        summary["total"],
        summary["buy"],
        summary["sell"],
        summary["wait"],
    )


