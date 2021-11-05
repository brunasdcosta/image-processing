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
for tag_id in exifdata:
	tag = TAGS.get(tag_id, tag_id)	
	if tag == 'XResolution':
		resolution_x = exifdata.get(tag_id)
		if isinstance(resolution_x, bytes):
			resolution_x = resolution_x.decode()
	if tag == 'YResolution':
		resolution_y = exifdata.get(tag_id)
		if isinstance(resolution_y, bytes):
			resolution_y = resolution_y.decode()
if resolution_x != 0 and resolution_y != 0:
	print(f'Resolução X: {resolution_x[0]}\nResolução Y: {resolution_y[0]}')

# c. Com base nas informações acima, estime as dimensões do pixel e o tamanho da imagem em polegadas
print(f'Dimensão do pixel: 1/{resolution_x[0]} x 1/{resolution_y[0]}')
result = width/resolution_x[0]
result_ = height/resolution_y[0]
print(f'Tamanho em polegadas: {round(float(result),2)}x{round(float(result_),2)}')
# cv2.waitKey(0) # Necessário para que a janela da imagem não feche imediatamente
# cv2.destroyAllWindows() # Fecha todas as janelas de imagens abertas