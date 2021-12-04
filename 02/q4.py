import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np


############### 4.b
# imagem_3 = Image.open('imagem3.jpg')
# imagem3_histogram = imagem3.histogram()
# plt.hist(imagem2_histogram, 256, (0, 256))
# plt.show()

############### 4.c
# light = cv2.imread("imagem3.jpg", 0)
# print("Luminância do pixel mais escuro:", min(light.flatten()))

# dark = cv2.imread("imagem3.jpg", 255)
# print("Luminância do pixel mais claro:", min(dark.flatten()))

############### 4.e
# imagem3 = np.array(Image.open('imagem3.jpg'))

# thresh = 128

# maxval = 255

# im_bin = (imagem3 > thresh) * maxval

# print(im_bin)

# Image.fromarray(np.uint8(im_bin)).save('img_binarization.jpg')

############### 4.f
imagem3 = np.array(Image.open('imagem3.jpg'))
imagem3_bin = np.array(Image.open('img_binarization.jpg'))


imagem_3 = cv2.cvtColor(imagem3, cv2.COLOR_BGR2GRAY)

imagem_bin = cv2.cvtColor(imagem3_bin, cv2.COLOR_BGR2GRAY)

contrast_img3 = imagem_3.std()

contrast_img_bin = imagem_bin.std()

print("Contraste da Imagem origial: ", contrast_img3)
print("Contraste da Imagem binarizada: ", contrast_img_bin)
print("É possível perceber que o constraste da imagem binarizada é maior. Porém, isso não necessariamente diz que a imagem tem melhor qualidade. Nesse caso é o oposto disso.")