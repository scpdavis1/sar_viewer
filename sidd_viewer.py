import matplotlib.pyplot as plt
from sarpy.io.product.converter import open_product
from sys import argv
from gc import collect
from argparse import ArgumentParser

# input = '2023-11-10-17-01-39_UMBRA-04_SICD.nitf'
# sidd_input = '2023-06-09-19-51-37_UMBRA-05_SIDD.nitf'
# walrus = '2024-10-02-07-25-58_UMBRA-07_SIDD.nitf'
# test_img = 'test_convert_to_sidd.nitf'
# jeddah_tower = '2025-06-10-08-33-52_UMBRA-09_SIDD.nitf'

def center_square(sidd_reader, size: int) -> tuple:
    """
    Given a size, make a square chip from the center.
    
    :param sidd_reader: Description
    :param size: Description
    :type size: int
    :return: Description
    :rtype: tuple
    """
    img_size = sidd_reader.data_size
    center_xy = tuple([ x//2 for x in img_size ])
    radius = size//2

    return (
        center_xy[0] - radius,
        center_xy[0] + radius,
        center_xy[1] - radius,
        center_xy[1] + radius,
    )

def center_half_size(sidd_reader) -> tuple:
    """
    Docstring for center_half_size
    
    :param sidd_reader: Description
    :return: Description
    :rtype: tuple
    """
    size = sidd_reader.data_size

    rows_start = size[0]//2//2
    rows_end = size[0]-rows_start

    cols_start = size[1]//2//2
    cols_end = size[1]-cols_start
    
    return (rows_start, rows_end, cols_start, cols_end)

def view_sidd(path: str, size: int) -> None:
    """
    Given a SIDD, plot the whole thing or a centered square chip.
    
    :param path: Description
    :type path: str
    :param bounds: Description
    :type bounds: tuple
    """
    sidd_data = open_product(path)
    if size != None:
        bounds = center_square(sidd_data, size)

        sidd_data = sidd_data[
            bounds[0]:bounds[1],
            bounds[2]:bounds[3]
        ]
    else:
        sidd_data = sidd_data[:]

    plt.figure(figsize=(10, 10))
    plt.imshow(sidd_data, cmap='gray')
    plt.title('SAR SIDD Data')
    plt.colorbar(label='db')
    plt.show()
    plt.close()
    collect()
    
if __name__ == "__main__":

    # Arg parser
    parser = ArgumentParser(
        prog='SIDDViewer',
        description='View a SIDD.',
    )
    parser.add_argument(
        'sidd_path',
        help="Path to a SIDD.",
    )
    parser.add_argument(
        '-s',
        '--size',
        type=int,
        help="Box square size. If not used will render entire image.",
    )

    args = parser.parse_args()

    view_sidd(
        args.sidd_path,
        size=args.size,
    )
