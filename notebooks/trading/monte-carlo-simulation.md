Monte Carlo Simulation: Building R Code Step by Step\
From Random Walks to Asset Price Modeling (M02)

---

## STEP 1: Basic Coin Flip Random Walk\\

### The Concept

A random walk starts with independent coin flips. Each flip is +1 or -1 with equal probability (50%). This is the basic "innovation" or "shock" (z_t) that drives the process.

### The Math

$z_t \sim Bernoulli(p=0.5) → ±1$ with equal probability

```r
# Generate 100 random coin flips
n <- 100
p <- 0.5  # probability threshold

# Generate uniform random numbers [0,1]
z <- runif(n)

# Convert to ±1
# If z < p: sign(p - z) = sign(positive) = +1
# If z > p: sign(p - z) = sign(negative) = -1
x <- sign(p - z)

# Check first 20 flips
print(head(x, 20))
# Output: 1 -1 1 1 -1 -1 1 -1 1 1 -1 1 -1 -1 1 1 1 -1 1 -1
```

### What's Happening

- `runif(n)` generates n uniform random numbers between 0 and 1
- We compare each to 0.5 to get a 50/50 split
- `sign()` converts the result to +1 or -1
- These are independent draws—each flip has no memory of the previous one (IID)

---

## STEP 2: Build the Cumulative Random Walk

### The Concept

A random walk is the sum of independent increments. Each position is the previous position plus the current flip:

$$S_t = S_{t-1} + x_t = S_0 + x_1 + x_2 + ... + x_t$$

From M02 theory: **Var(S_t) = t** (variance grows linearly with time, std dev grows as √t)

### The R Code

```r
# Start from Step 1
n <- 100
p <- 0.5
z <- runif(n)
x <- sign(p - z)

# Build cumulative sum (the random walk)
S <- c(0, cumsum(x))  # Start at 0, then add each flip

# S is now length 101 (0 to 100 steps)
# S[1] = 0 (starting point)
# S[2] = 0 + x[1]
# S[3] = 0 + x[1] + x[2]
# ...
# S[101] = sum of all flips

# Plot it
plot(0:n, S, type='l', 
     main='Simple Random Walk',
     xlab='Time (steps)', 
     ylab='Position',
     col='steelblue',
     lwd=2)
grid()

# Print summary statistics
cat("Final position:", S[n+1], "\n")
cat("Maximum reached:", max(S), "\n")
cat("Minimum reached:", min(S), "\n")
cat("Theoretical std dev at t=100: sqrt(100) =", sqrt(100), "\n")
```

### Key Output

The plot shows a jagged path wandering up and down from 0. By step 100, the path might be anywhere from -20 to +20 (roughly ±√100 = ±10).

---

## STEP 3: Multiple Paths (The Core of Monte Carlo)

### The Concept

A single random walk is just one realization of randomness. To understand the **distribution** of outcomes, we generate many paths (say 1,000). Each column of a matrix is an independent path. Then we compute statistics across paths.

### The Math

- Generate Nt × Np matrix of random increments
- Compute Np independent cumulative paths
- At each time t, compute mean and std deviation across paths

### The R Code

```r
# Parameters
Nt <- 100  # number of time steps
Np <- 1000 # number of paths

# Generate random flips for ALL paths at once
# Result: 100 x 1000 matrix
z <- matrix(runif(Nt * Np), nrow=Nt)  # Each column is one path's flips
x <- sign(0.5 - z)  # Convert to ±1 (elementwise)

# Build cumulative paths
# Each column is one random walk
# Start with row of zeros
S <- rbind(rep(0, Np), apply(x, 2, cumsum))
# apply(x, 2, cumsum) applies cumsum to each column (MARGIN=2)
# Result: 101 x 1000 matrix

# Compute statistics across paths (across columns)
mean_path <- rowMeans(S)      # Mean at each time
sd_path <- apply(S, 1, sd)    # Std dev at each time

# Plot mean and confidence band
plot(0:Nt, mean_path, type='l', col='red', lwd=2,
     main='Monte Carlo Random Walk (1000 paths)',
     xlab='Time', ylab='Position',
     ylim=c(mean_path - 2*sd_path)[1:50], c(mean_path + 2*sd_path)[1:50])

# Add ±1σ band
lines(0:Nt, mean_path + sd_path, col='orange', lty=2)
lines(0:Nt, mean_path - sd_path, col='orange', lty=2)

# Check theory: Var(S_t) = t
t_values <- 0:Nt
theoretical_sd <- sqrt(t_values)
empirical_sd <- sd_path

plot(t_values, empirical_sd, type='l', col='blue', lwd=2,
     main='Standard Deviation: Theory vs Empirical',
     xlab='Time', ylab='Std Dev')
lines(t_values, theoretical_sd, col='red', lwd=2, lty=2)
legend('topleft', c('Empirical (1000 paths)', 'Theory (sqrt(t))'),
       col=c('blue', 'red'), lty=c(1,2))
```

