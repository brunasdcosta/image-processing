import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np
import imageio
import os




############### 5.a
# Utilizando o gradiente morfológico que consiste na diferença entre dilatação e erosão de uma imagem, teremos o resultado semelhante ao contorno do objeto.
# img = cv2.imread('imagem4.jpg', 0)
kernel = np.ones((5,5),np.uint8)
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

# Image.fromarray(np.uint8(gradient)).save('img_morphological_gradient.jpg')


############### 5.b
# Utilizando a operação morfológica de dilatação conseguiremos aumentar as bordas das imagens.
img_gradient = cv2.imread('img_morphological_gradient.jpg')
dilation = cv2.dilate(img_gradient,kernel,iterations = 1)
Image.fromarray(np.uint8(dilation)).save('img_morphological_dilation.jpg')
