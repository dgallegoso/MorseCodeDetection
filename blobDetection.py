# -*- coding: utf-8 -*-
# Standard imports
import cv2
import numpy as np;

# Read image
def findBlob(im):
    # Our operations on the frame come here
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # cv2.imshow("rectangle", im)
    # cv2.waitKey(0)
    im=cv2.GaussianBlur(im, (5, 5), 55)
    im=cv2.medianBlur(im, 5)
    # cv2.imshow("rectangle", im)
    # cv2.waitKey(0)

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

    return keypoints

def getKeypointIm(im, elements):
    for i, elem in enumerate(elements):
        if int(elem.signal[-1]) == 1 and (elem.plot or i == 0):
            cv2.circle(im, tuple(elem.coord.astype(int)), int(elem.rad), (0,0,255))
