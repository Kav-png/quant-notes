

## Card 1

**Q:** List the assumptions underlying the Black-Scholes-Merton model.

**A:** (1) Stock price follows GBM with constant \(\mu\), \(\sigma\). (2) No transaction costs/taxes; securities perfectly divisible. (3) No dividends during the option's life (relaxed by Merton 1973). (4) No arbitrage opportunities. (5) Trading is continuous. (6) Short selling permitted with full use of proceeds. (7) Risk-free rate \(r\) is constant and the same for all maturities.

---

## Card 2

**Q:** Write the SDE for the stock price under the BSM model and name each term.

**A:** \[ dS = \mu S\,dt + \sigma S\,dz \] \(\mu\) is the (constant) expected return, \(\sigma\) the (constant) volatility, \(dz\) a Wiener process. This implies \(S\) is lognormally distributed: \(\ln S_T \sim \phi(\ln S_0 + (\mu-\sigma^2/2)T,\ \sigma^2 T)\).

---

## Card 3

**Q:** In deriving the BSM PDE, what portfolio is constructed and why does it eliminate the random (\(dz\)) term?

**A:** Short 1 unit of the derivative, long \(\partial f/\partial S\) shares of the stock. Both the derivative (via Itô's lemma) and the stock have a \(dz\) term proportional to \(\sigma S\); choosing this exact hedge ratio makes the two cancel, leaving a portfolio whose value change over \(dt\) is deterministic — i.e. instantaneously riskless, so it must earn exactly \(r\).

---

## Card 4

**Q:** Write the Black-Scholes-Merton partial differential equation.

**A:** \[ \frac{\partial f}{\partial t} + rS\frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 f}{\partial S^2} = rf \]

---

## Card 5

**Q:** Why does the real-world drift \(\mu\) not appear in the BSM PDE, and what does this license us to do?

**A:** The riskless-hedge construction cancels \(\mu\) out algebraically when forming the PDE, so the PDE — and hence the derivative's price — does not depend on risk preferences or the real-world expected return. This licenses risk-neutral valuation: we can price the derivative in a fictitious world where every asset earns \(r\), avoiding the need to ever estimate \(\mu\).

---

## Card 6

**Q:** Write the formulas for \(d_1\) and \(d_2\) in the BSM model.

**A:** \[ d_1 = \frac{\ln(S_0/K) + (r+\sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T} \]

---

## Card 7

**Q:** Write the closed-form price of a European call option under BSM.

**A:** \[ c = S_0 N(d_1) - Ke^{-rT}N(d_2) \] \(N(d_2)\) is the risk-neutral probability of exercise; \(S_0N(d_1)\) is the present value of the stock received conditional on exercise.

---

## Card 8

**Q:** Write the closed-form price of a European put option under BSM.

**A:** \[ p = Ke^{-rT}N(-d_2) - S_0 N(-d_1) \]

---

## Card 9

**Q:** State put-call parity for European options and confirm it follows from the BSM call/put formulas.

**A:** \(c - p = S_0 - Ke^{-rT}\). Subtracting the put formula from the call formula: \(S_0N(d_1)-Ke^{-rT}N(d_2) - [Ke^{-rT}N(-d_2)-S_0N(-d_1)] = S_0[N(d_1)+N(-d_1)] - Ke^{-rT}[N(d_2)+N(-d_2)] = S_0(1) - Ke^{-rT}(1)\), since \(N(x)+N(-x)=1\).

---

## Card 10

**Q:** Define Delta for a call option and give its BSM formula.

**A:** Delta \(=\partial c/\partial S = N(d_1)\). It is the hedge ratio: shares of stock needed to offset the option's price sensitivity to a small move in \(S\).

---

## Card 11

**Q:** Define Gamma. Why is Gamma identical for a call and a put with the same strike and expiry?

**A:** Gamma \(=\partial^2 c/\partial S^2 = \dfrac{N'(d_1)}{S_0\sigma\sqrt{T}}\). From put-call parity \(c-p=S_0-Ke^{-rT}\), the RHS is linear in \(S_0\) (zero second derivative), so \(\partial^2c/\partial S^2=\partial^2p/\partial S^2\) — Gamma must match.

---

## Card 12

**Q:** Define Vega. Why is its existence a notable internal tension within the BSM model?

**A:** Vega \(=\partial c/\partial\sigma = S_0N'(d_1)\sqrt{T}\). The model assumes \(\sigma\) is constant, yet the price has nonzero sensitivity to it — in practice traders hedge against changes in a parameter the model itself treats as fixed, which is the standard caveat about using BSM Greeks for real risk management.

---

## Card 13

**Q:** Define Rho for a call option and give its BSM formula.

**A:** Rho \(=\partial c/\partial r = KTe^{-rT}N(d_2)\) — sensitivity of the option price to the risk-free rate.

---

## Card 14

**Q:** How is implied volatility defined, and why can't it be solved in closed form?

**A:** Implied vol \(\sigma_{IV}\) is the value of \(\sigma\) that makes the BSM formula equal the observed market price of the option. Because \(\sigma\) enters \(d_1\)/\(d_2\) nonlinearly inside \(N(\cdot)\), the pricing formula cannot be algebraically inverted for \(\sigma\) — it must be solved numerically (root-finding on price as a function of \(\sigma\)).

---

## Card 15

**Q:** What does Peter Jäckel's "Let's Be Rational" technique do differently from naive bisection when solving for implied volatility, and why does that matter for a deterministic MCP pricing tool?

**A:** It converges to machine precision in at most two Newton-type iterations using a rational approximation tailored to the BSM price function, instead of many bisection steps governed by a tolerance/iteration cap. For a deterministic tool, this matters because the same inputs must always produce the identical output to full float precision — a tolerance-bounded bisection solver can give slightly different answers depending on iteration limits, breaking that guarantee.

---

## Card 16

**Q:** How does the Merton (1973) extension modify \(d_1\) and the call price formula to handle a continuous dividend yield \(q\)?

**A:** Replace \(S_0\) with \(S_0e^{-qT}\) wherever it appears (discounting the stock for dividends paid out): \[ d_1 = \frac{\ln(S_0/K)+(r-q+\sigma^2/2)T}{\sigma\sqrt{T}} \] \[ c = S_0e^{-qT}N(d_1) - Ke^{-rT}N(d_2) \]

---

## Card 17

**Q:** Name two empirical phenomena that violate BSM's assumptions, and what each implies about using a single \(\sigma\) across an entire option chain.

**A:** (1) Volatility smile/skew: the market prices different strikes as if \(\sigma\) varies by strike, contradicting the constant-\(\sigma\) assumption — so implied vol must be computed per-strike, not assumed global. (2) Jumps: GBM paths are continuous, but real prices gap on news (earnings, M&A) — BSM underprices tail risk; Merton's jump-diffusion model relaxes this at the cost of extra parameters.

---

## Card 18

**Q:** Define Theta for a call option. What sign does it typically have for a long option position, and why?

**A:** Theta \(=\partial c/\partial t = -\dfrac{S_0N'(d_1)\sigma}{2\sqrt{T}} - rKe^{-rT}N(d_2)\). Usually negative for a long call/put: as time passes with \(S\) and \(\sigma\) held fixed, less time remains for the underlying to move favorably, so the option's time value decays ("time decay").

---
