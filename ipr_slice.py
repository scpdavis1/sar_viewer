import matplotlib.pyplot as plt
from sarpy.io.complex.converter import open_complex
from sarpy.io.product.converter import open_product
import numpy as np

input = '2023-11-10-17-01-39_UMBRA-04_SICD.nitf'
sidd_input = '2023-06-09-19-51-37_UMBRA-05_SIDD.nitf'
walrus = '2024-10-02-07-25-58_UMBRA-07_SIDD.nitf'
test_img = 'test_convert_to_sidd.nitf'
jeddah_tower = '2025-06-10-08-33-52_UMBRA-09_SIDD.nitf'


x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.figure(1)
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')

reader = open_complex(input)[0:1000, 0:1000]
image_data = 20 * np.log10(np.abs(reader))
sidd_reader = open_product(sidd_input)[:]

plt.figure(figsize=(10, 10))
plt.imshow(image_data, cmap='gray')
plt.title('SAR SICD Data')
plt.colorbar(label='db')

plt.figure(figsize=(10, 10))
plt.imshow(sidd_reader, cmap='gray')
plt.title('SAR SIDD Data')
plt.colorbar(label='db')

plt.show()
