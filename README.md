# Algorithmic Trading MADC
A repo to alorithmically trading US stocks
### Resourses
 1. [Link](https://medium.com/codex/algorithmic-trading-with-macd-in-python-1c2769a6ad1b) to Blog article for implementing the MADC algorithm based on exponential averages.
 

### To-Do list 
- [x] MADC implementing with Backtesting on the same data. 
- [ ] understand what does the `span` attribute means in `pd.ewm()`.
- [ ] Use a optimizer to find the optimal `fast` and `slow` periods. The cost is the percentage of profit.  
- [ ] Some way to get an email when its time to buy or sell.(nehi pata kaise hoga, bus ho jana chaiye ;D)
 

When the fast average is more than the slow average, then it means that the price has moved up signigicanlty in the near term so its time to sell. Where as if the fast average is lagging behind the slow average then it means in the last few days or weeks the price has dropped signigicanlty hence its a good time to buy.
