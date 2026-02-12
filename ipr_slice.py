import matplotlib.pyplot as plt
from sarpy.io.complex.converter import open_complex
from sarpy.io.product.converter import open_product
# from sarpy.io.complex.utils import get_min_max_complex
import numpy as np
from gc import collect

input_sicd = '2023-06-09-19-51-37_UMBRA-05_SICD.nitf'

sicd_reader = open_complex(input_sicd)
size = sicd_reader.data_size


sicd_data = sicd_reader[:]
flat_max = np.argmax(sicd_data)
row = flat_max // size[0]
col = flat_max % size[0]
print(row, col, flat_max)

slicex = sicd_data[row, :]
slicey = sicd_data[:, col]


# print(slice)
# log_scalex = 20 * np.log10(np.abs(slicex))
# log_scaley = 20 * np.log10(np.abs(slicey))

amplitudex = np.abs(slicex)
amplitudey = np.abs(slicey)

plt.figure()
plt.plot(amplitudex, color='blue')
plt.title('SICD slice x')

plt.figure()
plt.plot(amplitudey, color='green')
plt.title('SICD slice y')
plt.show()

plt.close()
collect()


