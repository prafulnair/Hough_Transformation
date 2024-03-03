

---

# Lane Detection using Hough Transform

In this project, I implement the Hough transform to detect straight lanes in an image. The task involves processing an image of a road and identifying major lanes using edge detection and the Hough transform.

## Instructions

1. **Clone Repository**: Clone the repository containing the code and data under the "hough" folder.

2. **Dependencies**: Ensure you have the necessary dependencies installed, including Python, NumPy, scikit-image (skimage), and any other required libraries.

3. **Run Script**: Run the Python script `hough.py` to perform lane detection using the Hough transform.

4. **Results**: The script will produce four figures displaying:
   - Original image with detected edges.
   - Region of interest (ROI) mask applied to edge map.
   - Detected lanes using the Hough transform, represented in blue and orange.
   - Final result after non-maximum suppression (NMS) to suppress neighboring lane detections.

## Steps

1. **Step 1: Edge Detection**:
   - Load the image "road.jpg", convert it to grayscale, and run the Canny edge detector to find edges.

2. **Step 2: Region of Interest (ROI)**:
   - Use the provided function `create_mask` in `utils.py` to create a binary mask for the ROI.
   - Multiply the mask with the edge map to obtain an edge map containing only the edges within the ROI.

3. **Step 3: Hough Transform**:
   - Implement the Hough transform using the polar representation \((\rho, \theta)\) as the parameter space.
   - Find the cell with the highest value in the Hough space, representing the primary lane (blue).
   - Apply non-maximum suppression (NMS) to suppress neighboring cells.
   - Find the next cell with the highest value in the Hough space, representing the secondary lane (orange).

## Report

- The script will generate four plots illustrating the original image with detected edges, the ROI mask applied to the edge map, the detected lanes using the Hough transform, and the final result after NMS.

---
