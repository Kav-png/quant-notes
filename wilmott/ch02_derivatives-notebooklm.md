# Options Flashcards

## Card 1

**Q:** Term: Call Option

**A:** Definition: A contract giving the holder the right, but not the obligation, to buy an underlying asset at a specified strike price at a specified future time. Example: Holding a call on Apple with a strike of $40$ allows you to buy the stock for $40$ even if the market price is $50$.

---

## Card 2

**Q:** Term: Put Option

**A:** Definition: A contract giving the holder the right, but not the obligation, to sell an underlying asset at a specified strike price at a specified future time. Example: A put option with a strike of $100$ allows you to sell a stock for $100$ even if its market price has fallen to $80$.

---

## Card 3

**Q:** Formula: European Call Option Payoff at Expiry

**A:** $\max(S - E, 0)$, where $S$ is the underlying asset price at expiry and $E$ is the strike price.

---

## Card 4

**Q:** Formula: European Put Option Payoff at Expiry

**A:** $\max(E - S, 0)$, where $E$ is the strike price and $S$ is the underlying asset price at expiry.

---

## Card 5

**Q:** Term: Strike Price (Exercise Price)

**A:** Definition: The previously agreed-upon price at which the underlying asset can be bought (for a call) or sold (for a put) at exercise. Example: If you have a call with a strike of $25$, you have the right to purchase the stock for exactly $25$.

---

## Card 6

**Q:** Term: Expiration Date (Expiry)

**A:** Definition: The specific date on which an option must be exercised or it ceases to exist and gives the holder no further rights. Example: An option expiring on the third Friday of April cannot be used to trade the underlying asset on Saturday.

---

## Card 7

**Q:** Term: Underlying Asset

**A:** Definition: The financial instrument (such as a stock, commodity, or index) upon which the value of an option contract depends. Example: In a call option on Microsoft, Microsoft stock is the underlying asset.

---

## Card 8

**Q:** Term: Premium

**A:** Definition: The initial amount of money paid by the buyer to the writer to acquire the rights granted by an option contract. Example: Paying $1.875$ up front to own a call option that expires in one month.

---

## Card 9

**Q:** Term: Intrinsic Value

**A:** Definition: The payoff that would be received if the underlying asset were at its current market level when the option expires. Example: A call with a strike of $40$ has $2.50$ of intrinsic value if the current stock price is $42.50$.

---

## Card 10

**Q:** Term: Time Value

**A:** Definition: The portion of an option's market value that exceeds its intrinsic value, reflecting the possibility of future price movements. Example: An option with a premium of $3.00$ and intrinsic value of $2.00$ has $1.00$ of time value.

---

## Card 11

**Q:** Term: In the Money (ITM)

**A:** Definition: An option that has positive intrinsic value, meaning the market price is favorable relative to the strike. Example: A call option is ITM when the asset price is higher than the strike price.

---

## Card 12

**Q:** Term: Out of the Money (OTM)

**A:** Definition: An option with no intrinsic value, where its entire value consists of time value. Example: A call option is OTM when the asset price is lower than the strike price.

---

## Card 13

**Q:** Term: At the Money (ATM)

**A:** Definition: An option where the strike price is equal or very close to the current market price of the underlying asset. Example: A call with a strike of $50$ when the stock is trading at $50.05$.

---

## Card 14

**Q:** Term: Long Position

**A:** Definition: A market position where an investor owns a quantity of an asset or has positive exposure to its price increase. Example: Buying one call option gives the investor a long position in that option.

---

## Card 15

**Q:** Term: Short Position

**A:** Definition: A market position involving a negative amount of an asset or a negative exposure to its price movement. Example: Writing an option for a premium creates a short position for the writer.

---

## Card 16

**Q:** What is the primary difference between a payoff diagram and a profit diagram?

**A:** A payoff diagram shows the value at expiry, while a profit diagram subtracts the initial premium paid to show the net gain or loss.

---

## Card 17

**Q:** Term: Writing an Option

**A:** Definition: The act of selling an option contract and receiving the premium in exchange for the obligation to fulfill the contract if exercised. Example: A trader writes a put, receiving $5$ but agreeing to buy the stock at $100$ if the holder exercises.

---

## Card 18

**Q:** Term: Margin

**A:** Definition: The collateral deposit required by clearing houses from option writers to cover the risk of potential default on their obligations. Example: A writer depositing cash or securities to ensure they can pay the holder if a short call goes deep into the money.

---

## Card 19

**Q:** Term: American Option

**A:** Definition: An option contract that allows the holder the right to exercise at any time during the life of the contract up to expiry. Example: Exercising a call option two weeks before its three-month expiry date.

---

## Card 20

**Q:** Term: European Option

**A:** Definition: An option contract that can only be exercised on the specific expiration date itself. Example: A call option that forbids the holder from buying the underlying asset until the final Friday of the contract.

