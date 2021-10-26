from PIL import Image
import numpy as np


def rgb_to_gray(im):
    new_im = Image.new(mode='L', size=im.size)
    (x, y) = im.size
    for i in range(0, x):
        for j in range(0, y):
            if im.mode == 'RGB' or im.mode == 'YCbCr':
                (r, g, b) = im.getpixel((i, j))
            elif im.mode == 'RGBA' or im.mode == 'CMYK':
                (r, g, b, A) = im.getpixel((i, j))
            elif im.mode == 'L':
                return im
            calc_gray = (r * 0.299) + (0.587 * g) + (0.114 * b)
            calc_gray = np.floor(calc_gray)
            new_im.putpixel((i, j), int(calc_gray))
    return new_im


if __name__ == '__main__':
    im = Image.open('test_data/input/1.jpg')

    print("Image format: ", im.format)
    print("Image Size: ", im.size)
    print("Image Mode: ", im.mode)
    new_im1 = rgb_to_gray(im)
    new_im1.show()

    new_im1.save('test_data/output/1_gs.jpg', quality=95)
