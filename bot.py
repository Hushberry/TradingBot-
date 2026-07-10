from datetime import datetime, timedelta
import time
import config
import logger
import mt5_connector
import screens.dashboard as dashboard
import MetaTrader5 as mt5
from engines import candle_engine
from engines import trend_engine
from engines import pattern_engine
from engines import support_engine
from engines import signal_engine
import analysis_dashboard
from engines import confirmation_engine
from engines import mtf_engine
from engines import risk_manager
from engines import entry_engine
from ui import terminal_ui
from ui import market_watch
from ui import trade_card
from ui import account_overview
from ui import scan_summary
from ui import open_positions
from ui import trade_history
from ui import performance_dashboard
from ui import live_terminal
from screens import dashboard
from engines import ai_score_engine


start_time = time.time()
# ==========================================
# START BOT
# ==========================================


start_time = time.time()

logger.log("KAI_Bot has started.")

mt5_connector.connect_to_mt5()

account = mt5.account_info()
risk = risk_manager.risk_report(1)

terminal_ui.clear()

dashboard.show_header(account)



account_data = {
    "balance": risk["balance"],
    "equity": risk["equity"],
    "free_margin": risk["free_margin"],
    "risk_amount": risk["risk_amount"],
    "drawdown": risk["drawdown"],
    "max_daily_loss": risk["max_daily_loss"],
    "max_daily_profit": risk["max_daily_profit"],
    "can_trade": risk["can_trade"],
}
account_overview.draw(account_data)
# ==========================================
# OPEN POSITIONS
# ==========================================


raw_positions = mt5.positions_get()

positions = []
if raw_positions:
    for pos in raw_positions:
        positions.append({
            "symbol": pos.symbol,
            "type": "BUY" if pos.type == mt5.ORDER_TYPE_BUY else "SELL",
            "lot": pos.volume,
            "price": pos.price_open,
            "profit": pos.profit,
        })

# ==========================================
# TRADE HISTORY
# ==========================================

date_from = datetime.now() - timedelta(days=7)
date_to = datetime.now()

raw_history = mt5.history_deals_get(date_from, date_to)

history = []
if raw_history:
    for deal in raw_history:
        history.append({
            "ticket": deal.ticket,
            "symbol": deal.symbol,
            "type": "BUY" if deal.type == mt5.DEAL_TYPE_BUY else "SELL",
            "lots": deal.volume,
            "profit": deal.profit,
        })

# ==========================================
# PERFORMANCE CALCULATION
# ==========================================

def calculate_performance(history):
    if not history:
        return {
            "total_trades": 0, "wins": 0, "losses": 0, "win_rate": 0,
            "profit_factor": 0, "net_profit": 0, "largest_win": 0,
            "largest_loss": 0, "average_rr": 0, "current_streak": 0,
            "best_pair": "N/A", "worst_pair": "N/A",
        }
    wins = [t for t in history if t["profit"] > 0]
    losses = [t for t in history if t["profit"] < 0]
    total_trades = len(history)
    win_count = len(wins)
    loss_count = len(losses)
    win_rate = (win_count / total_trades * 100) if total_trades else 0
    gross_profit = sum(t["profit"] for t in wins)
    gross_loss = abs(sum(t["profit"] for t in losses))
    profit_factor = (gross_profit / gross_loss) if gross_loss > 0 else 0
    net_profit = sum(t["profit"] for t in history)
    largest_win = max((t["profit"] for t in wins), default=0)
    largest_loss = min((t["profit"] for t in losses), default=0)
    avg_win = (gross_profit / win_count) if win_count else 0
    avg_loss = (gross_loss / loss_count) if loss_count else 0
    average_rr = (avg_win / avg_loss) if avg_loss else 0
    streak = 0
    for t in reversed(history):
        if t["profit"] > 0:
            if streak >= 0:
                streak += 1
            else:
                break
        elif t["profit"] < 0:
            if streak <= 0:
                streak -= 1
            else:
                break
    pair_profit = {}
    for t in history:
        pair_profit.setdefault(t["symbol"], 0)
        pair_profit[t["symbol"]] += t["profit"]
    best_pair = max(pair_profit, key=pair_profit.get) if pair_profit else "N/A"
    worst_pair = min(pair_profit, key=pair_profit.get) if pair_profit else "N/A"
    return {
        "total_trades": total_trades,
        "wins": win_count,
        "losses": loss_count,
        "win_rate": win_rate,
        "profit_factor": profit_factor,
        "net_profit": net_profit,
        "largest_win": largest_win,
        "largest_loss": largest_loss,
        "average_rr": average_rr,
        "current_streak": streak,
        "best_pair": best_pair,
        "worst_pair": worst_pair,
    }

performance = calculate_performance(history)


# ==========================================
# SETTINGS
# ==========================================

SYMBOLS = [
    "XAUUSDm",
    "EURUSDm",
    "GBPUSDm",
    "USDJPYm",
    "USDCHFm",
    "USDCADm",
    "UKOILm",
    "USOILm",
    "BTCUSDm",
    "ETHUSDm",
]

TIMEFRAME = mt5.TIMEFRAME_H1
CANDLE_COUNT = 500



best_trade = None
highest_score = -1 

