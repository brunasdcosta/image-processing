import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
import matplotlib.pyplot as plt # pip install matplotlib
import numpy as np
import imageio
import os



img_orig = cv2.imread("imagem5.jpg")

############### 6.a
# Aqui vamos ler uma imagem e aplicar o desfoque gaussiano à imagem usando a função cv2.GaussianBlur().
img = cv2.imread("imagem5.jpg",  cv2.IMREAD_GRAYSCALE)
dst = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)

Image.fromarray(np.uint8(dst)).save('img_denoise.jpg')

############### 6.b


cv2.imshow("Imagem5 - Original", img_orig)
cv2.imshow("Imagem5 - Com Filtro Gaussiano Aplicado", dst)

print('Utilizamos do Filtro Gaussiano que consiste em um filtro capaz de reduzir o nível de ruído de um sinal de entrada, a fim de diminuir a distorção numa imagem')
print('Desta forma, é possível notar que os ruídos na imagem tratada pelo desfoque gaussiano foi bastante melhorado em relação à original.')
print('Em contra partida, temos o desfoque da imagem, apenas do melhoramento dos ruídos.')
cv2.waitKey(0)
cv2.destroyAllWindows()