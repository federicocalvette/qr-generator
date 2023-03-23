import qrcode
from PIL import Image

IMAGENLOGO = r'./img/logo.jpg' # Path del logo
URL = 'https://www.youtube.com/channel/UChSfyFn6Ev4bm_yl7R7h2eg' #URL del QR
QR_COLOR = '#000000' # Color principal 
QR_COLOR_FONDO = '#ffffff' # Color del fondo
PATH_SAVE_QR = r'./QR/QR.png' # Path donde guardaremos el QR generado

logo = Image.open(IMAGENLOGO)

# Tamaño de la imagen que vamos a colocar en nuestro QR
hsize = int((float(logo.size[1])*float(100/float(logo.size[0]))))
logo = logo.resize((100, hsize), Image.ANTIALIAS)

# Creamos el objeto del QR
QRcode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

# Cargamos la info de la URL en el QR
QRcode.add_data(URL)
QRcode.make # Creamos el QR basico


# Agregamos nuestra imagen al QR
QRimg = QRcode.make_image(fill_color=QR_COLOR, back_color=QR_COLOR_FONDO).convert('RGB')

#Establecemos la posicion de la imagen en el centro.
position_logo = ((QRimg.size[0] - logo.size[0]) // 2,(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, position_logo)

# Guardamos la imagen de nuestro código QR en el directorio definido
QRimg.save(PATH_SAVE_QR)