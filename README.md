# Relative Value Pairs Tool

![CI Workflow](https://github.com/stefan931025-sys/relative-value-pairs-tool/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Discretionary Relative Value & Cointegrated Pairs Trading Decision Engine designed for systematic asset pair monitoring and statistical arbitrage execution.

## 🚀 Quantitative Methodology

* **Cointegration Testing:** Executes Augmented Dickey-Fuller (ADF) tests to verify stationary spread relationships before triggering relative value signals.
* **Dynamic Hedge Ratio Estimation:** Utilizes Ordinary Least Squares (OLS) regression to compute optimal hedge ratios across asset pairs.
* **Execution Framework:** Engine core resides in `core/pairs_engine.py` for modular integration into systematic execution workflows.

---

## 📊 Mathematical Specifications

### 1. OLS Hedge Ratio & Spread Construction

$$Y_{1,t} = \alpha + \beta Y_{2,t} + \varepsilon_t$$

$$S_t = Y_{1,t} - \hat{\beta} Y_{2,t}$$

Where $\hat{\beta}$ is the OLS-estimated hedge ratio and $S_t$ represents the linear combination spread tested for stationarity.

### 2. Augmented Dickey-Fuller (ADF) Stationarity Test

$$\Delta S_t = \alpha + \gamma S_{t-1} + \sum_{i=1}^{k} \delta_i \Delta S_{t-i} + u_t$$

Evaluates the null hypothesis $H_0: \gamma = 0$ (unit root / non-stationary) against $H_1: \gamma < 0$ (mean-reverting cointegrated spread).

### 3. Normalized Z-Score Entry Signal

$$Z_t = \frac{S_t - \mu_s}{\sigma_s}$$

Where $\mu_s$ and $\sigma_s$ denote the rolling mean and standard deviation over lookback window $w$.

---

## 📁 Repository Structure

```text
relative-value-pairs-tool/
├── .devcontainer/     # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions automated test workflow
├── core/
│   └── pairs_engine.py # OLS regression, ADF tests & Z-score modules
├── tests/
│   └── test_pairs_engine.py # Automated pytest suite
├── main.py            # Main execution pipeline script
├── repo_auditor.py    # Static AST analysis governance tool
├── requirements.txt   # Python dependencies
└── README.md          # System documentation
