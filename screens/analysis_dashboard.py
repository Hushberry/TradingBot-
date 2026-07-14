from ast import Return
from encodings.punycode import T
from turtle import title
from numpy import empty, percentile
from core import config
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime
from colorama import Fore, Style
from screens.dashboard import show_header



LABEL = config.LABEL_WIDTH

console = Console()

def build_confidence_bar(percent):
    """
    Build a graphical confidence bar

    example

    80 ->
    ████████ ░░ 80%
    """
    percent = max(0, min(100, int(percent)))

    filled = percent // 10
    empty = 10 - filled

    return "█" * filled + "░" *empty 

def show_analysis(
    symbol,
    timeframe,
    latest_candle,
    ma50,
    ma200,
    trend,
    market_structure,
    pattern,
    order_blocks,
    liquidity,
    support,
    resistance,
    h1_trend,
    h4_trend,
    mtf_confirmation,
    score,
    percent,
    signal,
    grade,
    entry,
    risk,
):


    LINE = config.LINE_WIDTH

    confidence = percent

    table = Table(show_header=False, box=None)

    table.add_row(
       "Trend",
       signal,
       "Confidence",
      f"{build_confidence_bar(confidence)} {confidence}%"
    )
    table.add_row(
        "AI Score",
        f"{score}/100",
        "AI Grade",
        grade
    )

    table.add_row(
        "Pattern",
        str(pattern),
        "Structure",
        str(market_structure)
    )

    table.add_row(
        "Entry",
        f"{entry:.5f}" if isinstance(entry, float) else str(entry),
        "Support",
        f"{support:.5f}" if isinstance(support, float) else str(support)
    )

    table.add_row(
        "Resistance",
        f"{resistance:.5f}" if isinstance(resistance, float) else str(resistance),
        "MA50",
       f"{ma50:.5f}" if ma50 is not None else "N/A"
    )

    table.add_row(
       "MA200",
        f"{ma200:.5f}",
        "Pattern",
        str(pattern)
   )



    table.add_row(
        "H1",
        str(h1_trend),
        "H4",
        str(h4_trend)
    )

    table.add_row(
        "Confirmation",
        str(mtf_confirmation),
        "",
        ""
    )
    console.print()

    console.print(
        Panel(
            table,
            title=f"[bold cyan]{symbol}[/bold cyan]  ({timeframe})",
            subtitle="KAI Smart Money AI",
            expand=False,
        )
    )
    console.print(show_order_blocks(order_blocks))

    print("=" * 60)
    print("ORDER BLOCK DATA")
    print(order_blocks)
    print(type(order_blocks))
    print("=" * 60)



def show_order_blocks(order_blocks):
    """
    Display Institutional Footprint Summary.
    """

    table = Table(show_header=True, box=None)

    table.add_column("Metric", style="cyan", no_wrap=True)
    table.add_column("Value", style="green")

    if not order_blocks:
        table.add_row("Status", "No Order Blocks")
        return Panel(
            table,
            title="[bold yellow]Institutional Footprint[/bold yellow]",
            border_style="yellow",
            expand=False,
        )

    bullish = len(order_blocks.get("bullish_order_blocks", []))
    bearish = len(order_blocks.get("bearish_order_blocks", []))
    breaker = len(order_blocks.get("breaker_blocks", []))
    mitigated = len(order_blocks.get("mitigated_blocks", []))
    fresh = len(order_blocks.get("fresh_blocks", []))
    invalidated = len(order_blocks.get("invalidated_blocks", []))

    stats = order_blocks.get("statistics", {})
    displacement = stats.get("displacement_count", 0)

    table.add_row("Bullish OB", str(bullish))
    table.add_row("Bearish OB", str(bearish))
    table.add_row("Breaker Blocks", str(breaker))
    table.add_row("Fresh Blocks", str(fresh))
    table.add_row("Mitigated", str(mitigated))
    table.add_row("Invalidated", str(invalidated))
    table.add_row("Displacement", str(displacement))

    return Panel(
        table,
        title="[bold yellow]Institutional Footprint[/bold yellow]",
        border_style="yellow",
        expand=False,
    )




def show_scan_summary(
    total_pairs,
    buy,
    sell,
    wait,
    average_score,
):
    """
    Displays final scan statistics.
    """

    table = Table(title="Market Scan Summary", show_header=True)

    table.add_column("Metric", style="cyan")
    table.add_column("Value", justify="right", style="green")

    table.add_row("Pairs Scanned", str(total_pairs))
    table.add_row("BUY Signals", str(buy))
    table.add_row("SELL Signals", str(sell))
    table.add_row("WAIT Signals", str(wait))

    console.print(table)

    if average_score >= 80:
        institutional_bias = "🟢 Strongly Bullish"

    elif average_score >= 60:
        institutional_bias = "🟢 Bullish"

    elif average_score >= 40:
        institutional_bias = "🟡 Moderately Bullish"

    elif average_score >= 20:
        institutional_bias = "🟠 Neutral"

    else:
        institutional_bias = "🔴 Bearish"

    console.print(f"\nAverage AI Score   : [bold cyan]{average_score:.1f}%[/bold cyan]")
    console.print(f"Institutional Bias : [bold green]{institutional_bias}[/bold green]")

    
def trade_strength(score):

    if score >= 9:
        return "🟢 STRONG BUY"
    
    elif score >= 7:
        return "🟢 BUY"
    
    elif score >= 5:
        return "🟡 WAIT"
    
    elif score >= 3:
        return "🟠 WEAK SELL"
    
    else:
        return "🔴 STRONG SELL"
    