# ==========================================
# MARKET WATCH
# ==========================================

market_data = []

for symbol in SYMBOLS:

    info = mt5.symbol_info(symbol)
    tick = mt5.symbol_info_tick(symbol)

    if info is None or tick is None:
        continue

    # Download candles
    rates = candle_engine.get_historical_candles(
        symbol,
        TIMEFRAME,
        CANDLE_COUNT
    )

    if rates is None:
        continue

    # Latest price
    latest_price = rates[-1]["close"]

    # Calculate moving averages
    ma50 = trend_engine.calculate_ma(rates, 50)
    ma200 = trend_engine.calculate_ma(rates, 200)

    # Detect trend
    trend = trend_engine.analyze_trend(
        latest_price,
        ma50,
        ma200
    )

    # Spread
    spread = (tick.ask - tick.bid) / info.point

    # Trade bias (BUY/SELL/WAIT)
    signal = signal_engine.get_trade_bias(trend)

    # Candlestick pattern
    pattern = pattern_engine.analyze_patterns(rates)

    # Multi-timeframe confirmation (H1 vs H4)
    h1_trend = mtf_engine.get_timeframe_trend(symbol, mt5.TIMEFRAME_H1)
    h4_trend = mtf_engine.get_timeframe_trend(symbol, mt5.TIMEFRAME_H4)
    mtf_confirmation = mtf_engine.compare_trends(h1_trend, h4_trend)

    # Market structure — not built yet, stubbed for now
    market_structure = "N/A"

    # Confirmation score
    result = confirmation_engine.calculate_trade_score(
        trend,
        pattern,
        market_structure,
        mtf_confirmation,
        signal,
    )

    percent = result["percent"]

    
    market_data.append({
        "symbol": symbol,
        "trend": trend,
        "signal": signal,
        "confidence": percent,
        "spread": spread,
        "bid": tick.bid,
        "ask": tick.ask,
    })

# Show Market Watch
dashboard.show_market_watch(market_data)

print()

buy_count = 0
sell_count = 0
wait_count = 0

total_ai_score = 0  


for symbol in SYMBOLS:

    rates = candle_engine.get_historical_candles(
        symbol,
        TIMEFRAME,
        CANDLE_COUNT
    )

    if rates is None:
        continue

    latest_candle = rates[-1]
    latest_price = latest_candle["close"]

    # -------------------------
    # Trend Analysis
    # -------------------------

    ma50 = trend_engine.calculate_ma(rates, 50)
    ma200 = trend_engine.calculate_ma(rates, 200)

    trend = trend_engine.analyze_trend(
        latest_price,
        ma50,
        ma200
    )

    market_structure = trend_engine.get_market_structure(rates)

    pattern = pattern_engine.analyze_patterns(rates)

    support = support_engine.find_support(rates)
    resistance = support_engine.find_resistance(rates)

    # -------------------------
    # Trade Signal
    # -------------------------

    signal = signal_engine.get_trade_bias(trend)
    
    if signal == "✅ BUY":
       buy_count += 1

    elif signal == "🔴 SELL":
      sell_count += 1

    elif signal == "⏯  WAIT":
        wait_count += 1
    entry = entry_engine.get_entry_price(
        signal,
        latest_candle
    )

    # -------------------------
    # Multi Timeframe
    # -------------------------

    h1_trend = mtf_engine.get_timeframe_trend(
        symbol,
        config.TIMEFRAME
    )

    h4_trend = mtf_engine.get_timeframe_trend(
        symbol,
        config.HIGHER_TIMEFRAME
    )

    mtf_confirmation = mtf_engine.compare_trends(
        h4_trend,
        h1_trend
    )

    # -------------------------
    # AI Confidence
    # -------------------------

    ai = ai_score_engine.calculate_score(
    trend,
    pattern,
    market_structure,
    mtf_confirmation,
    ma50,
    ma200,
    latest_candle["close"]
)

    score = ai["score"]
    percent = ai["percent"]
    grade = ai["grade"]

    total_ai_score += percent

    average_score = total_ai_score / len(market_data)



    
    # -------------------------
    # Display Analysis
    # -------------------------

    analysis_dashboard.show_analysis(
        symbol,
        candle_engine.get_timeframe_name(TIMEFRAME),
        latest_candle,
        ma50,
        ma200,
        trend,
        market_structure,
        pattern,
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
    )

    print()

# ==========================================
# SCAN SUMMARY
# ==========================================

analysis_dashboard.show_scan_summary(
    len(market_data),
    buy_count,
    sell_count,
    wait_count,
    average_score
)

print()

print("=" * config.LINE_WIDTH)

print("KAI SMART MONEY AI v3.0".center(config.LINE_WIDTH))

print("(Core Engine)".center(config.LINE_WIDTH))

print("Institutional Trading Intelligence".center(config.LINE_WIDTH))

print("Powered by Smart Money Concepts + AI".center(config.LINE_WIDTH))

print("=" * config.LINE_WIDTH)

print(f"Scan Completed Successfully".center(config.LINE_WIDTH))

print("=" * config.LINE_WIDTH)

runtime = time.time() - start_time

print(f"\nTotal Runtime : {runtime:.2f} seconds")