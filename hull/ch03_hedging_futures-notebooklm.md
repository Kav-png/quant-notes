# Hedging Flashcards

## Card 1

**Q:** Term: Short Hedge

**A:** Definition: A hedging strategy involving a short position in futures contracts, used when the hedger already owns an asset or expects to own and sell it in the future. Example: A US exporter who expects to receive euros in three months and shorts euro futures to lock in the exchange rate.

---

## Card 2

**Q:** Term: Long Hedge

**A:** Definition: A hedging strategy involving a long position in futures contracts, used when a company knows it must purchase a certain asset in the future and wants to lock in the price now. Example: A copper fabricator taking a long position in copper futures to fix the cost of raw materials needed in four months.

---

## Card 3

**Q:** Term: Perfect Hedge

**A:** Definition: A hedge that completely eliminates the risk associated with a price movement in an underlying variable. Example: A futures contract that exactly matches the maturity, quantity, and specific asset of the exposure, resulting in zero net gain or loss.

---

## Card 4

**Q:** Why is a study of hedging strategies largely a study of 'imperfect' hedges?

**A:** Perfect hedges are rare in practice, requiring strategies that perform as close to perfect as possible to minimise residual risk.

---

## Card 5

**Q:** What is a 'hedge-and-forget' strategy?

**A:** A strategy where a hedger takes a futures position at the start of the life of the hedge and holds it without adjustment until the end of the hedge.

---

## Card 6

**Q:** How does a company determine whether a short or long hedge is appropriate for a commodity?

**A:** A short position is taken to offset a gain from a price increase, while a long position is taken to offset a loss from a price increase.

---

## Card 7

**Q:** Under what condition is a short hedge appropriate for an asset not yet owned?

**A:** It is appropriate if the hedger knows they will receive the asset at a specific time in the future, such as an exporter receiving foreign currency.

---

## Card 8

**Q:** Why might a company choose to focus on its main business activities rather than predicting commodity prices?

**A:** Companies generally lack expertise in predicting financial variables like interest rates or commodity prices, so hedging allows them to focus on their core skills.

---

## Card 9

**Q:** What is the primary argument against companies hedging on behalf of shareholders?

**A:** Shareholders can diversify their own portfolios, making the hedging of specific corporate risks unnecessary if the company acts in the interest of well-diversified investors.

---

## Card 10

**Q:** Pitfall: Why might hedging be more expensive for individual shareholders than for a corporation?

**A:** Corporations benefit from lower transaction costs and commissions per dollar of hedging due to the large size of their transactions compared to individuals.

---

## Card 11

**Q:** Pitfall: How can hedging negatively affect a company if its competitors do not hedge?

**A:** If industry prices fluctuate to reflect raw material costs, a hedged company faces fluctuating profit margins while unhedged competitors maintain constant margins.

---

## Card 12

**Q:** Pitfall: What is the 'treasurer's dilemma' regarding hedging outcomes?

**A:** If the spot price moves in the company's favour, the treasurer may face criticism for the losses on the futures position, despite the overall risk reduction.

---

## Card 13

**Q:** Term: Basis

**A:** Definition: The difference between the spot price of the asset being hedged and the futures price of the contract used. Example: If the spot price is $2.50 and the futures price is $2.20, the basis is $0.30.

---

## Card 14

**Q:** Formula for the Basis

**A:** $Basis = Spot\ price\ of\ asset\ to\ be\ hedged - Futures\ price\ of\ contract\ used$

---

## Card 15

**Q:** What occurs during a 'strengthening' of the basis?

**A:** The basis increases, which happens when the spot price increases by more than the futures price or decreases by less than the futures price.

---

## Card 16

**Q:** What occurs during a 'weakening' of the basis?

**A:** The basis decreases, which happens when the futures price increases by more than the spot price or decreases by less than the spot price.

---

## Card 17

**Q:** Formula for the effective price obtained in a short hedge

**A:** $S_2 + F_1 - F_2$ or $F_1 + b_2$, where $S_2$ is the final spot price, $F_1$ is the initial futures price, $F_2$ is the final futures price, and $b_2$ is the final basis.

---

## Card 18

**Q:** Formula for the effective price paid in a long hedge

**A:** $S_2 + F_1 - F_2$ or $F_1 + b_2$, where $S_2$ is the final spot price, $F_1$ is the initial futures price, $F_2$ is the final futures price, and $b_2$ is the final basis.

---

## Card 19

**Q:** How does an unexpected strengthening of the basis affect a short hedger?

