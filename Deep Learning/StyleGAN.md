Concepts:
[[Equalized Learning Rate]]
[[Weight Initialization]]


Reference:
- Not used in StyleGAN2 paper: [[GAN Quality Metrics]] 
- [[Improved Precision and Recall Metric for Assessing Generative Models]] (StyleGAN2)
> If we were willing to sacrifice scale-specific controls (see video), we could simply remove the normalization, thus removing the artifacts and also improving FID slightly
- Weight Normalization (StyleGAN2)
	- [On the Effects of Batch and Weight Normalization in Generative Adversarial Networks](https://arxiv.org/pdf/1704.03971.pdf)
	- [Weight Normalization: A Simple Reparameterization to Accelerate Training of Deep Neural Networks](https://arxiv.org/pdf/1602.07868.pdf)
>    Our demodulation is also related to weight normalization [37] that performs the same calculation as a part of  reparameterizing the weight tensor. Prior work has identified weight normalization as beneficial in the context of  GAN training [43].

- Trainig
	- https://github.com/l4rz/practical-aspects-of-stylegan2-training