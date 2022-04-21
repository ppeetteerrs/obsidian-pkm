## Methodology
Currently, stage 1 StyleGAN is trained using the CheXpert dataset. This dataset consists of around 200k chest X-rays consisting of 14 different labels:
![[chexpert_labels.png]]

To verify that stage 2 works, we have to ensure that:
- Stage 1 StyleGAN is **capable** of generating CXR images with the intended pathology
- Find CT scans with the desired pathology and check that generated CXR actually contains the pathology (or even more details)

More details on each pathology:
- **Enlarged Cardiom**: not sure, to find out
- **Cardiomegaly**: Enlarged heart. Can diagnose in CXR
- **Lung Lesion, Lung Opactiy, Edema, Consolidation**: generic observations, not very valuable, need CT scan to diagnose more specific conditions
- **Pneumonia**: Pneumonia, not very certain in CXR
- **Atelectasis**: Lung collapse, not too sure in CXR
- **Pneumothorax**: Leaky lung, quite certain in CXR

So the plan is:
**Stage 1 StyleGAN Training**
- Select subset of CheXpert 

Ideas:
- StyleGAN increase higher resolution channels, reduce lower resolution channel

[[ESP32-C3#Documents]]
![](https://hit.yhype.me/github/profile?user_id=8547778)
https://github.com/rvignav/CT2Xray
