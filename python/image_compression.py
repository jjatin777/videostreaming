# from PIL import Image, ImageDraw, ImageFont

import cv2

# used some pillow
# im = Image.open("C:/Users/jatin/Desktop/VideoStream/python/Clean.jpg")
# print('Input file size   : ', im.size )
# im.save("C:/Users/jatin/Desktop/VideoStream/python/Compressed.jpg" ,optimize=True,quality=20) 

# task 1
# # Reading image with cv2
# img = cv2.imread("C:/Users/jatin/Desktop/VideoStream/python/Clean.jpg")

# # compressing image by saving
# cv2.imwrite("C:/Users/jatin/Desktop/VideoStream/python/Compressed.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 20])

# # reading compressed image
# img = cv2.imread ("C:/Users/jatin/Desktop/VideoStream/python/Compressed.jpg")

''' 
  
# task 2 
# video capture object
vid = cv2.VideoCapture(0)

while(True):
      
    # Capture the video frame by frame
    ret, frame = vid.read()
  
    # compressing frame by saving it
    cv2.imwrite("C:/Users/jatin/Desktop/VideoStream/python/frame.jpg", frame, [int(cv2.IMWRITE_JPEG_QUALITY), 50])
    
    # reading compressed image
    frame = cv2.imread ("C:/Users/jatin/Desktop/VideoStream/python/frame.jpg")
    
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()

'''
# copying image
path = "C:/Users/jatin/Desktop/VideoStream/python/Compressed.jpg"
newpath = "C:/Users/jatin/Desktop/VideoStream/python/createdCompressed.jpg"
with open(path,'rb') as imFile:
    imstring = imFile.read()
    with open(newpath,'wb') as dest_image:
        dest_image.write(imstring)




        