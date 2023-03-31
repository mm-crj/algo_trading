# algo_trading
A repo to alorithmically trading US stocks
### Resourses
 1. [Link](https://medium.com/codex/algorithmic-trading-with-macd-in-python-1c2769a6ad1b) to Blog article for implementing the MADC algorithm based on exponential averages.
 

### To-Do list 
 1. Find the exponential average of daily mid price of last 12 months. 
 2. And compare against 6 Months exponential avg.
 3. See if in the past, buying when 6 months(fast avg) exceeded 12 months(slow agv) and selling when 6 months was less than 12 months, is actually a good stratagy.  
 4. Some way to get an email when its time to buy or sell.(nehi pata kaise hoga, bus ho jana chaiye ;D)
 

When the fast average is more than the slow average, then it means that the price has moved up signigicanlty in the near term so its time to sell. Where as if the fast average is lagging behind the slow average then it means in the last few days or weeks the price has dropped signigicanlty hence its a good time to buy.
