# Hedging Flashcards

## Card 1

**Q:** Term: Short Hedge

**A:** Definition: A hedging strategy that involves taking a short position in a futures contract. Example: A copper producer selling copper futures to protect against a potential decline in prices before their inventory is ready for sale.

---

## Card 2

**Q:** Term: Long Hedge

**A:** Definition: A hedging strategy that involves taking a long position in a futures contract. Example: An airline purchasing heating oil futures to lock in the cost of fuel it knows it must buy in three months.

---

## Card 3

**Q:** Term: Basis

**A:** Definition: The difference between the spot price of the asset being hedged and the futures price of the contract used. Example: If the spot price of gold is $1,800 and the futures price is $1,810, the basis is $-\$10$.

---

## Card 4

**Q:** How does a 'strengthening' of the basis affect a short hedger?

**A:** It improves the hedger's position because the spot price increases more (or decreases less) relative to the futures price.

---

## Card 5

**Q:** How does a 'weakening' of the basis affect a long hedger?

**A:** It improves the hedger's position because the spot price decreases more (or increases less) relative to the futures price.

---

## Card 6

**Q:** Term: Basis Risk

**A:** Definition: The uncertainty regarding the value of the basis at the time a hedge is closed out. Example: A company hedging exposure to jet fuel using heating oil futures, where the price gap between the two commodities fluctuates unexpectedly.

---

## Card 7

**Q:** What occurs to the basis of a futures contract at the moment of expiration if the underlying asset is identical to the hedged asset?

**A:** The basis becomes zero.

---

## Card 8

**Q:** Term: Cross Hedging

**A:** Definition: Hedging a risk using a futures contract on an asset that is different from, but correlated with, the asset being hedged. Example: Using wheat futures to hedge the price of rye.

---

## Card 9

**Q:** Formula: Optimal Hedge Ratio ($h^*$)

**A:** $h^* = \rho \frac{\sigma_S}{\sigma_F}$, where $\rho$ is the correlation coefficient between changes in spot and futures prices, and $\sigma_S$ and $\sigma_F$ are their respective standard deviations.

---

## Card 10

**Q:** What is the key insight behind the derivation of the optimal hedge ratio $h^*$?

**A:** It is the slope of the best-fit regression line of changes in spot prices ($\Delta S$) against changes in futures prices ($\Delta F$).

---

## Card 11

**Q:** Formula: Optimal Number of Contracts ($N^*$)

**A:** $N^* = \frac{h^* Q_A}{Q_F}$, where $h^*$ is the optimal hedge ratio, $Q_A$ is the size of the position being hedged, and $Q_F$ is the size of one futures contract.

---

## Card 12

**Q:** Term: Hedge Effectiveness

**A:** Definition: The proportion of variance in the asset price exposure that is eliminated by the hedge, calculated as the square of the correlation coefficient. Example: A hedge with a correlation of $0.9$ between spot and futures has an effectiveness ($R^2$) of $0.81$.

---

## Card 13

**Q:** Term: Tailing the Hedge

**A:** Definition: An adjustment to the number of futures contracts to account for the impact of daily settlement and interest. Example: Using the current dollar value of the position ($V_A$) and the futures contract ($V_F$) instead of asset quantities to determine $N^*$.

---

## Card 14

**Q:** Formula: Optimal Number of Contracts for a Tailed Hedge ($N^*$)

**A:** $N^* = h^* \frac{V_A}{V_F}$, where $V_A$ is the dollar value of the position, $V_F$ is the dollar value of one futures contract, and $h^*$ is the optimal hedge ratio.

---

## Card 15

**Q:** Term: Stock Index Futures

**A:** Definition: Futures contracts based on a hypothetical portfolio of stocks representing a segment of the market. Example: An investor selling S&P 500 futures to protect a well-diversified equity portfolio from market downturns.

---

## Card 16

**Q:** Formula: Number of Contracts to Hedge an Equity Portfolio ($N^*$)

**A:** $N^* = \beta \frac{V_A}{V_F}$, where $\beta$ is the portfolio beta, $V_A$ is the current value of the portfolio, and $V_F$ is the value of one futures contract.

---

## Card 17

**Q:** How is the optimal number of contracts calculated when the goal is to reduce a portfolio's beta from $\beta$ to $\beta^*$?

**A:** The number of contracts to short is $(\beta - \beta^*) \frac{V_A}{V_F}$.

---

## Card 18

**Q:** Under what condition is the optimal number of contracts for an equity hedge calculated as $(\beta^* - \beta) \frac{V_A}{V_F}$ using a long position?

**A:** When the investor wishes to increase the beta of the portfolio from $\beta$ to a higher level $\beta^*$.

