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


if __name__ == '__main__':
    file_name = "1.jpg"
    original_image = Image.open('test_data/input/' + file_name)

    print("Image Info: Format - Size - Mode")
    print(original_image.format, original_image.size, original_image.mode)

    print("Enter window size: ")
    n = int(input())

    # gray_scale_image = rgb_to_gray(original_image)
    # gray_scale_image.show()
    # gray_scale_image.save('test_data/output/' + file_name.split(".")[0] + '_gs.jpg', quality=95)

