# Algorithmic Trading MADC
A Portfolio repo to showcase implementation and back testing of quantitative strategies.

### Design
New Folder structure
```
.
├── DataGathering
│   └── data_fetcher.py
├── Strategies
│   ├── market_making_strategy.py
│   └── strategy_base.py
├── Backtesting
│   └── backtester.py
├── Visualization
│   └── visualizer.py
├── Execution (C++)
│   ├── ExecutionEngine.cpp
│   └── ExecutionEngine.h
├── Main
│   └── main.py
└── requirements.txt
```
Databases to be used for storing data. Preferably PostgreSQL.

<!--### Resourses
 1. [Link](https://medium.com/codex/algorithmic-trading-with-macd-in-python-1c2769a6ad1b) to Blog article for implementing the MADC algorithm based on exponential averages.-->


### To-Do list
- [x] MADC implementing with Backtesting on the same data.
- [ ] understand what does the `span` attribute means in `pd.ewm()`.
- [ ] Use a optimizer to find the optimal `fast` and `slow` periods. The cost is the percentage of profit.
- [ ] Some way to get an email when its time to buy or sell.
- [ ] Figure out a way to hide database credentials(Env variables?).


When the fast average is more than the slow average, then it means that the price has moved up significantly in the near term so its time to sell. Where as if the fast average is lagging behind the slow average then it means in the last few days or weeks the price has dropped significantly hence its a good time to buy.


