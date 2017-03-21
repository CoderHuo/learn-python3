#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image,ImageFilter

__author__ = 'Mr.Huo'


def main():
    with Image.open('Tulips.jpg') as im_1:
        print(im_1)
        print('Original image size: %sx%s'%im_1.size)
        w,h = im_1.size
        #图像缩放
        im_1.thumbnail((w//2,h//2))
        im_1.save('thumbnail.jpg', 'jpeg')
        im_2 = im_1.filter(ImageFilter.BLUR)
        im_2.save('blur.jpg','jpeg')


if __name__ == '__main__':
    main()