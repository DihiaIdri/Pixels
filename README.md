# Pixels
In this code you will set the dimensions (H, W) of the poster you will print and 
the dimensions (hp, wp) of the pixels that you want. Ideally, we do not want the 
pixels on the last row or column to be cut. Therefore, the code validates that
the pixel dimensions you input, hp and wp, are divisors of the poster dimensions,
H and W, respectively. 


### Pixel dimension
#### 1. Enter the size of the poster
#### 2. Enter the size of the desired pixel 
#### 3. The code will tell you if that size is possible or not, because you want all pixels to fit in perfectly
   1. Verify if each input pixel dimension is a divisor of the respective poster dimension.
      1. If it is not: find a lower and upper bound of acceptable pixel dimensions
      2. You will be prompted to select the combination of dimensions (height and width of the pixel) to try
      3. The random pixel poster will appear on the screen 
      4. You will be prompted to type whether you like it "YES" or not "NO"
      5. If you do not like it, you will be prompted to try another combination of "acceptable" dimensions. 
      6. The same process will repeat itself until you are satisfied "YES"
      7. A poster with a PNG (can be modified)  format will be saved as well as a text file containing the 
      dimensions (so you don't forget) in a directory of your choosing