---

## Card 19

**Q:** Term: Stack and Roll

**A:** Definition: A strategy of rolling hedges forward by closing out near-term contracts and entering longer-term ones as they expire. Example: A company with a five-year exposure hedging with one-year futures and replacing them annually.

---

## Card 20

**Q:** Pitfall: What is a major risk associated with 'Stack and Roll' strategies during periods of adverse price movements?

**A:** Liquidity risk, as the hedger may face significant margin calls on the futures position before the gain on the underlying asset is realised.

---

## Card 21

**Q:** Pitfall: Why might a farmer be ill-advised to hedge $100\%$ of their expected crop production with futures?

**A:** Quantity uncertainty; if the crop is wiped out by weather, the farmer is left with a speculative futures position and no asset to offset the loss.

---

## Card 22

**Q:** Pitfall: How does the assumption of 'constant interest rates' affect the equivalence of forward and futures prices in hedging?

**A:** If interest rates are not constant, daily settlement in futures creates a timing difference in cash flows that forwards do not have.

---

## Card 23

**Q:** How does the 'hedge-and-forget' strategy differ from dynamic hedging?

**A:** In hedge-and-forget, the position is set at the start and not adjusted; in dynamic hedging, the position is frequently rebalanced.

---

## Card 24

**Q:** Why does Hull argue that a company should focus on hedging risks arising from its core business rather than external variables like exchange rates?

**A:** It allows the company to focus on its competitive advantages while avoiding 'financial' risks that it has no special expertise in managing.

---

## Card 25

**Q:** Under the Capital Asset Pricing Model (CAPM), what is the primary reason a corporate treasurer might justify hedging?

**A:** To reduce the probability of financial distress and ensure that funds are available for profitable investment opportunities.

---

## Card 26

**Q:** Formula: Effective Price for a Short Hedge

**A:** $F_1 + (S_2 - F_2)$, where $F_1$ is the initial futures price, $S_2$ is the final spot price, and $F_2$ is the final futures price.

---

## Card 27

**Q:** Formula: Effective Price for a Long Hedge

**A:** $F_1 + (S_2 - F_2)$, where $F_1$ is the initial futures price, $S_2$ is the final spot price, and $F_2$ is the final futures price.

---

## Card 28

**Q:** How is the 'Minimum Variance Hedge Ratio' conceptually related to the correlation coefficient $\rho$?

**A:** It is exactly equal to $\rho$ if the standard deviation of spot price changes and futures price changes are equal.

---

## Card 29

**Q:** In the context of equity hedging, what does a portfolio beta ($\beta$) of $1.5$ imply about its sensitivity?

**A:** The portfolio is $50\%$ more sensitive to market movements than the index.

---

## Card 30

**Q:** What is the primary reason that 'perfect' hedges are rare in practice?

**A:** Mismatches in the asset type, the exact date of the transaction, and the contract's delivery month create basis risk.

---

## Card 31

**Q:** If a hedger chooses a hedge ratio $h$ that is NOT the optimal $h^*$, what happens to the variance of the hedged position?

**A:** The variance of the position will be higher than the minimum possible variance.

---

## Card 32

**Q:** What does the 'Beta' in an equity hedge represent that the 'Hedge Ratio' ($h^*$) represents in a commodity hedge?

**A:** Both represent the sensitivity of the asset's price changes to the changes in the futures price used for the hedge.

---

## Card 33

**Q:** Why is it often recommended to choose a futures delivery month that is as close as possible to, but later than, the hedge expiration?

**A:** To minimise basis risk and avoid the complications of physical delivery during the delivery month.

---

## Card 34

**Q:** Term: Systematic Risk

**A:** Definition: The risk that is inherent to the entire market and cannot be diversified away. Example: A sudden increase in national interest rates affecting all stocks in an index.

---

## Card 35

**Q:** Term: Nonsystematic Risk

**A:** Definition: The risk that is unique to a specific company or industry and can be eliminated through diversification. Example: A strike at a specific mining company's facility.

---

## Card 36

**Q:** What is the result of hedging a well-diversified portfolio by shorting index futures to a target beta of zero?

**A:** The portfolio's return becomes approximately equal to the risk-free rate of interest.

---

## Card 37

**Q:** If the correlation $\rho$ between $\Delta S$ and $\Delta F$ is zero, what is the optimal hedge ratio $h^*$?

**A:** $0$, meaning no hedging is effective using that futures contract.

---

## Card 38

**Q:** Why does a short hedger benefit from an 'increase' in the basis ($S_2 - F_2 > S_1 - F_1$)?

**A:** Because the gain on the spot position exceeds the loss on the futures position (or vice versa).

---

## Card 39

