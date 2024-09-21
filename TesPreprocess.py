import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

citra = cv.imread('D://.Kuliah Raihan M//SEMESTER 3//Pengolahan Citra//Project Pisang UAS//Pisang Resize//Pisang-1.jpg') #Membaca citra

b, g, r = cv.split(citra)

# Ekualisasi histogram pada setiap saluran warna
b_eq = cv.equalizeHist(b)
g_eq = cv.equalizeHist(g)
r_eq = cv.equalizeHist(r)

# Menggabungkan saluran warna yang telah diekualisasi
citra_eq = cv.merge([b_eq, g_eq, r_eq])

cv.imshow("Asli", citra)
cv.imshow("Ekualisasi", citra_eq)

# Menyimpan gambar hasil ekualisasi
cv.imwrite('D://.Kuliah Raihan M//SEMESTER 3//Pengolahan Citra//Project Pisang UAS//Pisang Resize//Pisang-1_eq.jpg', citra_eq)

plt.figure(figsize=(10, 10))

plt.subplot(221), plt.hist(citra.ravel(), 256, [0, 256], color = 'black'), plt.title('Original')
plt.subplot(222), plt.hist(citra_eq.ravel(), 256, [0, 256], color = 'black'), plt.title('Ekualisasi')

plt.show()

cv.waitKey(0) #Agar tidak langsung keluar
cv.destroyAllWindows()
