# import other necessary libraries
import numpy as np
from utils import create_mask, create_line
from skimage.feature import peak_local_max
from skimage import feature
from skimage.io import imread
import matplotlib.pyplot as plt

# load the input image
image = imread('road.jpg', as_gray=True)

# run Canny edge detector to find edge points
edge1 = feature.canny(image)

# create a mask for ROI by calling create_mask
mask_roi = create_mask(edge1.shape[0], edge1.shape[1])

# extract edge points in ROI by multiplying edge map with the mask
edges_roi = edge1 * mask_roi

## unperformed steps
theta_res = 1
rho_res = 1
theta = np.deg2rad(np.arange(-90, 90, theta_res))
diagonal_length = int(np.ceil(np.sqrt(
    edges_roi.shape[0] ** 2 + edges_roi.shape[1] ** 2)))  # Adjusted to ceil to ensure covering all diagonal points
rho = np.arange(-diagonal_length, diagonal_length, rho_res)

# perform Hough transform
accumulator_size_rho = len(rho)
accumulator = np.zeros((accumulator_size_rho, len(theta)))

## unperformed step
edge_points = np.argwhere(edges_roi)

for y, x in edge_points:
    for t_idx, t in enumerate(theta):
        rho_val = int(x * np.cos(t) + y * np.sin(t))
        rho_idx = np.argmin(np.abs(rho - rho_val))
        accumulator[rho_idx, t_idx] += 1

# Find peaks in Hough space using peak_local_max
peaks = peak_local_max(accumulator, min_distance=50, threshold_abs=100)

# Sort peaks by accumulator values
sorted_peaks = peaks[np.argsort(accumulator[peaks[:, 0], peaks[:, 1]])[::-1]]

# Plot the peaks on the accumulator for visualization
plt.imshow(accumulator)
plt.scatter(sorted_peaks[:, 1], sorted_peaks[:, 0], c='r', marker='x')
plt.title('Peaks in Hough Space')
plt.show()

# Extract the two most prominent peaks

rho_idx1, theta_idx1 = sorted_peaks[0]
rho_idx2, theta_idx2 = sorted_peaks[1]

# Convert peaks into lines
xs1, ys1 = create_line(rho[rho_idx1], theta[theta_idx1], image)
xs2, ys2 = create_line(rho[rho_idx2], theta[theta_idx2], image)

# Plot the detected lanes
plt.imshow(image, cmap='gray')
plt.plot(xs1, ys1, 'b-', label='Lane 1')
plt.plot(xs2, ys2, 'orange', label='Lane 2')
plt.title('Detected Lanes')
plt.legend()
plt.show()
