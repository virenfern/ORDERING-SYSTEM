import qrcode
url = "https://drive.google.com/file/d/1l2vO5Fyt0bbRHX94vFV3jsF-ft1vvWzT/view?usp=sharing"
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
