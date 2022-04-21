# Introduction
Equalized Learning Rate is a concept introduced in [[ProGAN]].

> We deviate from the current trend of careful weight initialization, and instead use a trivial N(0, 1) initialization and then explicitly scale the weights at runtime. To be precise, we set wˆi = wi/c, where wi are the weights and c is the per-layer normalization constant from He’s initializer (He et al., 2015). The benefit of doing this dynamically instead of during initialization is somewhat subtle, and relates to the scale-invariance in commonly used adaptive stochastic gradient descent methods such as RMSProp (Tieleman & Hinton, 2012) and Adam (Kingma & Ba, 2015). These methods normalize a gradient update by its estimated standard deviation, thus making the update independent of the scale of the parameter. As a result, if some parameters have a larger dynamic range than others, they will take longer to adjust. This is a scenario modern initializers cause, and thus it is possible that a learning rate is both too large and too small at the same time. Our approach ensures that the dynamic range, and thus the learning speed, is the same for all weights. A similar reasoning was independently used by van Laarhoven (2017).

Modern optimizers such as the [[Deep Learning/Adam]] optimzer limit gradient update step sizes. However, in GANs, different parameters have vastly different dynamic ranges (i.e. the range of values). In order to equalize the learning rate between different parameters, we divide the parameters by its fan-in (i.e. estimated standard deviation) during runtime.

![[Deep Learning/Adam#Update rule]]

[*Reference video*](https://www.youtube.com/watch?v=XwUTJhKRVl8&feature=emb_title)

Note that StyleGAN2 code ignored the root 2 factor in their scaling factor because it was cancelled with the subsequent summing with bias term. Smart pants.