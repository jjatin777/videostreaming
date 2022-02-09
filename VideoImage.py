'''
import cv2
import copy


raw_img = cv2.imread ("C:/Users/jatin/Desktop/VideoStream/Jatin.jpg",0)
# img = cv2.resize(raw_img, (16,9))
img = raw_img

print('Image Dimensions :', img.shape)

# array = bytearray(img)

# print(len(array))
# i = 0
# for x in array:
#     i+=1
#     print(x)
# print(i)
# print(len(img))
# print(len(img[0]))

negative = copy.deepcopy(img)
# print(len(img))
for x in range(len(img)):
    for y in range(len(img[x])):
        for z in range(len(img[x][y])):
            # print(x,y,z)
            negative[x][y][z] = 255 - negative[x][y][z]

# for x in range(3):
#     for y in range(len(img[x])):
#         for z in range(len(img[x][y])):
            
#             if negative[x][y][z] == img[x][y][z]:
#                 print(x,y,z)
# print(negative)


# cv2.imshow("Jatin", img)
cv2.imshow("Jatin", negative)

# cv2.waitKey(0)
cv2.waitKey(20000)
cv2.destroyAllWindows()


#importing the required package
from PIL import Image
  
#open image in png format
img_png = Image.open("C:/Users/jatin/Desktop/VideoStream/Screenshot.png")
img_png = img_png.convert('RGB')
  
#The image object is used to save the image in jpg format
img_png.save("C:/Users/jatin/Desktop/VideoStream/Screenshot.jpg")
'''

import cv2


img = cv2.imread ("C:/Users/jatin/Desktop/VideoStream/Screenshot.png")
# print(img.shape)

# img = cv2.resize(img, (960,520))
cv2.imwrite("C:/Users/jatin/Desktop/VideoStream/Clean.jpg", img)