**A:** The hedger's position improves because the effective price received for the asset increases.

---

## Card 20

**Q:** How does an unexpected weakening of the basis affect a long hedger?

**A:** The hedger's position improves because the effective price paid for the asset decreases.

---

## Card 21

**Q:** Term: Cross Hedging

**A:** Definition: A hedging strategy used when the asset underlying the futures contract is different from the asset whose price is being hedged. Example: An airline using heating oil futures to hedge its exposure to jet fuel price volatility.

---

## Card 22

**Q:** Term: Hedge Ratio

**A:** Definition: The ratio of the size of the position taken in futures contracts to the size of the total exposure. Example: A hedge ratio of 1.0 means the futures position size exactly matches the exposure size.

---

## Card 23

**Q:** Formula for the Minimum Variance Hedge Ratio

**A:** $h^* = \rho \frac{\sigma_S}{\sigma_F}$ where $\rho$ is the correlation between $\Delta S$ and $\Delta F$, $\sigma_S$ is the standard deviation of $\Delta S$, and $\sigma_F$ is the standard deviation of $\Delta F$.

---

## Card 24

**Q:** What is the key insight behind the Minimum Variance Hedge Ratio derivation?

**A:** It is the slope of the best-fit line from a linear regression of changes in the spot price ($\Delta S$) against changes in the futures price ($\Delta F$).

---

## Card 25

**Q:** How is hedge effectiveness measured in cross hedging?

**A:** Hedge effectiveness is the proportion of the variance eliminated, equal to the $R^2$ from the regression of $\Delta S$ against $\Delta F$, which is $\rho^2$.

---

## Card 26

**Q:** Formula for the optimal number of futures contracts (without tailing)

**A:** $N^* = \frac{h^* Q_A}{Q_F}$ where $h^*$ is the hedge ratio, $Q_A$ is the size of the position being hedged, and $Q_F$ is the size of one futures contract.

---

## Card 27

**Q:** Term: Tailing the Hedge

**A:** Definition: An adjustment made to the number of futures contracts in a hedge to account for the impact of daily settlement. Example: Reducing the number of contracts slightly when the spot price is lower than the futures price.

---

## Card 28

**Q:** Formula for the optimal number of contracts with tailing

**A:** $N^* = h^* \frac{V_A}{V_F}$ where $V_A$ is the dollar value of the position being hedged and $V_F$ is the dollar value of one futures contract (futures price times contract size).

---

## Card 29

**Q:** Why should a delivery month later than the hedge expiration usually be chosen?

**A:** Futures prices can be erratic during the delivery month, and long hedgers avoid the risk and cost of having to take physical delivery.

---

## Card 30

**Q:** How is the basis risk affected by the time difference between hedge expiration and the delivery month?

**A:** Basis risk generally increases as the time difference between the hedge expiration and the delivery month increases.

---

## Card 31

**Q:** Term: Stock Index

**A:** Definition: A measure that tracks changes in the value of a hypothetical portfolio of stocks, often used to manage equity price exposure. Example: The S&P 500 Index, which reflects the market capitalisation of 500 large publicly held US companies.

---

## Card 32

**Q:** Formula for the number of contracts to hedge a well-diversified equity portfolio

**A:** $N^* = \beta \frac{V_A}{V_F}$ where $\beta$ is the beta of the portfolio, $V_A$ is its current value, and $V_F$ is the current value of one futures contract.

---

## Card 33

**Q:** How is the stock index hedge formula derived in relation to cross hedging?

**A:** The formula treats the optimal hedge ratio $h^*$ as equivalent to the portfolio beta $\beta$, representing the slope of the regression of portfolio returns against index returns.

---

## Card 34

**Q:** What is the expected return of a perfectly hedged equity portfolio?

**A:** The portfolio is expected to grow at the risk-free interest rate, regardless of the performance of the stock market.

---

## Card 35

**Q:** Why might a manager use index futures instead of selling a portfolio to reduce risk?

**A:** Hedging protects against short-term market uncertainty while avoiding the high transaction costs associated with selling and later repurchasing the portfolio.

---

## Card 36

**Q:** Formula to change a portfolio beta from $\beta$ to $\beta^*$ where $\beta > \beta^*$

**A:** $Short\ Position = (\beta - \beta^*) \frac{V_A}{V_F}$ where $V_A$ is the portfolio value and $V_F$ is the value of one futures contract.

---

## Card 37

