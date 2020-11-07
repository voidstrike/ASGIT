import os
import argparse

from PIL import Image


def main(opt):
    root = opt.in_dir
    out = opt.out_dir
    for filename in os.listdir(root):
        # print(filename)
        if filename.endswith(".jpg"):
            im = Image.open(root + filename)
            im = im.resize((256, 256))
            im.save(out + filename)
            continue
        else:
            continue
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_dir', type=str, required=True)
    parser.add_argument('--out_dir', type=str, required=True)
    opt = parser.parse_args()
    main(opt)
