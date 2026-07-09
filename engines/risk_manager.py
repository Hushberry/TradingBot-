import MetaTrader5 as mt5

def get_account_info():
    """
    Returns account information.
    """

    account = mt5.account_info()
    if account is None:
        return None
    
    return{
        "balance": account.balance,
        "equity": account.equity,
        "margin": account.margin,
        "free_margin": account.margin_free,
        "margin_level": account.margin_level,
        "profit": account.profit,
    }

def calculate_risk_amount(balance, risk_percent=1.0):
    """
    Calculates the dollar amount to risk.
    """

    return balance * (risk_percent / 100)


def can_trade(account, minimum_margin=100):
    """
    Checks if enough free margin exists.
    """
    if account["free_margin"] < minimum_margin:
        return False
    
    return True

def calculate_drawdown(balance, equity):
    """
    Calculates current drawdown.
    """

    if balance == 0:
        return 0
    
    return((balance - equity) / balance) * 100

def max_daily_loss(balance, percent=5):
    """
    Maximum loss allowed today.
    """

    return balance * (percent / 100)

def max_daily_profit(balance, percent=10):
    """
    Daily profit target.
    """
    return balance * (percent / 100)

def risk_report(risk_percent=1):
    """
    Complete account risk report.
    """

    account = get_account_info()

    if account is None:
        return None
    
    balance = account["balance"]
    equity = account["equity"]

    return {
        "balance": balance,
        "equity": equity,
        "free_margin": account["free_margin"],
        "risk_amount": calculate_risk_amount(balance, risk_percent),
        "drawdown": calculate_drawdown(balance, equity),
        "max_daily_loss": max_daily_loss(balance),
        "max_daily_profit": max_daily_profit(balance),
        "can_trade": can_trade(account),
    }