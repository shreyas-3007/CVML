import cv2
import numpy as np
import matplotlib.pyplot as plt

# input image
img_1 = cv2.imread('graph 1.png')
img = cv2.resize(img_1, (500, 500))


cv2.namedWindow('image')

# list to store the clicked points
points = []

# mouse  function
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) >= 6:
            #  polynomial regression
            coeffs = np.polyfit([p[0] for p in points], [p[1] for p in points], 2)

            #  x values
            x_values = np.arange(0, img.shape[1], 1)

           
            y_values = np.polyval(coeffs, x_values)

            # Ploting   input image and  fitted curve
            plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            plt.plot(x_values, y_values, color='red', linewidth=1)
            plt.show()



cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()
