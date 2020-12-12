# Attention-Based Spatial Guidance for Image-to-Image Translation

This repo contains the PyTorch implementation of ["Attention-Based Spatial Guidance for Image-to-Image Translation"]() (WACV 2021).
The implementation is based on the official [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) code.
Our model and contribution are in `./models/attn_cycle_gan_model.py`, `./models/attn_cycle_gan_v2_model.py`

<img src='imgs/motivation.png'>
<img src='imgs/settings.png'>

## Getting Started
### Installation

- Clone this repo:
```
git clone https://github.com/voidstrike/ASGIT
```

- Install requirement based on the official CycleGAN repo (Visdom and Dominate). You can install all of them by one command:
```
pip install -r requirements.txt
```

For CONDA users, you can use script `./scripts/conda_dep.sh` to install pytorch and other libraries (NOT tested)

### Download Datasets

Cityscapes dataset can be downloaded from [Cityscapes](https://www.cityscapes-dataset.com). You must register an account to access and download the dataset.

ImageNet based datasets like apple2orange, horse2zebra, etc can be downloaded using `./scripts/download_cyclegan_model.sh`

Day2Night dataset can be downloaded from [Day2Night](https://drive.google.com/file/d/1lU3Tmzkhp3TOeosZGpjNMGkrWNdtrjHa/view?usp=sharing). Noted that those street images are cropped from [BDD100K](https://bair.berkeley.edu/blog/2018/05/30/bdd/) dataset

### Run Experiments

- Train a model (The following commands are for PHA+RHP, PHA+Alpha, TAM+RHP, TAM+Alpha)
```
python3 train_attn.py --netG resnet_9blocks --netD posthoc_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH
python3 train_attn.py --netG resnet_9blocks --netD posthoc_attn_v2 --model attn_cycle_gan_v2 --concat alpha --dataroot DATASETPATH
python3 train_attn.py --netG resnet_9blocks --netD trainable_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH
python3 train_attn.py --netG resnet_9blocks --netD trainable_attn_v2 --model attn_cycle_gan_v2 --concate alpha --dataroot DATASETPATH
```
- There are more hyper parameter options, please refer to the source code for more detail.
- To view training results and and log plots, please run `python -m visdom.server` and go to URL http://localhost:8097.
- To see more intermediate results, check out `./checkpoints/NAME/web/index.html`

- Test a model (Please make sure --netG, --netD, --model and --concat are consistent with the training command)
```
python3 test.py --netG resnet_9blocks --netD posthoc_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH
python3 test.py --netG resnet_9blocks --netD posthoc_attn_v2 --model attn_cycle_gan_v2 --concat alpha --dataroot DATASETPATH
python3 test.py --netG resnet_9blocks --netD trainable_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH
python3 test.py --netG resnet_9blocks --netD trainable_attn_v2 --model attn_cycle_gan_v2 --concate alpha --dataroot DATASETPATH
```

### Results
We provide some translation results of our model.

### SCENERY 
<img src='imgs/scene.png'>

### OBJECT
<img src='imgs/object.png'>

### Citation

If you use this code or dataset for your research, please cite our paper:

PENDING.



