# Relative Value Pairs Tool

[![Relative Value Pairs Tool CI](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/stefan931025-sys/relative-value-pairs-tool)
[![Python Version](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Discretionary Relative Value & Cointegrated Pairs Trading Decision Engine designed for systematic asset pair monitoring and statistical arbitrage execution[span_6](start_span)[span_6](end_span).

---

## Quantitative Methodology

* **Cointegration Testing:** Executes Augmented Dickey-Fuller (ADF) tests to verify stationary spread relationships before triggering relative value signals[span_7](start_span)[span_7](end_span).
* **Dynamic Hedge Ratio Estimation:** Utilizes Ordinary Least Squares (OLS) regression to compute optimal hedge ratios across asset pairs[span_8](start_span)[span_8](end_span).
* **Execution Framework:** Engine core resides in `core/pairs_engine.py` for modular integration into systematic execution workflows[span_9](start_span)[span_9](end_span).

---

## Mathematical Specifications

### 1. OLS Hedge Ratio & Spread Construction
$$Y_{1,t} = \alpha + \beta Y_{2,t} + \varepsilon_t$$
$$S_t = Y_{1,t} - \hat{\beta} Y_{2,t}$$
Where $\hat{\beta}$ is the OLS-estimated hedge ratio and $S_t$ represents the linear combination spread tested for stationarity.

### 2. Augmented Dickey-Fuller (ADF) Stationarity Test
$$\Delta S_t = \alpha + \gamma S_{t-1} + \sum_{i=1}^{p} \delta_i \Delta S_{t-i} + u_t$$
Evaluates the null hypothesis $H_0: \gamma = 0$ (unit root / non-stationary) against $H_1: \gamma < 0$ (mean-reverting cointegrated spread).

### 3. Normalized Z-Score Entry Signal
$$Z_t = \frac{S_t - \mu_{S, w}}{\sigma_{S, w}}$$
Where $\mu_{S, w}$ and $\sigma_{S, w}$ denote the rolling mean and standard deviation over lookback window $w$.

---

## System Architecture & Data Flow

```text
+-----------------------------------------------------------------------------------+
|                        PAIRED ASSET PRICE & RETURN SERIES                         |
|                    (Synchronized Historical & Live Price Feeds)                   |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                      COINTEGRATION & HEDGE RATIO ESTIMATOR                        |
|  * OLS Dynamic Hedge Ratio ($\hat{\beta}$)   * ADF Unit Root Stationarity Filter  |
|  * Spread Residual Construction ($S_t$)       * Rolling Z-Score Normalization     |
+-----------------------------------------------------------------------------------+
                                          |
                                          v
+-----------------------------------------------------------------------------------+
|                       RELATIVE VALUE DECISION & RISK ENGINE                       |
|            (Mean-Reversion Entry/Exit Signals & Pair Allocation Sizing)           |
+-----------------------------------------------------------------------------------+
