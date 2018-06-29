import numpy as np
import cv2

img_color = cv2.imread( '2.jpg', cv2.IMREAD_COLOR )


height, width, channel = img_color.shape
img_gray = np.zeros( (height,width), np.uint8 )


print(height, width, channel)


for y in range(0, height):
    for x in range(0, width):
        b = img_color.item(y,x,0)
        g = img_color.item(y,x,1)
        r = img_color.item(y,x,2)

        gray = (int(b)+int(g)+int(r))/3.0

        if gray>255:
            gray=255

        img_gray.itemset( y, x, gray)



cv2.imshow( 'color image', img_color )
cv2.imshow( 'gray image', img_gray )

cv2.imwrite('result2.jpg', img_gray )

cv2.waitKey(0)
cv2.destroyAllWindows()
