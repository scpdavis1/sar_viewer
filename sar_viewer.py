import matplotlib.pyplot as plt
from sarpy.io.product.converter import open_product
from sarpy.io.complex.converter import open_complex
from gc import collect
from argparse import ArgumentParser

import numpy as np

def center_square(reader, size: int) -> tuple:
    """
    Given a size, make a square chip from the center.
    
    :param sidd_reader: Description
    :param size: Description
    :type size: int
    :return: Description
    :rtype: tuple
    """
    img_size = reader.data_size
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

def view_sicd(path: str, size: int) -> None:
    """
    Given a SICD, plot the whole thing or a centered square chip.
    
    :param path: Description
    :type path: str
    :param size: Description
    :type size: int
    """
    sicd_data = open_complex(path)
    if size != None:
        bounds = center_square(sicd_data, size)

        sicd_data = sicd_data[
            bounds[0]:bounds[1],
            bounds[2]:bounds[3]
        ]
    else:
        sicd_data = sicd_data[:]
    
    log_scale = 20 * np.log10(np.abs(sicd_data))
    
    plt.figure(figsize=(10, 10))
    plt.imshow(log_scale, cmap='gray')
    plt.title('SAR SICD Data')
    plt.colorbar(label='db')
    plt.show()
    plt.close()
    collect()
    
if __name__ == "__main__":

    # Arg parser
    parser = ArgumentParser(
        prog='SIDDViewer',
        description='View a SIDD or SICD.',
    )
    parser.add_argument(
        'path',
        help="Path to a SIDD or SICD.",
    )
    parser.add_argument(
        '--sidd',
        action='store_true'
    )
    parser.add_argument(
        '--sicd',
        action='store_true'
    )
    parser.add_argument(
        '-s',
        '--size',
        type=int,
        help="Box square size. If not used will render entire image.",
    )

    args = parser.parse_args()

    if args.sidd == args.sicd:
        raise Exception("Choose a single image type.")

    if args.sidd:
        view_sidd(
            args.path,
            size=args.size,
        )
    else:
        view_sicd(
            args.path,
            size=args.size
        )
