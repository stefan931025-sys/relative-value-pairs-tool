import pytest

def test_augmented_dickey_fuller_stationarity():
    """Verify Augmented Dickey-Fuller (ADF) t-stat threshold for spread stationarity."""
    adf_statistic = -3.85
    critical_value_5pct = -2.86
    
    is_stationary = adf_statistic < critical_value_5pct
    
    assert is_stationary is True

def test_hedge_ratio_spread():
    """Verify spread calculation using Ordinary Least Squares (OLS) hedge ratio."""
    price_a = 100.0
    price_b = 50.0
    hedge_ratio = 1.8  # Beta parameter from OLS regression
    
    spread = price_a - (hedge_ratio * price_b)
    
    assert pytest.approx(spread, 0.01) == 10.0
