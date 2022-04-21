The pSp model uses a [ResNet](https://arxiv.org/pdf/1610.02915.pdf) backbone to construct a feature pyramid which would then pass through a series of mapping CNNs to generate latent vectors in the w+ space.

The ResNet backbone used in the pSp model is a mess (seriously can't people just clean up their own code before they publish a paper??!). The pSp ResNet implementation is copied (without modification) from a [guy](https://github.com/TreB1eN/InsightFace_Pytorch)''s implementation of the [Arcface](https://openaccess.thecvf.com/content_CVPR_2019/papers/Deng_ArcFace_Additive_Angular_Margin_Loss_for_Deep_Face_Recognition_CVPR_2019_paper.pdf) ResNet. But that funny guy apparently did not follow the original [implementation](https://github.com/deepinsight/insightface/blob/master/recognition/arcface_mxnet/symbol/fresnet.py) of the Arcface paper (in MXNet, another regrettable life decision I guess). And that TreB1eN guy did not bother to explain the differences (I would guess its more like an uncorrected mistake) as seen [here](https://github.com/TreB1eN/InsightFace_Pytorch/issues/37).

Shortcut of maxpool taken from here? (https://arxiv.org/pdf/2004.04989.pdf)

pSp => ArcFace => CosFace => SphereFace
(interesting, maybe this embedding can be used to detect different CXR identities?)

See SphereFace Table 2 (https://arxiv.org/pdf/1704.08063.pdf). That's where the CNN architecture was taken from (i.e. different from native ResNet), not using bottleneck. All different implementations shown here (https://github.com/ronghuaiyang/arcface-pytorch/blob/master/models/resnet.py), ResNet 34 (no bottleneck) vs ResNet 50+ (bottlenect) vs Face-ResNet (no-bottleneck, PReLU). Not sure where the PReLU came from (came from SpherFace).

From SphereFace github (https://github.com/wy1iu/sphereface/search?p=2&q=prelu):
In SphereFace, our network architecures use residual units as building blocks, but are quite different from the standrad ResNets (e.g., BatchNorm is not used, the prelu replaces the relu, different initializations, etc). We proposed 4-layer, 20-layer, 36-layer and 64-layer architectures for face recognition (details can be found in the [paper]

[3, 4, 14, 3] came from ArcFace MXNet https://github.com/deepinsight/insightface/blob/8b79096e70a10a4899f1ce59882ea4d56e634d40/recognition/arcface_mxnet/symbol/fresnet.py#L1175, which did not follow here https://github.com/tornadomeet/ResNet/blob/master/train_resnet.py. Oh, cuz original ResNet has 3-layer bottleneck for ResNet50 onwards, so [3, 4, 6, 3] means 50 layers. But ArcFace uses 2-layer block without bottlenect, so need [3, 4, 14, 3] following the convention (with reason?) to put more layers in conv4_x

So, I guess I will implement my own ResNet...

![[evolution of deep cnn.png]]

![[evolution of deep cnn 2.png]]
![[evolution of deep cnn 3.png]]

![[evolution of deep cnn 4.png]]

CNN Techniques and Architectural Breakthroughs
- https://arxiv.org/ftp/arxiv/papers/1901/1901.06032.pdf
- https://towardsdatascience.com/from-lenet-to-efficientnet-the-evolution-of-cnns-3a57eb34672f
- https://medium.com/@neuralnets/swish-activation-function-by-google-53e1ea86f820
- https://www.aismartz.com/blog/cnn-architectures/
- https://theaisummer.com/cnn-architectures/
- https://analyticsindiamag.com/how-the-deep-learning-approach-for-object-detection-evolved-over-the-years/
- 