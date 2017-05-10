# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("data/milestone.jpg", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.
params = cv2.SimpleBlobDetector_Params()
params.filterByColor = True
params.blobColor = 255
params.filterByArea = True
params.minArea = 0
params.maxArea = im.shape[0] * im.shape[1] * 10

params.filterByCircularity = False

params.filterByInertia = False
params.filterByConvexity = False

params.minDistBetweenBlobs = 5

detector = cv2.SimpleBlobDetector(params)

# Detect blobs.
keypoints = detector.detect(im)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
