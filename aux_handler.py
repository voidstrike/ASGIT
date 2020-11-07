import os
import argparse


def main(opt):
    src, tgt = opt.named, opt.target

    name_list = list()
    for item in os.listdir(src):
        # print(item)
        if item.endswith('.jpg'):
            name_list.append(item)
    name_list = sorted(name_list)
    # print(name_list)

    tag_list = list()
    for item in os.listdir(tgt):
        if item.endswith('.jpg'):
            tag_list.append(int(item.split('.')[0]))
    tag_list = sorted(tag_list)
    # print(tag_list)

    for _, (src_item, tgt_item) in enumerate(zip(name_list, tag_list)):
        src_path = os.path.join(tgt, '{}.jpg'.format(tgt_item))
        tgt_path = os.path.join(tgt, src_item)
        os.rename(src_path, tgt_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--named', default='/home/yulin/Desktop/ori_name/testA/', type=str, help='path to named images')
    parser.add_argument('--target', default='/home/yulin/Desktop/ori_name/test/', type=str, help='path to target images')

    conf = parser.parse_args()
    main(conf)
