import cv2

# Load the image
img = cv2.imread('graph 1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
resized_img = cv2.resize(img, (500, 500))

# Get the dimensions of the image
height, width = img.shape[:2]

print(img.shape)
print(gray.shape)
print(resized_img.shape)

# Define the new dimensions


# Resize the image
#resized_img = cv2.resize(img, (new_width, new_height))

# Display the original and resized images
#cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
