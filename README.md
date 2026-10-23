![CI Pipeline](https://github.com/stefan931025-sys/relative-value-pairs-tool/actions/workflows/ci.yml/badge.svg)

# Relative Value Pairs Tool

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
Discretionary Relative Value & Cointegrated Pairs Trading Decision Engine designed for systematic asset pair monitoring and statistical arbitrage execution[span_11](start_span)[span_11](end_span).

---

## 📌 Quantitative Methodology

* **Cointegration Testing:** Executes Augmented Dickey-Fuller (ADF) tests to verify stationary spread relationships before triggering relative value signals[span_12](start_span)[span_12](end_span).
* **Dynamic Hedge Ratio Estimation:** Utilizes Ordinary Least Squares (OLS) regression to compute optimal hedge ratios across asset pairs[span_13](start_span)[span_13](end_span).
* **Execution Framework:** Engine core resides in `src/pairs_engine.py` for modular integration into execution workflows[span_14](start_span)[span_14](end_span).

---

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/stefan931025-sys/relative-value-pairs-tool.git](https://github.com/stefan931025-sys/relative-value-pairs-tool.git)
cd relative-value-pairs-tool

# Run relative value engine
python src/pairs_engine.py
