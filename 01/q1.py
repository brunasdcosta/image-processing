import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
from matplotlib import pyplot as plt # pip install matplotlib
import os

directory = os.getcwd()
file_path = directory + '/imagem1.jpg'

# a. Adiquira a imagem
image = cv2.imread(file_path)

# b. Mostre a imagem lida
# cv2.imshow("Imagem 1", image)

# c. Mostre e analise cada um dos diferentes planos de cor e seus histogramas

# d. Converta a imagem para níveis de cinza e mostre a imagem convertida
image_gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Imagem 1 - Niveis de cinza", image_gray_scale)

# e. Gere uma nova imagem que seja o negativo da imagem em níveis de cinza
image_gray_scale_invert = cv2.bitwise_not(image_gray_scale)

# f. Mostre o resultado
# cv2.imshow("Imagem 1 - Niveis de cinza e negativo", image_gray_scale_invert)

# g. Gere agora a imagem negativa (complementar) a imagem original em cores
image_invert = cv2.bitwise_not(image)

# h. Mostre o resultado
# cv2.imshow("Imagem 1 - Negativo", image_invert)

# i. Verifique as propriedades da imagem em termos de dimensão em pixels e resolução
height, width = image.shape[:2]
print(f'Dimensão:\n{width} pixels de largura\n{height} pixels de altura')

resolution_x = 0
resolution_y = 0

# Abre a imagem
image_pil = Image.open(file_path)

# Pega os metadados da imagem, como no caso: JPG
exifdata = image_pil.getexif()

for tag_id in exifdata: # Iterando sobre os metadados recuperados.
  tag = TAGS.get(tag_id, tag_id) # Necessário para acessar a tag de cada metadado.
  # Obtemos apenas a informação que desejamos. No caso, a resolução da imagem.
  if tag == 'XResolution':
    resolution_x = exifdata.get(tag_id) # Aqui, obtemos a resolução como uma tupla.
    resolution_x = resolution_x[0]/resolution_x[1] # Para obter a resolução de forma certa, dividimos o primeiro elemento pelo segundo da tupla.
  if tag == 'YResolution':
    resolution_y = exifdata.get(tag_id) # Mesmo caso explicado antes apra a tupla.
    resolution_y = resolution_y[0]/resolution_y[1] # Calculando a resolução.
print(f'Resolução:\nX: {resolution_x}\nY: {resolution_y}')

# j. Calcule o tamanho (dimensão em polegadas) da imagem

# Para obter a dimensão em polegadas, precisamos dividir a dimensão em pixels pelo valor do DPI correspondente.
width_in_inches = width/resolution_x # Calculando a largura da imagem em polegadas.
height_in_inches = height/resolution_y # Calculando a altura da imagem em polegadas.
print(f'Dimensão em polegadas:\n{round(float(width_in_inches),2)} de largura\n{round(float(height_in_inches),2)} de altura')

# k. Verifique o formato do arquivo e calcule o índice de compressão aplicado

# cv2.waitKey(0) # Necessário para que a janela da imagem não feche imediatamente
# cv2.destroyAllWindows() # Fecha todas as janelas de imagens abertas