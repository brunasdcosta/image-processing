import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS

file_path = '/home/bruna/workspace/image-processing/01/imagem3.jpg'

# a. Transfira a foto para o computador e mostre-a
image = cv2.imread(file_path)
# cv2.imshow("Imagem 3", image)

# b. Analise as propriedades da foto, no que concerne sua dimensão e resolução
height, width = image.shape[:2]
print(f'Dimensão:\n{width} pixels de largura\n{height} pixels de altura')

resolution_x = 0
resolution_y = 0

image_pil = Image.open(file_path)
exifdata = image_pil.getexif()
for tag_id in exifdata:
	tag = TAGS.get(tag_id, tag_id)	
	if tag=='XResolution':
		resolution_x = exifdata.get(tag_id)
		if isinstance(resolution_x, bytes):
			resolution_x = resolution_x.decode()
	if tag=='YResolution':
		resolution_y = exifdata.get(tag_id)
		if isinstance(resolution_y, bytes):
			resolution_y = resolution_y.decode()
if resolution_x!=0 and resolution_y!=0:
	print(f'Resolução X:{resolution_x}\nResolução Y:{resolution_y}')

# c. Com base nas informações acima, estime as dimensões do pixel e o tamanho da imagem em polegadas
print(f'Dimensão do pixel: 1/{resolution_x}x1/{resolution_y}')
result = width/resolution_x
result_ = height/resolution_y
print(f'Tamanho em polegadas: {round(float(result),2)}x{round(float(result_),2)}')
# cv2.waitKey(0) # Necessário para que a janela da imagem não feche imediatamente
# cv2.destroyAllWindows() # Fecha todas as janelas de imagens abertas