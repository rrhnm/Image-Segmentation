# Mengimpor modul OpenCV
import cv2 as cv

# Mengimpor gambar
img = cv.imread("D://.Kuliah Raihan M//SEMESTER 3//Pengolahan Citra//Project Pisang UAS//Data Punya Dimas//pisang1.jpg")

# Mengubah gambar dari BGR ke HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# Membuat fungsi untuk menampilkan nilai HSV pada titik koordinat ketika mouse diklik
def show_hsv(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        # Mendapatkan nilai HSV pada titik koordinat
        h, s, v = hsv[y, x]
        print("Koordinat [{}, {}]".format(x, y), end = " --> ")
        # Menampilkan nilai HSV pada titik koordinat
        text = "HSV [{}, {}, {}]".format(h, s, v)
        print(text)
        cv.imshow("image", img)

# Menampilkan gambar
cv.imshow("image", img)
cv.setMouseCallback("image", show_hsv)

cv.waitKey(0)
cv.destroyAllWindows()