# -*- coding: utf-8 -*-
# Standard imports
import cv2
import numpy as np;
from skimage import measure
import imutils
from imutils import contours


# Read image
def findBlob(im):
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # threshold the image to reveal light regions in the
    # blurred image
    thresh = cv2.threshold(blurred, 200, 255, cv2.THRESH_BINARY)[1]

    # perform a series of erosions and dilations to remove
    # any small blobs of noise from the thresholded image
    thresh = cv2.erode(thresh, None, iterations=2)
    thresh = cv2.dilate(thresh, None, iterations=4)
  
    # perform a connected component analysis on the thresholded
    # image, then initialize a mask to store only the "large"
    # components
    labels = measure.label(thresh, neighbors=8, background=0)

    mask = np.zeros(thresh.shape, dtype="uint8")

    # loop over the unique components
    for label in np.unique(labels):
        # if this is the background label, ignore it
        if label == 0:
            continue

        # otherwise, construct the label mask and count the
        # number of pixels 
        labelMask = np.zeros(thresh.shape, dtype="uint8")
        labelMask[labels == label] = 255
        numPixels = cv2.countNonZero(labelMask)

        # if the number of pixels in the component is sufficiently
        # large, then add it to our mask of "large blobs"
        if numPixels > 300:
            mask = cv2.add(mask, labelMask)

    circles = []

    # find the contours in the mask, then sort them from left to
    # right
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    try:
        cnts = cnts[0] if imutils.is_cv2() else cnts[1]
        cnts = contours.sort_contours(cnts)[0]
    except:
        return circles

    # loop over the contours
    for (i, c) in enumerate(cnts):
        # draw the bright spot on the image
        circles.append(cv2.minEnclosingCircle(c))

    return circles




    '''
    # Our operations on the frame come here
    im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("rectangle", im)
    #cv2.waitKey(0)
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
    print labels, keypoints
    return keypoints

    '''



def debugKeypointIm(im, keypoints):
    im = cv2.drawKeypoints(im, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)


def getKeypointIm(im, elements):
    for i, elem in enumerate(elements):
        if int(elem.signal[-1]) == 1 and (elem.plot or i == 0):
            try:
                cv2.circle(im, tuple(elem.coord.astype(int)), int(elem.rad), (0,0,255))
                font = cv2.FONT_HERSHEY_SIMPLEX
                text = str(elem.num)
                cv2.putText(im,text,tuple(elem.coord.astype(int)), font, 1,(0,0,255),2)
            except:
                print "hiding exception"
