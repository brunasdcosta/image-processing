import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
import os

directory = os.getcwd()
file_path = directory + '/imagem3.jpg'

# a. Transfira a foto para o computador e mostre-a
image = cv2.imread(file_path)
# cv2.imshow("Imagem 3", image)

# b. Analise as propriedades da foto, no que concerne sua dimensão e resolução
height, width = image.shape[:2]
print(f'Dimensão:\n{width} pixels de largura\n{height} pixels de altura')

resolution_x = 0
resolution_y = 0

# Abre a imagem
image_pil = Image.open(file_path)

# Pega os metadados da imagem, como no caso: JPG
exifdata = image_pil.getexif()

# Dentre as informações da imagem, faz uma busca nas lista para verificar a resolução horizontal e vertical e mostrar em tela
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

# c. Com base nas informações acima, estime as dimensões do pixel e o tamanho da imagem em polegadas
print(f'Dimensão do pixel:\n{round(1/resolution_x, 5)} de largura\n{round(1/resolution_y, 5)} de altura')

# Para obter a dimensão em polegadas, precisamos dividir a dimensão em pixels pelo valor do DPI correspondente.
width_in_inches = width/resolution_x
height_in_inches = height/resolution_y
print(f'Tamanho em polegadas:\n{round(float(width_in_inches), 2)} de largura\n{round(float(height_in_inches), 2)} de altura')

# cv2.waitKey(0) # Necessário para que a janela da imagem não feche imediatamente
# cv2.destroyAllWindows() # Fecha todas as janelas de imagens abertas