---
aliases: [Adaptive Moment Estimation]
---
# Introduction
Adam (Adaptive Moment Estimation) is an adaptive learning rate optimization algorithm published in [ICLR 2015](https://arxiv.org/pdf/1412.6980.pdf). It combines the concepts behind [RMSProp](RMSProp) and [SGD with momentum](SGD%20with%20momentum).

# Maths
## Moving averages
$m_t$ is moving average of gradient
$v_t$ is moving average of squared gradient (i.e. uncentered variance)
$\beta_1$ and $\beta_2$ are set to 0.9 and 0.999. No one ever changes them.
$$
\begin{align}
m_t &= \beta_1m_{t-1} + (1-\beta_1)g_t \\
v_t &= \beta_2v_{t-1} + (1-\beta_2)g_t^2
\end{align}
$$
## Update rule
We set the quantities $\hat{m_t}$ and  $\hat{v_t}$ as follows:
$$
\begin{align}
\hat{m_t} &= \frac{\hat{m_t}}{1-\beta_1^t} \\
\hat{v_t} &= \frac{\hat{v_t}}{1-\beta_2^t}
\end{align}
$$

such that:

$$
\begin{align}
E[\hat{m_t}] &= E[g_t] \\
E[\hat{v_t}] &= E[g_t^2]
\end{align}
$$

So the gradient update rule becomes:
$$
w_t = w_{t-1} - \eta \frac{\hat{m_t}}{\sqrt{\hat{v_t}} + \epsilon}
$$

## Consequences
1. Learning rate is limited to between 0 and $\eta$ (by [Cauchy–Schwarz Inequality](Cauchy%E2%80%93Schwarz%20Inequality.md))
2. Smaller variance (e.g. all values near mean) means higher update step

## Design Choices
*Why is the uncentered variance used?*
- We do not have access to the mean global gradient (across all batches / timesteps) but we can safely assume it to be zero.
- The variance has the same expectation as the uncentered variance of the global variance (or centered assuming 0 mean gradient)