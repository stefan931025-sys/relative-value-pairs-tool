# Relative Value Pairs Tool

![CI Workflow](https://github.com/stefan931025-sys/relative-value-pairs-tool/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Discretionary Relative Value & Cointegrated Pairs Trading Decision Engine designed for systematic asset pair monitoring and statistical arbitrage execution[span_2](start_span)[span_2](end_span)[span_3](start_span)[span_3](end_span).

## 🚀 Quantitative Methodology

* **Cointegration Testing:** Executes Augmented Dickey-Fuller (ADF) tests to verify stationary spread relationships before triggering relative value signals[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).
* **Dynamic Hedge Ratio Estimation:** Utilizes Ordinary Least Squares (OLS) regression to compute optimal hedge ratios across asset pairs[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
* **Execution Framework:** Engine core resides in `core/pairs_engine.py` for modular integration into systematic execution workflows[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).

---

## 📊 Mathematical Specifications

### 1. OLS Hedge Ratio & Spread Construction

$$Y_{1, t} = \alpha + \beta Y_{2, t} + \varepsilon_t$$

$$S_t = Y_{1, t} - \hat{\beta} Y_{2, t}$$

Where $\hat{\beta}$ is the OLS-estimated hedge ratio and $S_t$ represents the linear combination spread tested for stationarity[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).

### 2. Augmented Dickey-Fuller (ADF) Stationarity Test

$$\Delta S_t = \alpha + \gamma S_{t-1} + \sum_{i=1}^{k} \delta_i \Delta S_{t-i} + u_t$$

Evaluates the null hypothesis $H_0: \gamma = 0$ (unit root / non-stationary) against $H_1: \gamma < 0$ (mean-reverting cointegrated spread)[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).

### 3. Normalized Z-Score Entry Signal

$$Z_t = \frac{S_t - \mu_s}{\sigma_s}$$

Where $\mu_s$ and $\sigma_s$ denote the rolling mean and standard deviation over lookback window $w$[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).

---

## 📁 Repository Structure

```text
relative-value-pairs-tool/
├── .devcontainer/             # Devcontainer configuration for Codespaces[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions automated test workflow[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)
├── core/
│   └── pairs_engine.py        # OLS regression, ADF tests & Z-score modules[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span)
├── tests/
│   └── test_pairs_engine.py   # Automated pytest suite[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span)
├── main.py                    # Main execution pipeline script[span_24](start_span)[span_24](end_span)[span_25](start_span)[span_25](end_span)
├── repo_auditor.py            # Static AST analysis governance tool[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span)
├── requirements.txt           # Python dependencies[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span)
└── README.md                  # System documentation[span_30](start_span)[span_30](end_span)[span_31](start_span)[span_31](end_span)