---

## Card 21

**Q:** Term: Bermudan Option

**A:** Definition: An option that allows exercise only on specific pre-determined dates or during specific periods before the expiration date. Example: An option that can only be exercised on the first day of every month until it expires.

---

## Card 22

**Q:** How does increasing the strike price affect the value of call versus put options?

**A:** Increasing the strike price decreases the value of call options but increases the value of put options.

---

## Card 23

**Q:** Formula: Put-Call Parity for European Options

**A:** $C - P = S - E e^{-r(T-t)}$, where $C = call\ price$, $P = put\ price$, $S = asset\ price$, $E = strike$, $r = interest\ rate$, and $T-t = time\ to\ expiry$.

---

## Card 24

**Q:** How is Put-Call Parity derived using a portfolio approach?

**A:** The key insight is that a portfolio of a long call and a short put yields the exact same payoff at expiry as a long position in the underlying asset and a short cash position.

---

## Card 25

**Q:** Term: Binary Call Option (Digital Call)

**A:** Definition: An option that pays a fixed amount, typically $1$, if the underlying asset price is above the strike at expiry, and zero otherwise. Example: A contract that pays $1$ only if the DJIA is above $11,000$ on March 1st.

---

## Card 26

**Q:** Term: Binary Put Option (Digital Put)

**A:** Definition: An option that pays a fixed amount, typically $1$, if the underlying asset price is below the strike at expiry, and zero otherwise. Example: A contract that pays $1$ if a stock finishes below $50$ at the end of the month.

---

## Card 27

**Q:** Formula: Binary Put-Call Parity

**A:** $Binary\ Call + Binary\ Put = e^{-r(T-t)}$, where $r$ is the interest rate and $T-t$ is the time to maturity.

---

## Card 28

**Q:** Term: Bull Spread (Call Spread)

**A:** Definition: An option strategy involving the purchase of a call with a low strike and the sale of a call with a higher strike, both with the same expiry. Example: Buying a $100$ strike call and writing a $120$ strike call to profit from a rising market while limiting cost.

---

## Card 29

**Q:** Term: Bear Spread (Put Spread)

**A:** Definition: An option strategy involving the purchase of a high-strike put and the sale of a lower-strike put with the same expiry. Example: Buying a $120$ strike put and writing a $100$ strike put to benefit from a falling market.

---

## Card 30

**Q:** Term: Straddle

**A:** Definition: A strategy where an investor buys both a call and a put with the identical strike price and expiration date. Example: Buying a $100$ call and a $100$ put to profit from high volatility, regardless of the price direction.

---

## Card 31

**Q:** Term: Strangle

**A:** Definition: A strategy similar to a straddle but using a call with a higher strike price than the put. Example: Buying a $110$ call and a $90$ put to profit from a very large move in either direction at a lower cost than a straddle.

---

## Card 32

**Q:** Term: Butterfly Spread

**A:** Definition: A strategy involving three strikes where you buy one call at strike $E_1$, sell two calls at $E_2$, and buy one call at $E_3$ (where $E_1 < E_2 < E_3$). Example: A position built to profit if the asset price stays very close to $E_2$ at expiry.

---

## Card 33

**Q:** Term: Risk Reversal

**A:** Definition: A strategy consisting of a long call and a short put with different strike prices but the same expiry. Example: Buying a $110$ call and writing a $90$ put to create a position that mimics the underlying asset with a gap.

---

## Card 34

**Q:** Term: Condor

**A:** Definition: A strategy similar to a butterfly spread but utilizing four different strike prices instead of three. Example: Buying a $90$ call, selling a $100$ call, selling a $110$ call, and buying a $120$ call.

---

## Card 35

**Q:** Term: Calendar Spread

**A:** Definition: A strategy involving the purchase and sale of options with the same strike price but different expiration dates. Example: Selling a call expiring in one month and buying a call with the same strike expiring in three months.

---

## Card 36

**Q:** Term: LEAPS

**A:** Definition: Long-term Equity Anticipation Securities, which are exchange-traded options with much longer durations, typically up to three years. Example: Buying a call on a stock index that expires in January three years from now.

---

## Card 37

**Q:** Term: FLEX Options

**A:** Definition: FLexible EXchange-traded options that allow investors to customize terms like strike price, expiry date, and exercise style within an exchange environment. Example: Creating a call with an unusual expiry date of 4.5 years through the CBOE.

---

## Card 38

**Q:** Term: Warrants

**A:** Definition: Call options issued directly by a company on its own shares, resulting in new share issuance upon exercise. Example: A company issuing warrants to bondholders as an additional incentive, which dilutes existing shares if exercised.

---

## Card 39

**Q:** Term: Over the Counter (OTC) Options

**A:** Definition: Privately negotiated option contracts between two parties that do not follow the standardized conventions of exchange-traded options. Example: A bank selling a tailored put option with a contingent premium to a corporate client.

