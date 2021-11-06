import cv2 # pip install opencv-python
from PIL import Image # pip install pillow
from PIL.ExifTags import TAGS
import os

# pip install -U get-video-properties
# caso haja erro: sudo apt install ffmpeg
from videoprops import get_video_properties 
from videoprops import get_audio_properties

# os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"

directory = os.getcwd()
file_path = directory + '/video.mp4'

# a. Transfira o filme para seu computador e apresente-o.
load_video = cv2.VideoCapture(file_path)
ret_value, frame = load_video.read()

# while(1):
#    ret_value, frame = load_video.read()
#    cv2.imshow('frame',frame)
#    if cv2.waitKey(1) & 0xFF == ord('q') or ret_value == False :
#        load_video.release()
#        cv2.destroyAllWindows()
#        break
#    cv2.imshow('Vídeo',frame)

# b. Analise as propriedades do filme no que concerne a taxa de captura das imagens e do som.

fps = load_video.get(cv2.CAP_PROP_FPS)
props = get_audio_properties('video.mp4')

print ("Taxa de captura de imagem por segundo: {0}".format(fps))
print(f'''Taxa de amostragem de som: {props['sample_rate']}''')

load_video.release()

# c. Analise as propriedades do filme, no que concerne a dimensão e resolução de cada quadro.
props = get_video_properties('video.mp4')

print(f'''
Resolução: {props['width']}×{props['height']}
Proporção da tela: {props['display_aspect_ratio']}
Taxa de quadros: {props['avg_frame_rate']}
''')