**Q:** Formula to change a portfolio beta from $\beta$ to $\beta^*$ where $\beta < \beta^*$

**A:** $Long\ Position = (\beta^* - \beta) \frac{V_A}{V_F}$ where $V_A$ is the portfolio value and $V_F$ is the value of one futures contract.

---

## Card 38

**Q:** What is the objective of 'locking in the benefits of stock picking' using futures?

**A:** To remove the risk of general market movements via a short index futures position, leaving the investor exposed only to the performance of specific stocks relative to the market.

---

## Card 39

**Q:** Term: Stack and Roll

**A:** Definition: A strategy used when a hedge's expiration exceeds the available futures maturities, involving rolling a 'stack' of short-term contracts forward into later months. Example: A company rolling over three-month heating oil futures repeatedly to hedge a five-year supply contract.

---

## Card 40

**Q:** Pitfall: What liquidity risk was highlighted by the Metallgesellschaft (MG) case?

**A:** The mismatch in timing between immediate cash outflows from margin calls on short-term futures and the distant cash inflows from long-term supply contracts.

---

## Card 41

**Q:** Under what condition does the basis become zero?

**A:** The basis should be zero at the expiration of the futures contract if the asset being hedged is identical to the asset underlying the contract.

---

## Card 42

**Q:** How does daily settlement differentiate futures from forward contracts in hedging?

**A:** Futures require 'tailing' to account for the fact that the payoff is realised day-by-day rather than as a single lump sum at the end of the hedge.

---

## Card 43

**Q:** Process: What are the two main components of the basis in a cross-hedging scenario?

**A:** The basis between the underlying asset and the futures contract, and the basis arising from the difference between the actual asset and the underlying asset.

---

## Card 44

**Q:** Why is liquidity a factor when choosing a delivery month for a hedge?

**A:** Hedgers often prefer short-maturity contracts because they typically have the greatest liquidity, even if it requires rolling the hedge forward.

---

## Card 45

**Q:** The standard definition of the basis is $Spot - Futures$; what is the common alternative definition for financial assets?

**A:** $Futures\ price - Spot\ price$

---

## Card 46

**Q:** Under what condition is the optimal hedge ratio $h^*$ equal to 1.0?

**A:** When the changes in the spot price perfectly mirror the changes in the futures price, meaning $\rho = 1$ and $\sigma_S = \sigma_F$.

---

## Card 47

**Q:** In a stack and roll strategy, what action is taken when a futures contract is near expiration?

**A:** The existing futures contract is closed out, and a new position is taken in a futures contract with a later delivery date.

---

## Card 48

**Q:** How does the CAPM define systematic risk?

**A:** Systematic risk is the risk related to the return of the market as a whole that cannot be diversified away.

---

## Card 49

**Q:** Formula for Expected Return using CAPM

**A:** $R_F + \beta(R_M - R_F)$ where $R_F$ is the risk-free rate, $R_M$ is the market return, and $\beta$ is the systematic risk parameter.

---

## Card 50

**Q:** What is 'nonsystematic risk' in the context of equity portfolios?

**A:** Risk that is unique to an individual asset and can be eliminated by holding a large, well-diversified portfolio.

---

## Card 51

**Q:** Why might a company deliberately leave many risks unhedged in practice?

**A:** Potential reasons include competitive pressures, fear of executive criticism if the hedge loses money, or the belief that shareholders can diversify risk themselves.

---

## Card 52

**Q:** What happens to the basis of gold according to May 2010 market data?

**A:** The basis was negative, meaning the futures price was higher than the spot price.

---

## Card 53

**Q:** Term: Hedge-and-Forget

**A:** Definition: A passive hedging strategy where a position is opened at the start of the risk exposure and closed only at the end. Example: A farmer selling corn futures in the spring and closing the position only when the crop is harvested in the autumn.

---

## Card 54

**Q:** What are the three primary reasons for basis risk in practice?

**A:** Mismatch between the asset being hedged and the underlying asset, uncertainty regarding the transaction date, and the need to close the hedge before the delivery month.

---

## Card 55

**Q:** How do price-weighted indices like the DJIA differ from value-weighted indices like the S&P 500?

**A:** Price-weighted indices assign weights based on share price, whereas value-weighted indices assign weights proportional to market capitalisation.

---

## Card 56

**Q:** How is 'hedge effectiveness' defined in the context of regression analysis?

**A:** It is the proportion of the variance in the spot price change that is eliminated by the hedge, represented by the $R^2$ value.

---
