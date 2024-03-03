# import other necessary libaries

import numpy as np
from utils import create_mask, create_line
from skimage.feature import peak_local_max
from skimage import feature
from skimage.feature import peak_local_max
from skimage.io import imread
import matplotlib.pyplot as plt
from utils import create_line, create_mask

# load the input image
image = imread('road.jpg', as_gray=True)

# run Canny edge detector to find edge points
edge1 = feature.canny(image, sigma = 2)
edge2 = feature.canny(image, sigma=3)
edge3 = feature.canny(image, sigma=8)

## THIS IS MY STEP
## DISPLAY THE RESULTS
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(8, 3))

ax[0].imshow(image, cmap='gray')
ax[0].set_title('The IMage', fontsize=8)

ax[1].imshow(edge1, cmap='gray')
ax[1].set_title('Canny Edges sigma=1.5', fontsize=8)
#
# ax[2].imshow(edge2, cmap='gray')
# ax[2].set_title('Canny Edges sigma=3', fontsize=8)
#
# ax[3].imshow(edge3, cmap='gray')
# ax[3].set_title('Canny Edges sigma=8', fontsize=8)
for a in ax:
    a.axis('off')
fig.tight_layout()
plt.show()
# create a mask for ROI by calling create_mask

# extract edge points in ROI by multipling edge map with the mask

# perform Hough transform

# find the right lane by finding the peak in hough space

# zero out the values in accumulator around the neighborhood of the peak

# find the left lane by finding the peak in hough space

# plot the results
