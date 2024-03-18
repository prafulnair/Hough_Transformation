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
edge1 = feature.canny(image)

# display_Stuff(image, edge1)

# create a mask for ROI by calling create_mask
mask_roi = create_mask(edge1.shape[0], edge1.shape[1])

# extract edge points in ROI by multipling edge map with the mask
edges_roi = edge1 * mask_roi

# display_Stuff(image, edge1, edges_roi, mask_roi)


## new changes
theta_res = 1
rho_res = 1
theta = np.deg2rad(np.arange(-90, 90, theta_res))
diagonal_length = int(np.ceil(np.sqrt(
    edges_roi.shape[0] ** 2 + edges_roi.shape[1] ** 2)))  # Adjusting to ceil to ensure covering all diagonal points
rho = np.arange(-diagonal_length, diagonal_length, rho_res)

# perform Hough transform
accumulator_size_rho = len(rho)
accumulator = np.zeros((accumulator_size_rho, len(theta)))


edge_points = np.argwhere(edges_roi)
# updating the accumulator
for y, x in edge_points:
    for t_idx, t in enumerate(theta):
        rho_val = int(x * np.cos(t) + y * np.sin(t))
        rho_idx = np.argmin(np.abs(rho - rho_val))
        accumulator[rho_idx, t_idx] += 1

# find the right lane by finding the peak in hough space

# right_lane_theta, right_lane_rho = np.unravel_index(np.argmax(accumulator), accumulator.shape)

max_idx = np.argmax(accumulator)
rho_index, theta_idx = np.unravel_index(max_idx, accumulator.shape)
rho_val = rho[rho_index]
theta_val = theta[theta_idx]

# zero out the values in accumulator around the neighborhood of the peak (NMS basically)
neighborhood_size = 50
accumulator[max(0, rho_index - neighborhood_size):min(accumulator.shape[0], rho_index + neighborhood_size),
max(0, theta_idx - neighborhood_size):min(accumulator.shape[1], theta_idx + neighborhood_size)] = 0

# find the left lane by finding the peak in hough space
max_idx = np.argmax(accumulator)
rho_idx, theta_idx = np.unravel_index(max_idx, accumulator.shape)
rho_val_left = rho[rho_idx]
theta_val_left = theta[theta_idx]
# plot the results

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.ravel()
# Plot original image
axes[0].imshow(edge1, cmap='gray')
axes[0].set_title('Edges')

# Plot Canny edges
axes[1].imshow(edges_roi, cmap='gray')
axes[1].set_title('Edges in ROI')

# Plot edge points in ROI
axes[2].imshow(mask_roi, cmap='gray')
axes[2].set_title('mask')

# Plot detected lanes

axes[3].imshow(image)

# Plot right lane
x1_right = image.shape[1]
y1_right = int((rho_val - x1_right * np.cos(theta_val)) / np.sin(theta_val))
x2_right = image.shape[1] // 2

y2_right = int((rho_val - x2_right * np.cos(theta_val)) / np.sin(theta_val))


axes[3].plot([x1_right, x2_right], [y1_right, y2_right], 'b-')

# Plot left lane
x1_left = 160
y1_left = int((rho_val_left - x1_left * np.cos(theta_val_left)) / np.sin(theta_val_left))
x2_left = image.shape[1] // 2
y2_left = int((rho_val_left - x2_left * np.cos(theta_val_left)) / np.sin(theta_val_left))

axes[3].plot([x1_left, x2_left], [y1_left, y2_left], 'orange')

axes[3].set_title('Detected Lanes')

plt.show()
