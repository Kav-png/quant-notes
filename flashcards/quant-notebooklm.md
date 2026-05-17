# Finance Flashcards

## Card 1

**Q:** Term: Equity

**A:** Definition: A financial instrument representing an ownership interest in a company, typically in the form of shares of stock. Example: Owning 100 ordinary shares of Microsoft Corp.

---

## Card 2

**Q:** Term: Stock Split

**A:** Definition: A corporate action that increases the number of shares outstanding while reducing the share price proportionally, keeping total market capitalisation constant. Example: In a 'two-for-one' split, a shareholder receives two shares for every one held, and the share price is halved.

---

## Card 3

**Q:** Term: Commodity

**A:** Definition: Raw products such as precious metals, energy resources, or agricultural goods that are traded on markets. Example: Speculating on the price direction of crude oil without intending to take physical delivery.

---

## Card 4

**Q:** Term: Forward Contract

**A:** Definition: A private, non-standardised agreement between two parties to buy or sell an underlying asset at a specified future date for a price agreed today. Example: A bank entering an agreement with a client to exchange US Dollars for British Pounds in three months at a fixed rate.

---

## Card 5

**Q:** Term: Futures Contract

**A:** Definition: A standardised, exchange-traded agreement to buy or sell an asset at a predetermined price on a future date, settled daily via a clearing house. Example: Buying a gold futures contract on the COMEX exchange for 100 ounces of gold.

---

## Card 6

**Q:** Term: No-Arbitrage Principle

**A:** Definition: The fundamental financial theory that in an efficient market, it is impossible to make a risk-free profit for zero initial investment. Example: If a forward price is too high, an investor borrows money to buy the asset and sells it forward to lock in a riskless profit.

---

## Card 7

**Q:** Term: Arithmetic Random Walk

**A:** Definition: A model where the change in an asset's price is determined by adding a fixed random amount at each time step, leading to a Normal distribution. Example: Simulating a stock price by adding either $+1$ or $-1$ based on a coin toss.

---

## Card 8

**Q:** Term: Geometric Random Walk

**A:** Definition: A model where the asset price is multiplied by a random factor at each step, ensuring the price remains positive and yielding a lognormal distribution. Example: Modelling an asset where it rises by $1\%$ or falls by $1\%$ of its current value every day.

---

## Card 9

**Q:** Formula: No-Arbitrage Forward Price (Investment Asset)

**A:** $F = S e^{r(T-t)}$, where $F$ is the forward price, $S$ is the spot price, $r$ is the risk-free rate, and $T-t$ is the time to maturity. (Hull notes this applies to assets held for investment by a significant number of investors).

---

## Card 10

**Q:** Formula: Value of a long forward contract during its life

**A:** $f = S - K e^{-r(T-t)}$, where $f$ is the contract value, $S$ is the current spot price, $K$ is the delivery price, and $r$ is the risk-free rate. (Wilmott emphasises that $f$ is initially zero).

---

## Card 11

**Q:** How is the 'No Arbitrage' relationship between spot and forward prices derived?

**A:** The key insight is the construction of a hedged portfolio that replicates the forward contract's payoff by borrowing at the risk-free rate to buy the spot asset.

---

## Card 12

**Q:** What is the critical insight behind using a 'multiplicative rule' in asset price modelling?

**A:** It ensures that the magnitude of price changes is proportional to the asset's current level and prevents the asset price from ever becoming negative.

---

## Card 13

**Q:** What determines the 'delivery price' at the initiation of a forward contract?

**A:** It is set at a level that makes the initial value of the forward contract exactly zero for both parties.

---

## Card 14

**Q:** How does the 'marking to market' process in futures differ from forward contracts?

**A:** In futures, profits and losses are realised and paid daily, whereas in forwards, the entire gain or loss is only realised at maturity.

---

## Card 15

**Q:** Why do commodities often show seasonal effects in their price behaviour?

**A:** Prices are influenced by periodic supply and demand cycles, such as harvest times for crops or heating requirements for energy in winter.

---

## Card 16

