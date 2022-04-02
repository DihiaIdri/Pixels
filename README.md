# Pixels
In this code you will set the dimensions (H, W) of the poster you will print and 
the dimensions (hp, wp) of the pixels that you want. Ideally, we do not want the 
pixels on the last row or column to be cut. Therefore, the code validates that
the pixel dimensions you input, hp and wp, are divisors of the poster dimensions,
H and W, respectively. 


###Pixel dimension
1. Verify if each input pixel dimension is a divisor of the respective poster dimension.
2. If it is not: find the lower and upper bound.
3. You will be prompted to select the combination of dimensions to try
   1. The random pixel poster will appear on the screen 
   2. You will be prompted to type whether you like it "YES" or not "NO"
   3. If you do not like it, you will be prompted to try another combination of dimensions. 
   4. The same process will repeat itself until you are satisfied "YES"

4. A poster with a TIFF format will be saved as well as a text file containing the 
dimensions (so you don't forget) in a directory of your choosing
