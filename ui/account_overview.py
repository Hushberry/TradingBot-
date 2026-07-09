"""
account_overview.py

Displays account statistics
for KAI Bot
"""
from turtle import left
from colorama import Fore, Style
from ui import  terminal_ui


def money(value):
    return f"${value:.2f}"

def status(active):
    if active:
        return Fore.GREEN + "Active" + Style.RESET_ALL
    
    return Fore.RED + "Blocked" + Style.RESET_ALL 

def draw(account):

    terminal_ui.section("Account Overview")
    left_width = 32
    right_width = 39

    print("┌" + "─" * left_width + "┬" + "─" * right_width + "┐")
    
    print(
        f"| Balance       {money(account['balance']):<17}"
        f"| Drawdown      {account['drawdown']:.1f}%{'':<14}    |"
    )

    print(
        f"| Equity        {money(account['equity']):<17}"
        f"| Daily Loss    {money(account['max_daily_loss']):<17}       |"
    )

    print(
        f"| Free Margin   {money(account['free_margin']):<17}"
        f"| Daily Target  {money(account['max_daily_profit']):<17}       |"
    )

    print(
        f"| Risk/Trade    {money(account['risk_amount']):<17}" 
        f"| Status        {status(account['can_trade']):<26}       |"
    )

    print("└" + "─" * left_width + "┴" + "─" * right_width + "┘")