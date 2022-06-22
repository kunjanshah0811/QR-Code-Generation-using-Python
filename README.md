# QR-Code-Generation-using-Python
QR code stands for Quick Response Code. QR codes may look simple but they are capable of storing lots of data. Irrespective of how much data they contain when scanned QR code allows the user to access information instantly. That is why they are called Quick Response Code.

These are being used in many scenarios these days. It first appeared in Japan in 1994. QR codes can be used to store(encode) lots of data and that too of various types. For example, they can be used to encode:

Contact details
Facebook ids, Instagram ids, Twitter ids, WhatsApp ids, and more.
Event Details
Youtube links
Product details
Link directly to download an app on the Apple App Store or Google Play.
They are also being used in doing digital transactions by simply scanning QR codes.
Access Wi-Fi by storing encryption details such as SSID, password, and encryption type.

This article was published as a part of the Data Science Blogathon
Introduction
Beginners when start programming often get bored if they do not get a chance to play with some interesting code. So, in this article, I have explained three python projects with Code. Beginner programmers can try to implement these projects and get their hands dirty in the Python language.

Let’s start with the first one.

1. QR Code Generation using Python
QR code stands for Quick Response Code. QR codes may look simple but they are capable of storing lots of data. Irrespective of how much data they contain when scanned QR code allows the user to access information instantly. That is why they are called Quick Response Code.

These are being used in many scenarios these days. It first appeared in Japan in 1994. QR codes can be used to store(encode) lots of data and that too of various types. For example, they can be used to encode:

Contact details
Facebook ids, Instagram ids, Twitter ids, WhatsApp ids, and more.
Event Details
Youtube links
Product details
Link directly to download an app on the Apple App Store or Google Play.
They are also being used in doing digital transactions by simply scanning QR codes.
Access Wi-Fi by storing encryption details such as SSID, password, and encryption type.
This list goes on….!



We just saw some advantages of QR codes. Now we will learn here how we can generate QR codes in Python.

For QR code generation using python, we are going to use a python module called QRcode.

Link: https://pypi.org/project/qrcode/

Install it using this command: pip install qrcode

We will generate a QR Code for encoding the youtube link and we will also explore more. QR code generation is simple. Just pass the text, link, or any content to ‘make’ function of QRcode module.


You can see it’s just 3 lines of code to generate this QR Code. One more thing to mention is that it’s not necessary that you always have to give a link to qrcode.make() function. You can provide simple text also.

So this is the one part, which involves generating a QR Code and scanning it. But what if we want to read this QR Code i.e., now we want to know what was encoded in the QR Code without scanning it. For this, we will use OpenCV. OpenCV is a library of programming functions focused on real-time computer vision tasks.

Install opencv: pip install opencv-python

Code to decode a QR code back to know the original string.
