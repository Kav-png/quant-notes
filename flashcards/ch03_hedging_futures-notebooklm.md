# Hedging Flashcards

## Card 1

**Q:** Term: Perfect Hedge

**A:** Definition: A hedge that completely eliminates the risk associated with a particular exposure. Example: A producer locking in a price using a forward contract that matches their delivery date and asset exactly.

---

## Card 2

**Q:** Under what general condition is a short futures position appropriate for hedging?

**A:** When the hedger already owns an asset (or expects to own it) and intends to sell it at a future date.

---

## Card 3

**Q:** Term: Short Hedge

**A:** Definition: A hedging strategy involving a short position in futures contracts to offset the risk of price declines in an asset owned or to be received. Example: A US exporter who expects to receive euros in three months selling euro futures.

---

## Card 4

**Q:** Under what general condition is a long futures position appropriate for hedging?

**A:** When a company knows it will have to purchase a certain asset in the future and wants to lock in the purchase price.

---

## Card 5

**Q:** Term: Long Hedge

**A:** Definition: A strategy involving a long position in futures to protect against potential price increases of an asset the hedger needs to buy later. Example: A copper fabricator locking in the price of raw materials needed in five months.

---

## Card 6

**Q:** Why might a company choose futures over buying an asset immediately in the spot market for future use?

**A:** To avoid the immediate cash outlay, interest costs, and storage costs associated with holding physical inventory.

---

## Card 7

**Q:** What is the primary argument against individual shareholders needing a company to hedge its risks?

**A:** Shareholders can diversify their own portfolios or perform hedging themselves, though they usually face higher transaction costs than corporations.

---

## Card 8

**Q:** Pitfall: How can hedging negatively impact a company if its competitors do not hedge?

**A:** If industry prices fluctuate with raw material costs, a hedged company’s profit margins may fluctuate while unhedged competitors maintain constant margins.

---

## Card 9

**Q:** How does the treasurer’s risk differ from the company’s risk regarding hedging outcomes?

**A:** Hedging reduces company risk, but the treasurer may face professional criticism if the hedge results in a visible loss while the business gain is less obvious.

---

## Card 10

**Q:** Term: Basis

**A:** Definition: The difference between the spot price of an asset to be hedged and the futures price of the contract used. Example: If the spot price is $2.50 and the futures price is $2.20, the basis is $0.30.

---

## Card 11

**Q:** Formula: The Basis (\(b\))

**A:** $b = S - F$, where $S$ is the spot price of the asset to be hedged and $F$ is the futures price of the contract used.

---

## Card 12

**Q:** What defines a 'strengthening' of the basis?

**A:** An increase in the value of the basis over time.

---

## Card 13

**Q:** What defines a 'weakening' of the basis?

**A:** A decrease in the value of the basis over time.

---

## Card 14

**Q:** Formula: Effective price received in a short hedge using the basis

**A:** $P_{eff} = F_1 + b_2$, where $F_1$ is the initial futures price and $b_2$ is the basis at the time the position is closed.

---

## Card 15

**Q:** Formula: Effective price paid in a long hedge using the basis

**A:** $P_{eff} = F_1 + b_2$, where $F_1$ is the initial futures price and $b_2$ is the basis at the time the position is closed.

---

## Card 16

**Q:** Term: Cross Hedging

**A:** Definition: Hedging an exposure to the price of one asset by taking a position in futures contracts on a different but related asset. Example: An airline using heating oil futures to hedge its jet fuel price exposure.

---

## Card 17

**Q:** Term: Hedge Ratio

**A:** Definition: The ratio of the size of the position taken in futures contracts to the size of the total exposure. Example: Using 1,000 barrels of oil futures to hedge an exposure of 1,000 barrels gives a ratio of 1.0.

---

## Card 18

**Q:** Formula: Minimum Variance Hedge Ratio (\(h^*\))

