def show_dashboard(account):
    print("=" * 60)
    print("         KAI_BOT MARKET TERMINAL")
    print("=" * 60)

    print("Connection : ✅ Connected")
    print(f"Account    : {account.login}")
    print(f"Balance    : ${account.balance:,.2f}")
    print(f"Equity     : ${account.equity:,.2f}")
    print(f"Server     : {account.server}")

    print()

    print("=" * 60)
    print(f"{'Symbol':<12}{'Bid':<14}{'Ask':<14}{'Spread':<10}{'Volume'}")
    print("=" * 60)


def show_market(symbol, bid, ask, spread, volume):
    print(
        f"{symbol:<12}"
        f"{bid:<14}"
        f"{ask:<14}"
        f"{spread:<10.1f}"
        f"{volume:.2f}"
    )


def finish_dashboard():
    print("=" * 60)