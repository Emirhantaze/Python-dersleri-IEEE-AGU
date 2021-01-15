import numpy as np
import cv2
from matplotlib import pyplot as plt

# Basic averaging
img = cv2.imread('lena.jpg')
kernel = np.ones((10,10),np.float32)/100
avg = cv2.filter2D(img,-1,kernel)

# Median filtering
median = cv2.medianBlur(img, 5)

# Convert colors
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
avg = cv2.cvtColor(avg,cv2.COLOR_BGR2RGB)
median = cv2.cvtColor(median,cv2.COLOR_BGR2RGB)

# Show original image
plt.subplot(1,3,1),plt.imshow(img),plt.title('Original')
plt.axis('off')
# Show averaging filter output
plt.subplot(1,3,2),plt.imshow(avg),plt.title('Averaging Filter')
plt.axis('off')
# Show median filter output
plt.subplot(1,3,3),plt.imshow(median),plt.title('Median Filter')
plt.axis('off')
plt.show()