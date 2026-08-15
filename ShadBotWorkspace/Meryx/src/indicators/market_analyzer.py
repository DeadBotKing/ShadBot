from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class PriceBar:
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float

@dataclass(frozen=True)
class IndicatorSignal:
    indicator_name: str
    value: float
    signal_type: str

def calculate_sma(prices: List[float], period: int) -> List[float]:
    if not prices or period <= 0:
        raise ValueError("Invalid input for SMA calculation")
    
    sma_values = []
    window_sum = sum(prices[:period])
    sma_values.append(window_sum / period)
    
    for i in range(period, len(prices)):
        window_sum += prices[i] - prices[i - period]
        sma_values.append(window_sum / period)
    
    return sma_values

def calculate_ema(prices: List[float], period: int) -> List[float]:
    if not prices or period <= 0:
        raise ValueError("Invalid input for EMA calculation")
    
    ema_values = []
    multiplier = 2 / (period + 1)
    ema_values.append(prices[0])
    
    for price in prices[1:]:
        ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(ema)
    
    return ema_values

def calculate_rsi(prices: List[float], period: int = 14) -> List[float]:
    if not prices or period <= 0:
        raise ValueError("Invalid input for RSI calculation")
    
    gains = []
    losses = []
    
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i - 1]
        if diff > 0:
            gains.append(diff)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(-diff)
    
    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period
    
    rs = avg_gain / avg_loss
    rsi_values = [100 - (100 / (1 + rs))]
    
    for i in range(period, len(prices)):
        avg_gain = ((avg_gain * (period - 1)) + gains[i]) / period
        avg_loss = ((avg_loss * (period - 1)) + losses[i]) / period
        rs = avg_gain / avg_loss
        rsi_values.append(100 - (100 / (1 + rs)))
    
    return rsi_values

class MarketAnalyzer:
    def generate_signals(self, prices: List[float], indicator_name: str) -> IndicatorSignal:
        if not prices or len(prices) < 14:
            raise ValueError("Invalid input for signal generation")
        
        rsi = calculate_rsi(prices)
        
        if rsi[-1] < 30:
            signal_type = "BUY"
        elif rsi[-1] > 70:
            signal_type = "SELL"
        else:
            signal_type = "NEUTRAL"
        
        return IndicatorSignal(indicator_name, rsi[-1], signal_type)