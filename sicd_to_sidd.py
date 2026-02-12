import matplotlib.pyplot as plt
from sarpy.io.complex.converter import open_complex
from sarpy.io.product.converter import open_product
from sarpy.processing.sidd.sidd_product_creation import create_detected_image_sidd
from sarpy.processing.ortho_rectify import OrthorectificationHelper, NearestNeighborMethod

import numpy as np

sicd_input = '2023-06-09-19-51-37_UMBRA-05_SICD.nitf'
sidd_input = '2023-06-09-19-51-37_UMBRA-05_SIDD.nitf'
sidd_walrus = '2024-10-02-07-25-58_UMBRA-07_SIDD.nitf'
sidd_output = 'test_convert_to_sidd.nitf'

sicd_reader = open_complex(sicd_input)

ortho_helper = NearestNeighborMethod(
    sicd_reader,
    index=0
)

create_detected_image_sidd(
    ortho_helper,
    output_directory='.',
    output_file=sidd_output,
)
sidd_reader = open_product(sidd_input)[:]
processed_sidd = open_product(sidd_output)[:]
plt.figure(figsize=(10, 10))
plt.imshow(processed_sidd, cmap='gray')
plt.title('sarpy processed')
plt.colorbar(label='db')

plt.figure(figsize=(10, 10))
plt.imshow(sidd_reader, cmap='gray')
plt.title('umbra processed')
plt.colorbar(label='db')

plt.show()

