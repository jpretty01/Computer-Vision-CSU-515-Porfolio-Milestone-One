# Jeremy Pretty
# CSC 515 - Portfolio Milestone One 
# Ensure we import the OpenCV as well as the OS to get the file for the photo/image
import cv2
import os

# Getting the file path for the image
file_name = os.path.join(os.path.dirname(__file__), 'shutterstock93075775--250.jpg')

# Reading the image and displaying it
img = cv2.imread(file_name)

# Create a copy of the image and save it
cv2.imwrite('brain_image_copy.png', img)

# Displaying the image
cv2.imshow('brain_image_window', img)

# Wait for a key press to close the window
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()