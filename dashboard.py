from datetime import datetime
import config

def show_dashboard(account):
    
    current_time = datetime.now()


    print("=" * config.LINE_WIDTH)
    print("         KAI_BOT MARKET TERMINAL")
    print("=" * config.LINE_WIDTH)

    print(f"{'Connection':<12}: ✅ Connected")
    print(f"{'Date':<12}: {current_time.strftime('%d %b %Y')}")
    print(f"{'Time':<12}: {current_time.strftime('%H:%M:%S')}")
    print(f"{'Account':<12}: {account.login}")
    print(f"{'Server':<12}: {account.server}")
    print(f"{'Balance':<12}: ${account.balance:,.2f}")
    print(f"{'Equity':<12}: ${account.equity:,.2f}")

    print()

    print("=" * config.LINE_WIDTH)
    print(f"{'Symbol':<12}{'Bid':<14}{'Ask':<14}{'Spread':<10}{'Volume':<12}")
    print("=" * config.LINE_WIDTH)


def show_market(symbol, bid, ask, spread, volume):
    print(
        f"{symbol:<12}"
        f"{bid:<14.5f}"
        f"{ask:<14.5f}"
        f"{spread:<10.1f}"
        f"{volume:.2f}"
    )


def finish_dashboard():
    print("=" * config.LINE_WIDTH)