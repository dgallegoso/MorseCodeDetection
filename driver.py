import numpy as np
import cv2
import  blobDetection

cap = cv2.VideoCapture('data/flashlight.mp4')

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret: break

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    keypoints = blobDetection.findBlob(gray)
    gray = blobDetection.getKeypointIm(gray, keypoints)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
