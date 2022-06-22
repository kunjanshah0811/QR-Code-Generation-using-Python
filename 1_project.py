import qrcode
img = qrcode.make("India is a country with many religions. I love India.")
img.save("youtubeQR.jpg")

import cv2
d = cv2.QRCodeDetector()
val,_,_ = d.detectAndDecode(cv2.imread("youtubeQR.jpg"))
print("Decoded text is: ", val)