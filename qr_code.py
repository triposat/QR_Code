import qrcode # pip install qrcode

# The version parameter is an integer from 1 to 40 that controls the size of the QR Code.
# The error_correction parameter controls the error correction used for the QR Code.
# ERROR_CORRECT_L: About 7% or less errors can be corrected.
qr = qrcode.QRCode(
    version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=40, border=1)

qr.add_data("https://github.com/Iamtripathisatyam/")
qr.make(fit=True)

# Fill the colors
img = qr.make_image(fill_color="white", back_color="black")
# Save tghe final image
img.save(r"C:\Users\Dell\Desktop\Final.png")
