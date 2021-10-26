# Ordered Dithering Project

In this project, we use an ordered dithering method to turn an RGB image, first to a gray scale image and then, turn the gray scale image into a dithered image.

## How to run

First, create a "test_data" in thr root directory. Then, add two folders in itn named "input" and "output". in the input folder, add any image. to run the code by default, your desired input must be named 1.jpg. (to change this, you may change the values to the filename variable which is hardcoded, making it "*Filename*.jpg" for example)

After this, you can run [RGB2GrayScale](RGB2GrayScale.py) file to get the gray scale image, both shown and also saved in the output folder under the name of "*Filename*_gs.jpg".

For Dithering, you can run the [OrderedDithering](OrderedDithering.py) File, give the sliding window size as a console input and get the dithered image both as a shown output and saved as "*Filename*_d.jpg".
