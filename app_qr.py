import qrcode

# Data to encode
data = "https://maps.app.goo.gl/BZQFXpyR9gXngyx38?g_st=ic"

# Creating an instance of QRCode class
qr = qrcode.QRCode(version=1,
                   box_size=15,
                   border=5)

# Adding data to the instance 'qr'
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color='black',
                    back_color='white')

img.save('kien_qr.png')
