from PIL import Image
import numpy as np


def main(H, W, hp, wp):
    # Need the pixel dimensions to be an integer divisor of the poster dimension
    # For H dimension
    poster_D = [H, W]
    pixel_D = [hp, wp]
    #Column for H & W, Rows for min and max
    final_D = np.zeros((2, 2))
    final_num = np.zeros((2, 2))

    for i in range(2):
        if poster_D[i] % pixel_D[i] == 0:
            final_D[0][i] = pixel_D[i]
            final_D[1][i] = pixel_D[i]
            final_num[0][i] = poster_D[i] / pixel_D[i]
            final_num[1][i] = poster_D[i] / pixel_D[i]
        else:
            [p_min, p_max] = min_max(poster_D[i], pixel_D[i])
            final_D[0][i] = p_min
            final_D[1][i] = p_max
            final_num[0][i] = poster_D[i] / p_min
            final_num[1][i] = poster_D[i] / p_max

    print("Potential Pixel size in cm")
    print(final_D)
    print("Number of pixels for each dimension")
    print(final_num)
    satisfied = 'No'
    while (satisfied == 'No'):
        h_pixel = int(input("Enter the height of the pixel i.e.first column of pixel dimension: "))
        w_pixel = int(input("Enter the width of the pixel i.e.second  column of pixel dimension: "))
        im = poster(poster_D, h_pixel, w_pixel)
        im.show()
        satisfied = input("Are you satisfied? Yes or No?: ")
        if (satisfied == 'Yes'):
            im.save('/Users/dihiaidrici/Desktop/SecondPaper/PixelFigure.tif')

def poster(poster_D, h_pixel, w_pixel):
    h_pixel_num = int(poster_D[0] / h_pixel)
    w_pixel_num = int(poster_D[1] / w_pixel)

    # produce random pixel image. 255 is for an 8bit image. for 16bit it would be more
    imarray = np.random.rand(h_pixel_num, w_pixel_num, 3) * 255
    newImage = Image.fromarray(imarray.astype('uint8'))  # .convert('RGBA')
    return newImage

def min_max(poster_i, p_i):
    for p_min in range(p_i,0,-1):
        if(poster_i % p_min == 0):
            break
    for p_max in range(p_i, poster_i+1, 1):
        if (poster_i % p_max == 0):
            break
    return p_min, p_max


if __name__ == '__main__':
    H = 1000  # cm
    W = 1000  # cm
    hp = 3  # cm
    wp = 5  # cm
    main(H, W, hp, wp)