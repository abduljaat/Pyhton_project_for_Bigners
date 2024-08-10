# import pip install qr code mmodule

import qrcode as qr
img= qr.make("https://www.linkedin.com/in/abdul-rahman-806781312/") # past your social url
img.save("Abdul Rahman_linkedin.png")



# Advanced QR code 

import qrcode 

from PIL import Image
import qrcode.constants

qr= qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10,border=5)
qr.add_data("https://www.youtube.com/@muhammadirfanmalik/playlists")
qr.make(fit=True)
img=qr.make_image(fill_color="pink",back_color="white")
img.save("youtube.png")


