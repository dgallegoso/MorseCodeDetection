import cv2
import numpy as np;

# Read image
im = cv2.imread("data/milestone.jpg", cv2.IMREAD_GRAYSCALE)

# Set up the detector with default parameters.

params = cv2.SimpleBlobDetector_Params()
#increasing minThreshold gets rid of tiny blobs
params.minThreshold = 150;
params.maxThreshold = 175;

#use blobColor = 255 to find light blobs and blobColor = 0 to find dark blobs
params.filterByColor = True
params.blobColor = 255

# Filter by Area
params.filterByArea = True
params.minArea = 1
params.maxArea = 100000


detector = cv2.SimpleBlobDetector(params)


#increase the size of each blob
keypoints = detector.detect(im)
for kp in keypoints:
	kp.size *= 3

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
im_with_keypoints = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
