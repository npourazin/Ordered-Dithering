<div id="top"></div>

# Ordered Dithering Project

In this project, we use an ordered dithering method to turn an RGB image, first to a gray scale image and then, turn the gray scale image into a dithered image.

## About The Project

Ordered dithering is an image dithering algorithm. It is commonly used to display a continuous image on a display of smaller color depth. For example, Microsoft Windows uses it in 16-color graphics modes. The algorithm is characterized by noticeable crosshatch patterns in the result. ([source](https://en.wikipedia.org/wiki/Ordered_dithering))

<p align="right">(<a href="#top">back to top</a>)</p>


## Getting Started

### Prerequisites

As mentioned in [`requirements`](requirements.txt) file, [Numpy](https://numpy.org/) and [Pillow](https://python-pillow.org/) Libraries are to be installed in order to run this project. 

### How To Run

First, create a "test_data" in thr root directory. Then, add two folders in itn named "input" and "output". in the input folder, add any image. to run the code by default, your desired input must be named 1.jpg. (to change this, you may change the values to the filename variable which is hardcoded, making it "*Filename*.jpg" for example)

After this, you can run [`RGB2GrayScale`](RGB2GrayScale.py) file to get the gray scale image, both shown and also saved in the output folder under the name of "*Filename*_gs.jpg".

For Dithering, you can run the [`OrderedDithering`](OrderedDithering.py) File, give the sliding window size as a console input and get the dithered image both as a shown output and saved as "*Filename*_d.jpg".

<p align="right">(<a href="#top">back to top</a>)</p>

## Project Results Example

**The Original Image:**

![IMAGE NOT FOUND](Examples/original_image.jpg?raw=true "Original Image")



**The GrayScale Image:**

![IMAGE NOT FOUND](Examples/grayscale_image.jpg?raw=true "GrayScale Image")



**The Dithered Image:**

![IMAGE NOT FOUND](Examples/dithered_image.jpg?raw=true "Original Image")


<p align="right">(<a href="#top">back to top</a>)</p>


<!-- LICENSE -->
## License

Distributed under the MIT License. See [`LICENSE.md`](LICENSE.md) for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Niki Pourazin - [@npourazin](https://github.com/npourazin) - npourazin@aut.ac.ir

Project Link: [https://github.com/npourazin/Ordered-Dithering](https://github.com/npourazin/Ordered-Dithering)

<p align="right">(<a href="#top">back to top</a>)</p>
