import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
from matplotlib import pyplot as plt # pip install matplotlib

file_path = '/home/bruna/workspace/image-processing/01/imagem1.jpg'

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

# j. Calcule o tamanho (dimensão em polegadas) da imagem

result = width/resolution_x
result_ = height/resolution_y
print(f'Dimensão em polegadas: {round(float(result),2)}x{round(float(result_),2)}')

# k. Verifique o formato do arquivo e calcule o índice de compressão aplicado

# cv2.waitKey(0) # Necessário para que a janela da imagem não feche imediatamente
# cv2.destroyAllWindows() # Fecha todas as janelas de imagens abertas