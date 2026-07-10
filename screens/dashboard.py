import config
import MetaTrader5 as mt5
from datetime import datetime
from colorama import Fore, Style, init


init(autoreset=True)

def show_header(account_info):
    """
    Displays KAI BOT startup terminal.
    """

    print("=" * config.LINE_WIDTH)

    print(f"{config.BOT_NAME} Terminal v{config.VERSION}".center(config.LINE_WIDTH))

    print(f"{config.BOT_SUBTITLE}".center(config.LINE_WIDTH))

    print(f"{config.TAGLINE}".center(config.LINE_WIDTH))
    
    print("=" * config.LINE_WIDTH)

    print(f"{'Bot':<12}: {config.BOT_NAME}")
    print(f"{'Author':<12}: {config.AUTHOR}")
    print(f"{'Version':<12}: {config.VERSION}")
    print(f"{'Broker':<12}: Exness")
    print(f"{'Server':<12}: {account_info.server}")
    print(f"{'Account':<12}: {account_info.login}")
    print(f"{'Balance':<12}: ${account_info.balance:,.2f}")
    print(f"{'Equity':<12}: ${account_info.equity:,.2f}")
    print(f"{'Scan Time':<12}: {datetime.now().strftime('%d %b %Y | %H:%M:%S')}")

    print("=" * config.LINE_WIDTH)
    print("Status       : ✅ Connected to MetaTrader 5")
    print("=" * config.LINE_WIDTH)
    print()

def show_market_watch(symbols):

    print("=" * config.LINE_WIDTH)
    print(f"{'MARKET WATCH':^{config.LINE_WIDTH}}")
    print("=" * config.LINE_WIDTH)

    print(
        f"{'Symbol':<10}"
        f"{'Bid':>14}"
        f"{'Ask':>14}"
        f"{'Spread':>10}"
        f"{'Trend':>12}"
    )

    print("-" * config.LINE_WIDTH)

    for s in symbols:

        trend = s["trend"]

        if "Uptrend" in trend:
            trend = Fore.GREEN + trend + Style.RESET_ALL
        elif "Downtrend" in trend:
            trend = Fore.RED + trend + Style.RESET_ALL
        elif "Pullback" in trend:
            trend = Fore.YELLOW + trend + Style.RESET_ALL

        print(
            f"{s['symbol']:<10}"
            f"{s['bid']:>14.5f}"
            f"{s['ask']:>14.5f}"
            f"{s['spread']:>10.1f}   "
            f"{trend}"
        )

    print("=" * config.LINE_WIDTH)
    print()

def show_progress(current, total, symbol):

    print(f"[{current}/{total}] Scanning {symbol}...")


def show_summary(total, buys, sells, waits):

    print("=" * config.LINE_WIDTH)
    print(f"{'SESSION SUMMARY':^{config.LINE_WIDTH}}")
    print("=" * config.LINE_WIDTH)

    print(f"{'Pairs Scanned':<20}: {total}")
    print(f"{'BUY Signals':<20}: {buys}")
    print(f"{'SELL Signals':<20}: {sells}")
    print(f"{'WAIT':<20}: {waits}")

    print("=" * config.LINE_WIDTH)