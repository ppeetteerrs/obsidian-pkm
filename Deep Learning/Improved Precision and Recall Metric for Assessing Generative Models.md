# Concepts
1. Precision and Recall
![[GAN Precision and Recall.png]]
	- [Assessing Generative Models via Precision and Recall](https://arxiv.org/pdf/1806.00035.pdf) (2018)
	- Cannot estimate extrema due to reliance on relative probability densities (e.g. cannot interpret high density regions by mode collapse / truncation correctly)
2. [Revisiting Classifier Two-Sample Tests](https://arxiv.org/pdf/1610.06545.pdf) (2017)
	- Use binary classifier (DNN, or just KNN) to perform two-sample test / evaluate distribution between generated and real data distributions
	- Also cannot deal with mode collapse
3. Approximating Manifold using k nearest neighbours
![[GAN knn manifold approximation.png]]
![[knn precision recall.png]]
4. Pareto frontiers
	- Do not make assumptions / explicit preference in multi-objective optimization (precision vs recall) [[Multiobjective Optimization]]
	- Using snapshots during training

# Results
## StyleGAN alterations (black dots are lowest FID)
![[stylegan precision recall.png]]
A: original StyleGAN1
B: no minibatch std -> less variation
C: also less R1 discriminator regularization -> less variation
D: no progressive growing -> hurts FID
E: randomly translates output image before passing to discriminator -> better precision
F: no instance normalization -> more variety and better FID (lol somehow, but style mixing probably does not work)

## Realism score
![[stylegan realism score.png]]
truncation performed by only retraining hyperspheres with radii below median to perform over-conservative estimate (pruning prevents having very wrong scores for generated samples that fall in underrepresented samples where radii are overly loose)

R >= 1 means generated sample falls in real distribution

## Evaluate Interpolations
Do linear interpolation on StyleGAN latent space and investigate realism score