# Attention-Based Spatial Guidance for Image-to-Image Translation

This repo contains the PyTorch implementation of ["Attention-Based Spatial Guidance for Image-to-Image Translation"](https://openaccess.thecvf.com/content/WACV2021/papers/Lin_Attention-Based_Spatial_Guidance_for_Image-to-Image_Translation_WACV_2021_paper.pdf) (WACV 2021).\
This implementation is based on the official [CycleGAN](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix) code.\
Our model and contributions are in `./models/attn_cycle_gan_model.py` and  `./models/attn_cycle_gan_v2_model.py`, respectively.

<img src='imgs/motivation.png'>
<img src='imgs/settings.png'>

## Getting Started
### Installation

- Clone this repo:
```
git clone https://github.com/voidstrike/ASGIT
```

- Install the requirements based on the official CycleGAN repo (Visdom and Dominate). You can install all of them by one command:
```
pip install -r requirements.txt
```

For CONDA users, you can use script `./scripts/conda_dep.sh` to install pytorch and other libraries (NOT tested)

### Download Datasets

Cityscapes dataset can be downloaded from [Cityscapes](https://www.cityscapes-dataset.com). You must register an account to access and download the dataset.

ImageNet based datasets like apple2orange, horse2zebra and *.etc* can be downloaded using `./scripts/download_cyclegan_model.sh`.

Day2Night dataset can be downloaded from [here](https://drive.google.com/file/d/1lU3Tmzkhp3TOeosZGpjNMGkrWNdtrjHa/view?usp=sharing). Please note that those street images are cropped from [BDD100K](https://bair.berkeley.edu/blog/2018/05/30/bdd/) dataset.

### Run Experiments

- Train a model (The following commands are used for PHA+RHP, PHA+Alpha, TAM+RHP, TAM+Alpha, respectively)
```
python3 train_attn.py --netG resnet_9blocks --netD posthoc_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH --name EXP_NAME
python3 train_attn.py --netG resnet_9blocks --netD posthoc_attn_v2 --model attn_cycle_gan_v2 --concat alpha --dataroot DATASETPATH --name EXP_NAME
python3 train_attn.py --netG resnet_9blocks --netD trainable_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH --name EXP_NAME
python3 train_attn.py --netG resnet_9blocks --netD trainable_attn_v2 --model attn_cycle_gan_v2 --concate alpha --dataroot DATASETPATH --name EXP_NAME
```
- There are more hyper parameter options, please refer to the source code for more detail.
- Please modify DATASETPATH and EXP_NAME accordingly.
- To view training results and log plots, please run `python -m visdom.server` and go to URL http://localhost:8097.
- To see more intermediate results, check out `./checkpoints/EXP_NAME/web/index.html`

- Test a model (Please make sure --netG, --netD, --model and --concat are consistent with the training command)
```
python3 test.py --netG resnet_9blocks --netD posthoc_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH
python3 test.py --netG resnet_9blocks --netD posthoc_attn_v2 --model attn_cycle_gan_v2 --concat alpha --dataroot DATASETPATH
python3 test.py --netG resnet_9blocks --netD trainable_attn --model attn_cycle_gan --concat rmult --dataroot DATASETPATH
python3 test.py --netG resnet_9blocks --netD trainable_attn_v2 --model attn_cycle_gan_v2 --concate alpha --dataroot DATASETPATH
```

## Results
We provide some translation results of our model.

### SCENERY 
<img src='imgs/scene.png'>

### OBJECT
<img src='imgs/object.png'>

## Citation

If you use this code or dataset for your research, please consider cite our paper:

```
@InProceedings{Lin_2021_WACV,
    author    = {Lin, Yu and Wang, Yigong and Li, Yifan and Gao, Yang and Wang, Zhuoyi and Khan, Latifur},
    title     = {Attention-Based Spatial Guidance for Image-to-Image Translation},
    booktitle = {Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)},
    month     = {January},
    year      = {2021},
    pages     = {816-825}
}
```

## Update
### 2021-06-03
- For parameter `--netD`, a specified network without suffix `_v2` (e.g. `posthoc_attn`) means the attention mask will be normalized into [0, 1]. Thus, a model name w/ and w/o the `_v2` suffix are exchangable;
- There is a missing parameter: please adjust `--mask_size IMG_SIZE` to the shape of your input;
- If your dataset has more than 3000 images, please adjust L57 of `attn_cycle_gan_model.py` accordingly