**A:** $h^* = \rho \frac{\sigma_S}{\sigma_F}$, where $\rho$ is the correlation coefficient, $\sigma_S$ is the standard deviation of change in spot price, and $\sigma_F$ is the standard deviation of change in futures price.

---

## Card 19

**Q:** How is the 'hedge effectiveness' of a minimum variance hedge measured?

**A:** It is the proportion of the variance eliminated, calculated as the $R^2$ (or $\rho^2$) from the regression of change in spot against change in futures.

---

## Card 20

**Q:** Formula: Optimal number of contracts (\(N^*\)) without tailing

**A:** $N^* = \frac{h^* Q_A}{Q_F}$, where $h^*$ is the hedge ratio, $Q_A$ is the size of the position being hedged, and $Q_F$ is the size of one futures contract.

---

## Card 21

**Q:** Term: Tailing the Hedge

**A:** Definition: A small adjustment to the number of futures contracts to account for the impact of daily settlement. Example: Reducing the number of contracts slightly when futures prices are higher than spot prices.

---

## Card 22

**Q:** Formula: Optimal number of contracts (\(N^*\)) with tailing

**A:** $N^* = h^* \frac{V_A}{V_F}$, where $V_A$ is the dollar value of the position being hedged and $V_F$ is the dollar value of one futures contract.

---

## Card 23

**Q:** Why is a delivery month later than the hedge expiration typically chosen?

**A:** To avoid the erratic price fluctuations often seen during the delivery month and the risk of being forced to take/make physical delivery.

---

## Card 24

**Q:** What does a stock index track?

**A:** Changes in the value of a hypothetical portfolio of stocks, typically excluding dividends.

---

## Card 25

**Q:** Formula: Number of stock index futures contracts to hedge a portfolio

**A:** $N^* = \beta \frac{V_A}{V_F}$, where $\beta$ is the portfolio beta, $V_A$ is the current portfolio value, and $V_F$ is the current value of one futures contract.

---

## Card 26

**Q:** What is the key insight behind using index futures to hedge a well-diversified portfolio?

**A:** It allows the investor to earn the risk-free rate on the total position, effectively making the expected return independent of market performance.

---

## Card 27

**Q:** Formula: Contracts required to change portfolio beta from \(\beta\) to \(\beta^*\) (where \(\beta > \beta^*\))

**A:** $N^* = (\beta - \beta^*) \frac{V_A}{V_F}$ short contracts, where $V_A$ is the portfolio value and $V_F$ is the value of one futures contract.

---

## Card 28

**Q:** Formula: Contracts required to increase portfolio beta from \(\beta\) to \(\beta^*\) (where \(\beta < \beta^*\))

**A:** $N^* = (\beta^* - \beta) \frac{V_A}{V_F}$ long contracts, where $V_A$ is the portfolio value and $V_F$ is the value of one futures contract.

---

## Card 29

**Q:** How can index futures be used to 'lock in the benefits of stock picking'?

**A:** By shorting index futures equivalent to the portfolio's beta, the investor removes market risk and remains exposed only to the specific stocks' performance relative to the market.

---

## Card 30

**Q:** Term: Stack and Roll

**A:** Definition: A strategy of rolling a hedge forward by closing out near-term futures and entering new contracts with later delivery dates to cover long-term risk. Example: Hedging oil sales for 2025 using a series of 3-month futures contracts.

---

## Card 31

**Q:** Pitfall: What is the primary risk associated with the 'stack and roll' strategy?

**A:** Liquidity risk, as gains/losses on futures occur daily while gains/losses on the underlying long-term exposure may not be realised for years.

---

## Card 32

**Q:** How is the minimum variance hedge ratio (\(h^*\)) derived?

**A:** It is derived by finding the slope of the best-fit line from a linear regression of historical changes in spot prices (\(\Delta S\)) against historical changes in futures prices (\(\Delta F\)).

---

## Card 33

