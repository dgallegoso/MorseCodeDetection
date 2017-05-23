import numpy as np
import cv2
import  blobDetection

cap = cv2.VideoCapture('data/sos_light.mp4')

while(True):
    # Capture frame-by-frame
    ret, im = cap.read()

    if not ret: break

    keypoints = blobDetection.findBlob(im)
    im = blobDetection.getKeypointIm(im, keypoints)

    # Display the resulting frame
    cv2.imshow('frame',im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