**Q:** Under the no-arbitrage principle, how does the forward price relate to the expected future direction of the asset?

**A:** The forward price in no way depends on whether the asset is expected to increase or decrease in value; it is solely a function of the spot price and interest rates.

---

## Card 17

**Q:** Pitfall: Assuming an arithmetic random walk is suitable for long-term equity modelling.

**A:** The arithmetic model allows the asset price to become negative, which violates the principle of limited liability in shares.

---

## Card 18

**Q:** Pitfall: Ignoring transaction costs in no-arbitrage calculations.

**A:** In reality, bid-offer spreads and commissions create 'arbitrage bounds' where small price discrepancies cannot be profitably exploited.

---

## Card 19

**Q:** Pitfall: Assuming forward and futures prices are always identical.

**A:** They are only identical if interest rates are known in advance; if rates are stochastic, the daily settlement of futures can cause them to diverge from forwards.

---

## Card 20

**Q:** What is the primary difference between hedging and speculation?

**A:** Hedging is the avoidance of existing risk by locking in prices, while speculation is the intentional taking of risk to profit from market views.

---

## Card 21

**Q:** Why is 'standardisation' a defining feature of futures markets compared to forward markets?

**A:** Standardisation of contract size and delivery grades allows for high liquidity and ease of trading on public exchanges.

---

## Card 22

**Q:** In a geometric random walk, what happens to the magnitude of price changes as the asset price increases?

**A:** The magnitude of the changes increases because the random movement is proportional to the current level of the asset.

---

## Card 23

**Q:** How does a 'two-for-one' stock split affect the value of a single share?

**A:** The price of the share is reduced by half, though the total value of the investor's holding remains unchanged.

---

## Card 24

**Q:** What is the definition of the 'spot price' of an asset?

**A:** The price at which an asset can be bought or sold for immediate delivery. Example: The current price of gold displayed on a dealer's screen for an instant trade.

---

## Card 25

**Q:** What is the value of a futures contract at any time during its life, and why?

**A:** The value is always zero because the daily settlement process (marking to market) effectively resets the contract each day.

---

## Card 26

**Q:** If the forward price $F$ is greater than $S e^{r(T-t)}$, what riskless strategy should an arbitrageur employ?

**A:** The arbitrageur should sell the forward contract, borrow $S$ to buy the asset, and hold it until maturity to capture the excess.

---

## Card 27

**Q:** If the forward price $F$ is less than $S e^{r(T-t)}$, what riskless strategy should an arbitrageur employ?

**A:** The arbitrageur should buy the forward contract and 'short' the asset today, investing the proceeds at the risk-free rate until maturity.

---

## Card 28

**Q:** How does Wilmott define the 'time value of money'?

**A:** It is the simple technical issue that money held today can earn interest, making it worth more than the same nominal amount in the future.

---

## Card 29

**Q:** In the context of the binomial model, what does the variable $p$ represent?

**A:** The probability of the asset price rising in the next time step. (Wilmott notes this can be any value, not just $0.5$).

---

## Card 30

**Q:** What happens to the price distribution in an arithmetic random walk if $p < 0.5$?

**A:** The distribution of future prices will drift downwards over time.

---

## Card 31

**Q:** How does scarcity typically affect commodity prices?

**A:** Scarcity reduces supply relative to demand, which leads to higher market prices for the commodity.

---

## Card 32

**Q:** Term: Dividend

**A:** Definition: A portion of a company's earnings distributed to shareholders, which typically causes the share price to drop on the ex-dividend date. Example: A company paying $£0.50$ per share to its investors every quarter.

---

## Card 33

**Q:** What is the role of a clearing house in futures trading?

**A:** It acts as the intermediary for every trade, ensuring that daily settlement is performed and reducing counterparty default risk. (Hull highlights this as a key exchange mechanism).

---

## Card 34

**Q:** How does Wilmott's 'multiplicative rule' lead to a lognormal random walk?

**A:** By multiplying the price by a factor at each step, the log of the price follows an additive (Normal) walk, meaning the price itself is lognormally distributed.

