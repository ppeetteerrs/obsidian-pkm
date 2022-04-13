## CycleGAN Loss Function

$$\mathcal{L_{cyc}}(G,F) = \mathbb{E_{x \sim p_{data}(x)}} [\Vert F(G(x)) - x\Vert_1] + \mathbb{E_{y \sim p_{data}(y)}}[\Vert G(F(y)) - y\Vert_1]$$
