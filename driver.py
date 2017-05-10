import numpy as np
import cv2
# import cvxpy as cvx

orig_img = cv2.imread('data/milestone.jpg')

# Blur image to remove noise
frame=cv2.GaussianBlur(orig_img, (3, 3), 0)
frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

# Switch image from BGR colorspace to HSV
# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# cv2.imshow("Keypoints", hsv)
# cv2.waitKey(0)

# define range of purple color in HSV
# purpleMin = (115,50,10)
# purpleMax = (160, 255, 255)

# print hsv.shape

# Sets pixels to white if in purple range, else will be set to black
frame = cv2.inRange(frame, 200, 255)

minSize = 10

for size in range(minSize, min(frame.shape) / 2):
    for 


cv2.imshow("Keypoints", frame)
cv2.waitKey(0)


'''
x1 = cvx.Variable(2)
x2 = cvx.Variable(2)

A = frame / float(255)
A = A.astype(int)

constraints = [x1 >= 0,
               x2 >= 0,
               x1[0] <= frame.shape[0],
               x1[1] <= frame.shape[1],
               x2[0] <= frame.shape[0],
               x2[1] <= frame.shape[1]]
# lam = cvx.Parameter(sign = 'positive', 1)
'''

# cv2.imshow("Keypoints", mask)
# cv2.waitKey(0)

# Bitwise-AND of mask and purple only image - only used for display
# res = cv2.bitwise_and(frame, frame, mask= mask)

#    mask = cv2.erode(mask, None, iterations=1)
# commented out erode call, detection more accurate without it

# dilate makes the in range areas larger
# frame = cv2.dilate(frame, None, iterations=1)
#
# cv2.imshow("Keypoints", frame)
# cv2.waitKey(0)
'''
    # Set up the SimpleBlobdetector with default parameters.
params = cv2.SimpleBlobDetector_Params()

# Change thresholds
params.minThreshold = 50;
params.maxThreshold = 256;

# Filter by Area.
params.filterByArea = True
params.minArea = 30
params.maxArea = 100000

# Filter by Circularity
# params.filterByCircularity = True
# params.minCircularity = 0.1

# Filter by Convexity
# params.filterByConvexity = True
# params.minConvexity = 0.5

# Filter by Inertia
# params.filterByInertia =True
# params.minInertiaRatio = 0.5

params.filterByColor = True
params.blobColor = 255

detector = cv2.SimpleBlobDetector(params)

# Detect blobs.
# frame=255-frame
#
cv2.imshow("Keypoints", frame)
cv2.waitKey(0)
keypoints = detector.detect(frame)

print keypoints
im_with_keypoints = cv2.drawKeypoints(orig_img, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)
'''
