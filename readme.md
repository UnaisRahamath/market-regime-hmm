Abstract
- This project applies advanced statistical learning and probabilistic modeling to uncover latent market regimes in equity index data and exploit regime structure for return forecasting. Using a Hidden Markov Model (HMM) trained on transformed return and volatility features, the system detects persistent market states and demonstrates that regime-aware forecasts significantly outperform classical time-series baselines.

Data
- Daily OHLCV data for the S&P 500 spanning 2000–2026, sourced from Yahoo Finance.

Methodology
1. Data Engineering
- Cleaning and type normalization
- Log-return transformation
- Volatility feature construction
- Stationarity verification via ADF test

2. Regime Discovery
- Gaussian Hidden Markov Model
- BIC-based state selection (optimal: 5 regimes)
- Multi-seed optimization for stability
- Economic interpretation via drawdown, volatility, and persistence analysis

3. Forecasting Framework
- Baseline: walk-forward ARIMA (1,0,1)
- Regime-aware: conditional return expectation by inferred market state
- Out-of-sample evaluation with realistic walk-forward testing

Results
Model              MSE	    Direction Accuracy
ARIMA	        ~0.000158	     ~49.8%
Regime-Aware	~0.000149	     ~53.6%

Key Insight:
- Incorporating latent regime information produces a statistically meaningful improvement in both forecast error and directional accuracy over classical models.

Regime Characteristics
The discovered regimes exhibit:
- strong persistence
- realistic transition behavior
- economically interpretable drawdown profiles
- volatility alignment with historical crisis events
These properties confirm the model captures genuine market structure rather than noise.