**Q:** A company expects to sell $1,000,000$ units of an asset. If the optimal hedge ratio $h^*$ is $0.8$, for what quantity should they enter futures?

**A:** $800,000$ units.

---

## Card 40

**Q:** In cross hedging, how is $\sigma_S$ typically estimated?

**A:** By calculating the standard deviation of historical changes in the spot price over time intervals of the same length as the intended hedge.

---

## Card 41

**Q:** What is the relationship between 'hedge effectiveness' and the R-squared ($R^2$) value of a regression?

**A:** They are identical; both represent the proportion of variance explained by the relationship between the two variables.

---

## Card 42

**Q:** Why is the denominator in the contract number formula ($Q_F$ or $V_F$) important?

**A:** It standardises the hedge into discrete, tradable units defined by the exchange.

---

## Card 43

**Q:** What is the 'effective' exchange rate for a company that hedges a future currency sale with a short forward contract?

**A:** The forward price ($F_1$) agreed upon at the start of the contract.

---

## Card 44

**Q:** Formula: Standard Deviation of the Change in Value of a Hedged Position

**A:** $\sigma_P = \sqrt{\sigma_S^2 + h^2 \sigma_F^2 - 2h \rho \sigma_S \sigma_F}$, where $h$ is the hedge ratio.

---

## Card 45

**Q:** If the futures price is $F_1 = 2.20$ and $F_2 = 1.90$, and the spot price is $S_1 = 2.50$ and $S_2 = 2.00$, what is the basis at $t_1$ and $t_2$?

**A:** The basis at $t_1$ is $0.30$ and the basis at $t_2$ is $0.10$.

---

## Card 46

**Q:** How does the 'tailing' adjustment affect the number of contracts if the futures price is higher than the spot price?

**A:** It reduces the number of contracts since $V_A/V_F < Q_A/Q_F$.

---

## Card 47

**Q:** Term: Minimum Variance Hedge Ratio

**A:** Definition: The hedge ratio that results in the smallest possible variance for the value of the hedged position. Example: Calculating $h^* = 0.78$ for heating oil hedging jet fuel based on historical data.

---

## Card 48

**Q:** How can a fund manager 'lock in' a future purchase price for a stock index when they expect a cash inflow in one month?

**A:** By taking a long position in index futures today.

---

## Card 49

**Q:** What is the 'risk-free return' in the context of an equity portfolio hedge?

**A:** The return earned when the portfolio is perfectly hedged against market movements, often proxied by the Treasury bill rate.

---

## Card 50

**Q:** Why might a company choose NOT to hedge despite having significant exposure?

**A:** To avoid the costs of hedging, because shareholders are already diversified, or because competitors are also unhedged.

---

## Card 51

**Q:** In the formula $N = \beta \frac{V_A}{V_F}$, what happens to $N$ if the index level doubles while the portfolio value remains constant?

**A:** The number of contracts $N$ required to hedge the portfolio decreases by half.

---

## Card 52

**Q:** What is the primary objective of a 'short' hedger regarding price movements?

**A:** To offset a loss in the value of their physical asset with a gain in their short futures position.

---

## Card 53

**Q:** What does a negative basis imply about the relationship between spot and futures prices?

**A:** The futures price is higher than the spot price.

---

## Card 54

**Q:** How does 'daily settlement' influence the decision to 'tail' a hedge?

**A:** It recognises that profits/losses are realised daily and can earn interest, rather than being realised only at the end of the hedge.

---

## Card 55

**Q:** Why is the correlation coefficient $\rho$ squared to find hedge effectiveness?

**A:** Because $R^2$ represents the percentage of variance (the square of standard deviation) that is reduced.

---

## Card 56

**Q:** If a hedge is $100\%$ effective, what must the correlation $\rho$ be?

**A:** $1.0$ or $-1.0$.

---

## Card 57

**Q:** What is the 'effective price' paid by a long hedger if the basis strengthens unexpectedly?

**A:** The effective price paid will be higher than originally anticipated.

---

## Card 58

**Q:** How does the 'Appendix: Capital Asset Pricing Model' in Chapter 3 relate to hedging?

**A:** It provides the theoretical framework for understanding why market risk ($eta$) is the only risk that requires a risk premium.

---

## Card 59

**Q:** Term: Hedge-and-Forget

**A:** Definition: A hedging strategy where the position is established and then left unchanged until the hedge expires. Example: A treasurer buying 50 gold futures to hedge a purchase in December and holding them until the purchase date.

---

## Card 60

**Q:** Why is 'basis risk' higher in cross-hedging than in direct hedging?

**A:** Because it includes both the timing risk of the contract and the risk that the prices of the two different assets will not move in tandem.

---