### Key Insight

The empirical std dev (from the simulation) matches the theoretical √t almost perfectly! This is why Monte Carlo works—with enough paths, we recover exact results.

---

## STEP 4: Add Drift and Volatility

### The Concept

Real returns aren't ±1 equally. They have:

- **Drift (μ)**: Expected return direction (e.g., +1% per period)
- **Volatility (σ)**: Size of random moves (e.g., ±2%)

We scale random increments: **r_t = μ + σ·z_t** where z_t \~ Normal(0,1)

From M02 theory:

- E$r_t$ = μ
- Var(r_t) = σ²
- E$Σ r_t$ = T·μ (cumulative expected return = T×μ)
- Var(Σ r_t) = T·σ² (cumulative variance = T×σ²)

### The R Code

```r
# Parameters
Nt <- 100
Np <- 1000
mu <- 0.01     # 1% drift per period
sigma <- 0.02  # 2% volatility per period

# Generate normal random increments (not uniform!)
# rnorm gives Normal(mean, sd)
r <- matrix(rnorm(Nt * Np, mean=mu, sd=sigma), nrow=Nt)
# r is 100 x 1000 matrix of returns

# Build cumulative paths
X <- rbind(rep(0, Np), apply(r, 2, cumsum))
# X[t+1,] = sum of r[1:t,]

# Compute statistics
mean_X <- rowMeans(X)
sd_X <- apply(X, 1, sd)

# Theoretical values
theoretical_mean <- (0:Nt) * mu
theoretical_sd <- sqrt((0:Nt)) * sigma

# Plot comparison
plot(0:Nt, mean_X, type='l', col='blue', lwd=2,
     main='Drift + Volatility Process',
     xlab='Time', ylab='Cumulative Return')
lines(0:Nt, theoretical_mean, col='red', lwd=2, lty=2)
lines(0:Nt, mean_X + sd_X, col='orange', lty=2)
lines(0:Nt, mean_X - sd_X, col='orange', lty=2)

legend('topleft', c('Empirical mean', 'Theory (μ·t)', '±1σ band'),
       col=c('blue', 'red', 'orange'), lty=c(1,2,2))

# Check: at t=100, we expect
cat("t=100 expected mean:", 100 * mu, "\n")      # Should be 1.00
cat("t=100 empirical mean:", mean_X[101], "\n")  # Should be close
cat("t=100 expected std dev:", sqrt(100) * sigma, "\n")  # Should be 0.20
cat("t=100 empirical std dev:", sd_X[101], "\n") # Should be close
```

---

## STEP 5: Convert to Asset Prices (Lognormal)

### The Concept

Asset prices must:

