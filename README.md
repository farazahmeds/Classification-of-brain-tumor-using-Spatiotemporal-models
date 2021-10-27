# Classification-of-brain-tumor-using-Spatiotemporal-models

Classifying tumours using such deep learning methods has made significant progress with the availability of open datasets with reliable annotations. 
Typically those methods
are either 3D models, which use 3D volumetric MRIs or even 2D models considering each slice separately. However, by
treating one spatial dimension separately or by considering the slices as a sequence of images over time, spatiotemporal
models can be employed as "spatiospatial" models for this task. These models have the capabilities of learning specific spatial
and temporal relationship, while reducing computational costs. This is an implementation of two spatiotemporal models, ResNet (2+1)D
and ResNet Mixed Convolution, to classify different types of brain tumours. 
<p align="center">
<img src="meta/nets.png" alt="Spatiotemporal models and Conv3D model" width="500"/>
</p>

##### Getting started: #####

Execute ```run.py```, you can change the hyperparameters and settings for your experiments by overriding them in ```config/confg.yaml``` file or overriding through command line example: ```python run.py training.batch_size=2``` 

##### Preprint: #####
[Soumick Chatterjee, Faraz Ahmed Nizamani, Andreas Nürnberger, and Oliver Speck, Classification of Brain Tumours in MR Images using Deep Spatiospatial Models](https://arxiv.org/pdf/2105.14071.pdf)

BibTeX:
```
@article{chatterjee2021classification,
  title={Classification of Brain Tumours in MR Images using Deep Spatiospatial Models},
  author={Chatterjee, Soumick and Nizamani, Faraz Ahmed and N{\"u}rnberger, Andreas and Speck, Oliver},
  journal={arXiv preprint arXiv:2105.14071},
  year={2021}
}
```

