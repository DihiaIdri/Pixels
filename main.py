from PIL import Image
import numpy as np


def main(H, W, hp, wp):
    poster_D = [H, W]  # poster Dimensions
    pixel_D = [hp, wp]  # pixel Dimensions
    # Column for H & W, Rows for min and max
    final_D = np.zeros((2, 2))

    for i in range(2):
        if poster_D[i] % pixel_D[i] == 0:
            final_D[0][i] = pixel_D[i]
            final_D[1][i] = pixel_D[i]
        else:
            # find acceptable pixel dimensions, Column for H & W, Rows for min and max
            [size_min, size_max] = min_max(poster_D[i], pixel_D[i])
            final_D[0][i] = size_min
            final_D[1][i] = size_max

    print("Potential Pixel size in cm")
    print(final_D)
    print("Remember that the smaller the size of the pixel, the more pixels there will be.")
    satisfied = 'No'
    while satisfied == 'No' or satisfied == 'no':
        h_pixel = int(input("Enter the height of the pixel i.e.first column of pixel dimension: "))
        w_pixel = int(input("Enter the width of the pixel i.e.second  column of pixel dimension: "))

        if (h_pixel == final_D[0][0] or h_pixel == final_D[1][0]) and (w_pixel == final_D[0][1] or w_pixel == final_D[1][1]):
            num_h_pixel = int(poster_D[0] / h_pixel)
            num_w_pixel = int(poster_D[1] / w_pixel)
            im = poster(h_pixel, w_pixel, num_h_pixel, num_w_pixel)
            im.show()

            satisfied = input("Are you satisfied? Yes or No?: ")
            if satisfied == 'Yes' or satisfied == 'yes':
                im.save('/Users/dihiaidrici/Desktop/SecondPaper/PixelFigure.png')
                f = open('/Users/dihiaidrici/Desktop/SecondPaper/PosterDimensions', 'w')
                f.write('Poster dimensions in cm:\n')
                f.writelines(str(poster_D))
                f.write('\n')
                f.write('Pixel dimensions in cm:\n')
                f.writelines(str(pixel_D))
        else:
            print("You made a mistake selecting the height or width of the pixels. Try again. if you changed your mind about the pixel dimensions stop and try again")


def poster(mul_h, mul_w, num_h_pixel, num_w_pixel):
    hBig = num_h_pixel*mul_h
    wBig = num_w_pixel*mul_w
    # produce random pixel image. 255 is for an 8bit image. for 16bit it would be more
    im = np.random.rand(num_h_pixel, num_w_pixel, 3) * 255
    pixelImage = Image.fromarray(im.astype('uint8'))  # .convert('RGBA')

    imarray = np.zeros((hBig, wBig, 3))
    for x in range(num_w_pixel):  # Horizontal, column
        idx = mul_w*x
        for y in range(num_h_pixel):  # Vertical, rows
            idy = mul_h*y
            imarray[idy:idy + mul_h, idx:idx + mul_w] = imarray[idy:idy + mul_h, idx:idx + mul_w] + pixelImage.getpixel((x, y))

    large_pixelImage = Image.fromarray(imarray.astype('uint8'))  # .convert('RGBA')
    return large_pixelImage


def min_max(poster_i, p_i):
    for size_min in range(p_i, 0, -1):
        if poster_i % size_min == 0:
            break
    for size_max in range(p_i, poster_i+1, 1):
        if poster_i % size_max == 0:
            break
    return size_min, size_max


if __name__ == '__main__':
    H = 1000  # cm
    W = 1500  # cm
    hp = 4  # cm
    wp = 7  # cm
    main(H, W, hp, wp)