1. **Always be positive** (can't have negative stock price)
2. **Follow lognormal distribution** (log-returns are normal)

We use: **P_t = P_0 · exp(X_t)** where X_t = Σ log-returns

This ensures P_t &gt; 0 always, and matches Black-Scholes framework.

### The Math

```
log(P_t / P_0) = r_1 + r_2 + ... + r_t  (cumulative log-returns)
P_t = P_0 · exp(r_1 + r_2 + ... + r_t)
```

### The R Code

```r
# Parameters
P0 <- 100  # Initial price
mu <- 0.01
sigma <- 0.02
Nt <- 100
Np <- 1000

# Generate log-returns (same as Step 4)
r <- matrix(rnorm(Nt * Np, mean=mu, sd=sigma), nrow=Nt)
X <- rbind(rep(0, Np), apply(r, 2, cumsum))

# Convert to prices
# This is the KEY transformation:
P <- P0 * exp(X)  # Element-wise: each price = 100 * exp(log-return)

# Verify prices are positive
cat("Min price:", min(P), "\n")  # Should be > 0
cat("Max price:", max(P), "\n")

# Statistics
mean_price <- rowMeans(P)
sd_price <- apply(P, 1, sd)

# Plot: mean price path with ±1σ band
plot(0:Nt, mean_price, type='l', col='darkblue', lwd=2,
     main='Asset Price Simulation (1000 paths)',
     xlab='Time (days)', ylab='Price ($)',
     ylim=c(min(mean_price - sd_price), max(mean_price + sd_price)))

lines(0:Nt, mean_price + sd_price, col='orange', lty=2, lwd=1.5)
lines(0:Nt, mean_price - sd_price, col='orange', lty=2, lwd=1.5)

# Plot sample of 10 paths
for (i in 1:10) {
  lines(0:Nt, P[, i], col=rgb(0, 0.5, 1, alpha=0.2), lty=1)
}
legend('topleft', c('Mean path', '±1σ band', 'Sample paths (n=10)'),
       col=c('darkblue', 'orange', rgb(0, 0.5, 1, alpha=0.2)), lty=c(1,2,1))

# Expected final price (using theory)
E_P_final <- P0 * exp(mu * Nt)
cat("Expected final price:", E_P_final, "\n")
cat("Empirical final price (mean):", mean_price[Nt+1], "\n")
```

### Key Output

- Initial price: 100
- After 100 periods with μ=1%, σ=2%: Expected price ≈ 100·exp(1) ≈ 271.8
- The cone widens (increasing uncertainty) as time progresses
- Prices never go negative (always exp() &gt; 0)

---

## STEP 6: Time Scaling (Realistic Calendar Time)

### The Concept

Annual parameters must be scaled to the data frequency. For **daily** data:

- dt = 1/252 (252 trading days per year)
- μ\_daily = μ\_annual × dt
- σ\_daily = σ\_annual × √dt

This matches real option pricing and portfolio management.

### The Math

```
If annual parameters are (μ=5%, σ=20%), then daily are:
μ_daily = 0.05 × (1/252) ≈ 0.000198
σ_daily = 0.20 × √(1/252) ≈ 0.01265
```

### The R Code

```r
# ANNUAL PARAMETERS (realistic)
# Parameters
Nt <- 100  # number of time steps
Np <- 1000 # number of paths

# Generate random flips for ALL paths at once
z <- matrix(runif(Nt * Np), nrow=Nt)
x <- sign(0.5 - z)

# Build cumulative paths
S <- rbind(rep(0, Np), apply(x, 2, cumsum))

# Compute statistics across paths
mean_path <- rowMeans(S)
sd_path <- apply(S, 1, sd)

# Plot mean and confidence band - FIXED ylim
plot(0:Nt, mean_path, type='l', col='red', lwd=2,
     main='Monte Carlo Random Walk (1000 paths)',
     xlab='Time', ylab='Position',
     ylim=c(min(mean_path - 2*sd_path), max(mean_path + 2*sd_path)))

# Add ±1σ band
lines(0:Nt, mean_path + sd_path, col='orange', lty=2)
lines(0:Nt, mean_path - sd_path, col='orange', lty=2)

# Check theory: Var(S_t) = t
t_values <- 0:Nt
theoretical_sd <- sqrt(t_values)
empirical_sd <- sd_path

plot(t_values, empirical_sd, type='l', col='blue', lwd=2,
     main='Standard Deviation: Theory vs Empirical',
     xlab='Time', ylab='Std Dev')
lines(t_values, theoretical_sd, col='red', lwd=2, lty=2)
legend('topleft', c('Empirical (1000 paths)', 'Theory (sqrt(t))'),
       col=c('blue', 'red'), lty=c(1,2))
```

### Why This Matters

- **Without scaling**: dt × period would grow unbounded, breaking the model
- **With scaling**: Parameters adjust so 1 year of daily data ≈ 1 year of weekly data ≈ 1 year of annual data (mathematically equivalent)
- This is how **option prices** are calculated (Black-Scholes uses daily or continuous time scaling)

---

## PUTTING IT ALL TOGETHER: Complete Example

```r
# ============================================
# Complete Monte Carlo Asset Price Simulation
# ============================================

# 1. PARAMETERS (annualized, realistic stock)
P0 <- 100           # Initial price
mu_annual <- 0.08   # 8% annual drift
sigma_annual <- 0.25 # 25% annual volatility
years <- 2
days_per_year <- 252

# 2. TIME PARAMETERS
total_days <- years * days_per_year
dt <- 1 / days_per_year
mu_daily <- mu_annual * dt
sigma_daily <- sigma_annual * sqrt(dt)

# 3. MONTE CARLO PARAMETERS
Np <- 10000  # 10,000 paths for better statistics

# 4. GENERATE RETURNS
r <- matrix(rnorm(total_days * Np, mean=mu_daily, sd=sigma_daily), 
            nrow=total_days)

# 5. BUILD PRICE PATHS
log_returns <- rbind(rep(0, Np), apply(r, 2, cumsum))
prices <- P0 * exp(log_returns)

# 6. ANALYZE RESULTS
mean_price <- rowMeans(prices)
sd_price <- apply(prices, 1, sd)
min_price <- apply(prices, 1, min)
max_price <- apply(prices, 1, max)

# 7. COMPUTE RISK METRICS
final_prices <- prices[total_days + 1, ]
quantile_5 <- quantile(final_prices, 0.05)
quantile_50 <- quantile(final_prices, 0.50)
quantile_95 <- quantile(final_prices, 0.95)
expected_return <- mean(final_prices) / P0 - 1
value_at_risk <- P0 - quantile_5

# FIXED: Use paste(rep("=", 50), collapse="") instead of "="*50
cat(paste(rep("=", 50), collapse=""), "\n")
cat("MONTE CARLO RESULTS (10,000 paths, 2 years)\n")
cat(paste(rep("=", 50), collapse=""), "\n")
cat("Expected final price: $", round(mean(final_prices), 2), "\n")
cat("5th percentile: $", round(quantile_5, 2), "\n")
cat("50th percentile (median): $", round(quantile_50, 2), "\n")
cat("95th percentile: $", round(quantile_95, 2), "\n")
cat("\nExpected return:", round(expected_return*100, 2), "%\n")
cat("Value at Risk (5%):", round(value_at_risk, 2), "\n")

# 8. PLOT
plot_days <- 0:(total_days)
plot(plot_days, mean_price, type='l', lwd=2, col='darkblue',
     main='2-Year Stock Price Forecast',
     xlab='Days', ylab='Price ($)',
     ylim=c(min(min_price), max(max_price)))
lines(plot_days, mean_price + 1.96*sd_price, lty=2, col='red', lwd=1.5)
lines(plot_days, mean_price - 1.96*sd_price, lty=2, col='red', lwd=1.5)
abline(h=quantile_95, lty=3, col='green')
abline(h=quantile_5, lty=3, col='red')
legend('topleft', 
       c('Mean path', '±95% CI', '5th/95th %ile'),
       col=c('darkblue', 'red', 'green'), lty=c(1,2,3))
```

---

## Summary: Building Blocks to Remember

| Step | Key Function | Purpose |
| --- | --- | --- |
| 1 | `runif()` | Random shocks (uniform) |
| 2 | `cumsum()` | Cumulative sum = random walk |
| 3 | `matrix()`, `apply()` | Multiple paths at once |
| 4 | `rnorm()` | Normal increments (drift + volatility) |
| 5 | `exp()` | Convert to lognormal prices |
| 6 | `dt = 1/252` | Scale to real calendar time |

Each step adds complexity while building toward realistic financial simulation used in options pricing, risk management, and portfolio analysis!

```
```