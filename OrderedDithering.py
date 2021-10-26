from PIL import Image, ImageFilter
import numpy as np
from RGB2GrayScale import rgb_to_gray

dithering_table = []


def make_dither_table():
    """Creates a random dither table"""

    arr = np.arange(n * n)
    arr = np.random.permutation(arr)
    arr.reshape((n, n))
    for i in range(0, n):
        tmp = []
        for j in range(0, n):
            tmp.append(arr[j + i * n])
        dithering_table.append(tmp)

    print("Dithering table: ", dithering_table)


def dither(im):
    new_im = Image.new(mode='1', size=im.size)
    n = len(dithering_table)

    (x, y) = im.size
    for i in range(0, x):
        for j in range(0, y):
            if im.mode != 'L':
                return im
            color = im.getpixel((i, j))
            s = i % n
            t = j % n

            # scale = 1
            scale = 256 / (n * n)

            if color / scale > dithering_table[s][t]:
                new_im.putpixel((i, j), int(1))
            else:
                new_im.putpixel((i, j), int(0))

    return new_im


if __name__ == '__main__':
    file_name = "1.jpg"
    original_image = Image.open('test_data/input/' + file_name)

    print("Image Info: Format - Size - Mode")
    print(original_image.format, original_image.size, original_image.mode)

    print("Enter window size: ")
    n = int(input())

    gray_scale_image = rgb_to_gray(original_image)
    # gray_scale_image.show()
    # gray_scale_image.save('test_data/output/' + file_name.split(".")[0] + '_gs.jpg', quality=95)

    make_dither_table()
    dithered_image = dither(gray_scale_image)
    dithered_image.show()
    dithered_image.save('test_data/output/' + file_name.split(".")[0] + '_d.jpg', quality=95)
