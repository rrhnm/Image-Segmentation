import cv2
import numpy as np

# Menentukan rentang warna yang ingin disegmentasi
batasBawah_kuning = np.array([20, 100, 100])
batasAtas_kuning = np.array([35, 255, 255])

batasBawah_hijau = np.array([36, 100, 100])
batasAtas_hijau = np.array([86, 255, 255])

batasBawah_putih = np.array([0, 0, 200])
batasAtas_putih = np.array([180, 20, 255])

batasBawah_hitam = np.array([0, 0, 0])
batasAtas_hitam = np.array([180, 255, 50])

# Loop untuk setiap gambar
for i in range(1, 17):
    # Membaca gambar
    citra_pisang_asli = cv2.imread(f'D://.Kuliah Raihan M//SEMESTER 3//Pengolahan Citra//Project Pisang UAS//Pisang Resize//Pisang-{i}.jpg')

    # Mengubah gambar dari BGR ke HSV
    konversi_hsv = cv2.cvtColor(citra_pisang_asli, cv2.COLOR_BGR2HSV)

    # Membuat mask untuk setiap warna
    mask_kuning = cv2.inRange(konversi_hsv, batasBawah_kuning, batasAtas_kuning)
    mask_hijau = cv2.inRange(konversi_hsv, batasBawah_hijau, batasAtas_hijau)
    mask_putih = cv2.inRange(konversi_hsv, batasBawah_putih, batasAtas_putih)
    mask_hitam = cv2.inRange(konversi_hsv, batasBawah_hitam, batasAtas_hitam)

    # Menggabungkan semua mask
    mask = cv2.bitwise_or(mask_kuning, mask_hijau)
    mask = cv2.bitwise_or(mask, mask_putih)
    mask = cv2.bitwise_or(mask, mask_hitam)

    # Mengaplikasikan mask pada gambar
    hasil = cv2.bitwise_and(citra_pisang_asli, citra_pisang_asli, mask=mask)

    # Menampilkan gambar
    #cv2.imshow(f'Citra Pisang Asli {i}', citra_pisang_asli)
    #cv2.imshow(f'Hasil mask {i}', mask)
    cv2.imshow(f'Hasil Segmentasi {i}', hasil)

cv2.waitKey(0)
cv2.destroyAllWindows()