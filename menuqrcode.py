import qrcode
url = "https://drive.google.com/file/d/1uBbG8HaQsohAXfh9mNO2hT7n1f7s0A5f/view?usp=sharing"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill='black', back_color='white')
img.save("google_drive_qr_code.png")
img.show()
