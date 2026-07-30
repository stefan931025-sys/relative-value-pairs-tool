"""Relative Value Pairs Engine: Tests cointegration and computes spread z-scores for discretionary trading."""

import numpy as np
import pandas as pd
from statsmodels.tsa.stattools import coint
import yfinance as yf


class RelativeValuePairs:

  def __init__(self, ticker_a: str, ticker_b: str, period: str = "1y"):
    self.ticker_a = ticker_a
    self.ticker_b = ticker_b
    self.period = period
    self.data = self._fetch_data()

  def _fetch_data(self) -> pd.DataFrame:
    """Downloads historical adjusted closing prices."""
    df = yf.download(
        [self.ticker_a, self.ticker_b], period=self.period, progress=False
    )["Adj Close"]
    return df.dropna()

  def check_cointegration(self) -> tuple[float, float]:
    """Performs Engle-Granger two-step cointegration test."""
    p1 = self.data[self.ticker_a]
    p2 = self.data[self.ticker_b]
    score, p_value, _ = coint(p1, p2)
    return round(score, 4), round(p_value, 4)

  def calculate_spread_signal(self, window: int = 30) -> pd.DataFrame:
    """Computes hedge ratio, spread, rolling z-score, and trading metrics."""
    p1 = self.data[self.ticker_a]
    p2 = self.data[self.ticker_b]

    # Dynamic Hedge Ratio via OLS
    model = np.polyfit(p2, p1, 1)
    hedge_ratio = model[0]

    spread = p1 - (hedge_ratio * p2)
    rolling_mean = spread.rolling(window=window).mean()
    rolling_std = spread.rolling(window=window).std()

    z_score = (spread - rolling_mean) / rolling_std

    df_result = pd.DataFrame(
        {
            f"{self.ticker_a}_Price": p1,
            f"{self.ticker_b}_Price": p2,
            "Spread": spread,
            "Z_Score": z_score,
        },
        index=self.data.index,
    )

    return df_result, round(hedge_ratio, 4)


if __name__ == "__main__":
  # Example: Goldman Sachs (GS) vs Morgan Stanley (MS)
  pair = RelativeValuePairs("GS", "MS", period="1y")
  coint_score, p_val = pair.check_cointegration()
  df_signals, hedge_ratio = pair.calculate_spread_signal()

  latest_z = df_signals["Z_Score"].iloc[-1]

  print(f"=== RELATIVE VALUE PAIR: GS vs MS ===")
  print(f"Cointegration P-Value: {p_val} (Cointegrated if < 0.05)")
  print(f"Hedge Ratio: {hedge_ratio}")
  print(f"Current Spread Z-Score: {latest_z:.2f}")
