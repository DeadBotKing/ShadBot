"""
Enterprise Financial Indicator Engine.

Production-grade market analysis service implementing SMA, EMA, RSI,
and trading signal generation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence


@dataclass(frozen=True, slots=True)
class PriceBar:
    """
    Immutable time-series price bar.
    """

    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: int


@dataclass(frozen=True, slots=True)
class IndicatorSignal:
    """
    Generated trading indicator signal.
    """

    indicator_name: str
    value: float
    signal_type: str  # BUY, SELL, NEUTRAL


def calculate_sma(prices: Sequence[float], period: int) -> list[float]:
    """
    Calculate Simple Moving Average (SMA).
    """

    if not prices or period <= 0 or len(prices) < period:
        raise ValueError("Invalid input prices or period for SMA calculation.")

    sma_values: list[float] = []
    window_sum = sum(prices[:period])
    sma_values.append(window_sum / period)

    for i in range(period, len(prices)):
        window_sum += prices[i] - prices[i - period]
        sma_values.append(window_sum / period)

    return sma_values


def calculate_ema(prices: Sequence[float], period: int) -> list[float]:
    """
    Calculate Exponential Moving Average (EMA).
    """

    if not prices or period <= 0 or len(prices) < period:
        raise ValueError("Invalid input prices or period for EMA calculation.")

    ema_values: list[float] = []
    multiplier = 2.0 / (period + 1.0)
    current_ema = sum(prices[:period]) / period
    ema_values.append(current_ema)

    for i in range(period, len(prices)):
        current_ema = (prices[i] - current_ema) * multiplier + current_ema
        ema_values.append(current_ema)

    return ema_values


def calculate_rsi(prices: Sequence[float], period: int = 14) -> list[float]:
    """
    Calculate Relative Strength Index (RSI) returning values between 0 and 100.
    """

    if not prices or period <= 0 or len(prices) <= period:
        raise ValueError("Invalid input prices or period for RSI calculation.")

    gains: list[float] = []
    losses: list[float] = []

    for i in range(1, len(prices)):
        change = prices[i] - prices[i - 1]
        gains.append(max(0.0, change))
        losses.append(max(0.0, -change))

    avg_gain = sum(gains[:period]) / period
    avg_loss = sum(losses[:period]) / period

    rsi_values: list[float] = []
    for i in range(period, len(gains)):
        avg_gain = (avg_gain * (period - 1) + gains[i]) / period
        avg_loss = (avg_loss * (period - 1) + losses[i]) / period
        if avg_loss == 0:
            rsi_values.append(100.0)
        else:
            rs = avg_gain / avg_loss
            rsi_values.append(100.0 - (100.0 / (1.0 + rs)))

    return rsi_values


class MarketAnalyzer:
    """
    Signal Generator service evaluating market indicators.
    """

    def evaluate_rsi(self, rsi_value: float) -> IndicatorSignal:
        if rsi_value < 30.0:
            return IndicatorSignal("RSI", round(rsi_value, 2), "BUY")
        if rsi_value > 70.0:
            return IndicatorSignal("RSI", round(rsi_value, 2), "SELL")
        return IndicatorSignal("RSI", round(rsi_value, 2), "NEUTRAL")

    def analyze_market(self, prices: Sequence[float], period: int = 14) -> list[IndicatorSignal]:
        rsi_vals = calculate_rsi(prices, period)
        return [self.evaluate_rsi(val) for val in rsi_vals]