**Q:** How is the beta (\(\beta\)) of a stock portfolio defined in the context of CAPM?

**A:** The slope of the best-fit line obtained when regressing the excess return of the portfolio over the risk-free rate against the excess return of the market index.

---

## Card 34

**Q:** What happens to the basis of a futures contract as it approaches its delivery date?

**A:** If the asset being hedged is the same as the underlying asset, the basis must converge to zero at the expiration of the contract.

---

## Card 35

**Q:** Why might a company hedge even if it results in a lower profit than no hedging?

**A:** The goal of hedging is to reduce risk and lock in a certain price, not necessarily to maximise profit from price movements.

---

## Card 36

**Q:** Pitfall: What hidden assumption is made when calculating \(h^*\) from historical data?

**A:** It assumes that the correlation and volatilities observed in the past will remain representative of the relationship during the life of the hedge.

---

## Card 37

**Q:** In Example 3.1, why was the effective price ($0.7750) different from the initial spot price ($0.80)?

**A:** The hedge locks in a price close to the initial futures price ($0.78), adjusted for the final basis.

---

## Card 38

**Q:** What is the difference between Hull and Wilmott's focus on hedging?

**A:** Hull focuses on market practices and empirical risk reduction (e.g. basis risk, index hedging), while Wilmott typically focuses on the mathematical derivation of delta-neutrality in continuous time.

---

## Card 39

**Q:** An oil producer shorts 1,000 futures at $79. If oil drops to $75 at maturity, what is the producer's total revenue per barrel including the hedge?

**A:** Approximately $79 per barrel ($75 from the sale + $4 gain on the short futures).

---

## Card 40

**Q:** If a copper fabricator requires 100,000 lbs of copper and one contract is 25,000 lbs, how many contracts are needed for a hedge ratio of 1.0?

**A:** 4 contracts.

---

## Card 41

**Q:** What is 'basis risk'?

**A:** The risk that the basis will change in an unpredictable way between the time the hedge is initiated and the time it is closed out.

---

## Card 42

**Q:** Under what condition does \(h^* = 1.0\)?

**A:** When the correlation coefficient \(\rho\) is 1.0 and the standard deviations of the changes in spot and futures prices are equal.

---

## Card 43

**Q:** How does tailing a hedge modify the number of contracts?

**A:** It multiplies the standard hedge ratio by the ratio of the spot price to the futures price to account for the interest earned on margin cash flows.

---

## Card 44

**Q:** What is the formula for the dollar value of one futures contract (\(V_F\))?

**A:** $V_F = F \times Q_F$, where $F$ is the current futures price and $Q_F$ is the contract size.

---

## Card 45

**Q:** In stock index hedging, what does \(\beta = 2.0\) imply about the number of contracts needed compared to \(\beta = 1.0\)?

**A:** Twice as many contracts are required because the portfolio is twice as sensitive to market movements.

---

## Card 46

**Q:** Why is a 'hedge-and-forget' strategy generally assumed in Chapter 3?

**A:** To simplify the initial study of hedging principles before examining dynamic strategies that require frequent adjustments in later chapters.

---

## Card 47

**Q:** What is a 'cross hedge ratio'?

**A:** The optimal ratio of futures to exposure when the underlying asset of the futures contract differs from the asset being hedged.

---

## Card 48

**Q:** How can the stack and roll strategy lead to a disaster like Metallgesellschaft?

**A:** Falling prices caused massive margin calls on long futures, creating a liquidity crisis despite potentially offsetting long-term contract gains.

---

## Card 49

**Q:** In CAPM, what does 'nonsystematic risk' refer to?

**A:** Risk that is unique to an individual asset and can be eliminated through diversification.

---

## Card 50

**Q:** Formula: Expected return on an asset (CAPM)

**A:** $E[R] = R_F + \beta (R_M - R_F)$, where $R_F$ is the risk-free rate and $R_M$ is the return on the market.

---
