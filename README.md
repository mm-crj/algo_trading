# Algorithmic Trading
A Portfolio module to showcase implementation and back testing of quantitative strategies.

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
#### work flow
The main function calls the data fetcher module and stores the data in a
`PostgreSQL` database. Then the strategies folder will come into play. The idea
is that the user will be able to choose a particular strategy and time frame and find the optimal parameters for this strategy. The first strategy to implement is the market making strategy. But I am not sure this can be implemented using only the open, low, high, close and volume data. May be trade level data with spread is needed. Then we can try the Moving Average Convergence Divergence strategy.

<!--### Resources
 1. [Link](https://medium.com/codex/algorithmic-trading-with-macd-in-python-1c2769a6ad1b) to Blog article for implementing the MADC algorithm based on exponential averages.-->


### To-Do list
- [x] Figure out a way to secure database credentials(ini files).
- [x] Fetch and conform data
- [x] Store data in `PostgreSQL` database
- [ ] Read stored data in `Pandas` dataframe.
- [x] MADC implementing with Backtesting on the same data.
- [ ] understand what does the `span` attribute means in `pd.ewm()`.
- [ ] Use a optimizer to find the optimal `fast` and `slow` periods. The cost is the percentage of profit.
- [ ] Some way to get an email when its time to buy or sell.


When the fast average is more than the slow average, then it means that the price has moved up significantly in the near term so its time to sell. Where as if the fast average is lagging behind the slow average then it means in the last few days or weeks the price has dropped significantly hence its a good time to buy.