---

## Card 40

**Q:** Term: Gearing (Leverage)

**A:** Definition: The potential for a derivative to provide a significantly higher percentage return (or loss) than the underlying asset for a given move. Example: A stock rising $9.6\%$ resulting in a $28\%$ profit for a call option holder.

---

## Card 41

**Q:** Pitfall: What is the common misconception regarding the names 'American' and 'European' options?

**A:** They refer only to the exercise style (any time vs. expiry only) and do not indicate the continent or market where they are traded.

---

## Card 42

**Q:** Pitfall: What is the danger of writing options compared to buying them?

**A:** The buyer's loss is limited to the premium, while the writer faces potentially unlimited losses for a call or significant losses for a put.

---

## Card 43

**Q:** Pitfall: Why is a simple profit diagram that subtracts premium from payoff fundamentally incomplete?

**A:** It ignores the time value of money, as the premium is paid at $t=0$ while the payoff occurs at $t=T$; technically, cashflows should be discounted or compounded to a single date.

---

## Card 44

**Q:** How does the 'time to expiry' affect an option's convergence at maturity?

**A:** As time to expiry decreases, the option's value must converge to its payoff function as there is less time for the underlying to move.

---

## Card 45

**Q:** What distinction does Wilmott make between 'variables' and 'parameters' in option pricing?

**A:** Variables ($S$ and $t$) change inevitably during the contract's life, while parameters ($r$, $E$, and volatility) are generally held constant within the pricing model's equations.

---

## Card 46

**Q:** Why might an investor prefer a binary call over a vanilla call?

**A:** Binary calls can offer higher gearing for modest price rises above the strike, whereas vanilla calls are better for profiting from dramatic, unlimited price increases.

---

## Card 47

**Q:** True or False: In a perfectly hedged portfolio under Put-Call Parity, the future cashflow is zero.

**A:** True; because the future cashflow is zero, the value of the portfolio today must also be zero to prevent arbitrage.

---

## Card 48

**Q:** What is the role of an exchange 'clearing house' in derivatives trading?

**A:** The clearing house acts as the counterparty to every transaction, registering and settling trades to ensure the integrity of the market.

---

## Card 49

**Q:** Term: Hedging

**A:** Definition: The practice of buying or selling related financial contracts to offset the risk of an existing position. Example: An option writer buying the underlying stock to reduce the risk of a short call position.

---

## Card 50

**Q:** In the money (ITM) options have both _____ value and _____ value.

**A:** Intrinsic; Time

---

## Card 51

**Q:** If a call option is Out of the Money (OTM), its intrinsic value is _____.

**A:** Zero

---

## Card 52

**Q:** How is the 'Time Value' of an option related to the 'Intrinsic Value'?

**A:** $Time\ Value = Option\ Value - Intrinsic\ Value$.

---

## Card 53

**Q:** What happens to the intrinsic value of a call option as the underlying stock price rises?

**A:** The intrinsic value increases linearly once the stock price exceeds the strike price.

---

## Card 54

**Q:** What is the key characteristic of an 'Over the Counter' (OTC) term sheet?

**A:** It specifies the precise, non-standard details of a private contract, often including contingent features or customized triggers.

---

## Card 55

**Q:** Why does a higher volatility parameter usually lead to a higher option premium?

**A:** Higher volatility increases the probability that the underlying asset will move significantly into the money before expiry.

---

## Card 56

**Q:** What is 'at the money' (ATM) in the context of strike price?

**A:** A strike price that is very close to the current market level of the underlying asset.

---

## Card 57

**Q:** An option writer is sometimes called the _____ of the option.

**A:** Seller

---

## Card 58

**Q:** An option buyer is often called the _____ of the option.

**A:** Holder (or Purchaser)

---

## Card 59

**Q:** How does 'time value of money' affect the valuation of a payoff received in the future?

**A:** Future payoffs are worth less today; they must be discounted by multiplying by $e^{-r(T-t)}$.

---

## Card 60

**Q:** A portfolio consisting of a long call and a short call with a higher strike is a _____.

**A:** Bull Spread

---

## Card 61

**Q:** A portfolio consisting of a long put and a short put with a lower strike is a _____.

**A:** Bear Spread

---

## Card 62

**Q:** What is the payoff at expiry of a portfolio with one long call and one short put at the same strike $E$?

**A:** $S(T) - E$.

---

## Card 63

**Q:** Concept: Optionality

**A:** Definition: The characteristic of an option that provides the right to benefit from favorable price moves while avoiding the obligation of unfavorable ones. Example: Choosing not to exercise a call option when the stock price is $10$ below the strike.

---

## Card 64

**Q:** What is the meaning of a 'series' in exchange-traded options?

**A:** A group of option contracts sharing the same strike price and expiration date for a specific underlying asset.

---
