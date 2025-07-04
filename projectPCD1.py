# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vk_QUEUKseOuMkcCWmRszV8wNdwQG65Z
"""

from google.colab import drive
drive.mount('/content/drive')

import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

# Ganti path dengan direktori citra kamu
image_path = '/content/drive/MyDrive/pcd/1008.png'

# Baca citra berwarna dan konversi ke grayscale
img = cv2.imread(image_path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Resize menjadi 256x256
gray_resized = cv2.resize(gray, (256, 256))

# Histogram Equalization
equalized = cv2.equalizeHist(gray_resized)

# Tampilkan hasil dan histogram
show_image_and_histogram(gray_resized, equalized)

std_before = np.std(gray_resized)
std_after = np.std(equalized)

print(f"Standar Deviasi Sebelum: {std_before:.2f}")
print(f"Standar Deviasi Sesudah: {std_after:.2f}")

def show_image_and_histogram(original, processed, title1='Original', title2='Equalized'):
    fig, axs = plt.subplots(2, 2, figsize=(12, 6))

    axs[0, 0].imshow(original, cmap='gray')
    axs[0, 0].set_title(title1)
    axs[0, 0].axis('off')

    axs[0, 1].imshow(processed, cmap='gray')
    axs[0, 1].set_title(title2)
    axs[0, 1].axis('off')

    axs[1, 0].hist(original.ravel(), bins=256, range=(0, 256), color='gray')
    axs[1, 0].set_title('Histogram Sebelum')

    axs[1, 1].hist(processed.ravel(), bins=256, range=(0, 256), color='gray')
    axs[1, 1].set_title('Histogram Sesudah')
    plt.tight_layout()
    plt.show()

original = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
processed = cv2.equalizeHist(original)

show_image_and_histogram(original, processed)