---

## Card 35

**Q:** Why is the forward price $F$ quoted in newspapers actually a 'delivery price'?

**A:** It represents the price currently being agreed upon for new contracts to ensure they have an initial value of zero.

---

## Card 36

**Q:** Formula: Continuously Compounded Interest Growth

**A:** $S(T) = S(t) e^{r(T-t)}$, where $S(T)$ is the future value, $S(t)$ is the present value, $r$ is the interest rate, and $T-t$ is the time period.

---

## Card 37

**Q:** What is 'basis risk' in the context of hedging with futures?

**A:** The risk that the futures price will not move perfectly in line with the spot price of the asset being hedged. (Hull notes this as a common real-world complication).

---

## Card 38

**Q:** Term: Short Position

**A:** Definition: A market position where an investor agrees to sell an asset they do not necessarily own, profiting if the price falls. Example: Entering a forward contract to sell 1,000 barrels of oil at a fixed price.

---

## Card 39

**Q:** Term: Long Position

**A:** Definition: A market position where an investor agrees to buy an asset, profiting if the price rises. Example: Buying a futures contract for 100 ounces of gold.

---

## Card 40

**Q:** What happens to a forward contract's value as it approaches maturity if the spot price $S$ rises above the delivery price $K$?

**A:** The value of the long forward contract increases, eventually equaling $S - K$ at the moment of maturity.

---

## Card 41

**Q:** What is a 'Financial Index'?

**A:** A portfolio of assets, such as stocks, whose collective price performance is tracked as a single value. Example: The S&P 500 or the FTSE 100.

---

## Card 42

**Q:** How do speculators benefit from the high liquidity of futures markets?

**A:** They can easily 'close out' their positions before delivery by entering into an opposite trade, allowing them to profit from price moves without handling the physical asset.

---

## Card 43

**Q:** In currency markets, what is the 'forward exchange rate'?

**A:** The exchange rate agreed upon today for the delivery of a currency at a specified future date. Example: A 6-month GBP/USD forward rate of $1.4422$.

---

## Card 44

**Q:** Why does Wilmott consider the first chapter a 'gentle introduction'?

**A:** It focuses on definitions and market specifications with very little technical material, using 'time value of money' as the only simple mathematical concept.

---

## Card 45

**Q:** What is the 'maturity' or 'delivery date' of a contract?

**A:** The specific future date on which the underlying asset must be delivered and the delivery price must be paid.

---

## Card 46

**Q:** According to the no-arbitrage example provided by Wilmott, if $S=28.75$, $r=4.92\%$, and $T-t=1$, what is the consistent forward price?

**A:** $F = 28.75 e^{0.0492 \times 1} \approx 30.20$.

---

## Card 47

**Q:** How does the 'cheapest-to-deliver' feature in some bond futures affect the short position holder?

**A:** The holder of the short position has the right to choose which bond from a range of eligible bonds to deliver, naturally selecting the one with the lowest cost.

---

## Card 48

**Q:** What is the 'multiplicative rule' for simulating asset prices in Excel?

**A:** The next price is calculated by multiplying the current price by a factor (e.g., $1.01$ or $0.99$) based on a random number generator.

---

## Card 49

**Q:** How does a 'long forward' contract eliminate exchange rate risk for an American resident expecting to be paid in Yen?

**A:** By entering a contract to sell Yen for Dollars at a fixed rate in the future, the resident locks in their Dollar income regardless of market fluctuations.

---

## Card 50

**Q:** Term: Initial Margin

**A:** Definition: The funds that must be deposited by an investor when entering a futures contract to ensure they can meet potential losses. (Hull describes this as a safeguard for the exchange).

---

## Card 51

**Q:** What is the 'lognormal random walk' an approximation of?

**A:** It is the continuous-time limit of a discrete process using the multiplicative rule for asset price changes.

---

## Card 52

**Q:** Why are forwards and futures considered 'important building blocks' of finance theory?

**A:** They allow for the clear application of the no-arbitrage principle, which is the foundation for valuing more complex derivatives like options.

---
