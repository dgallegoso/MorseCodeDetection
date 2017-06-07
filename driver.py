import cv2
import  blobDetection
import motionTracking
import translate
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture('data/flashlight.mp4')

blobs = []
while(True):
    # Capture frame-by-frame
    ret, im = cap.read()

    if not ret: break

    keypoints = blobDetection.findBlob(im)
    blobs = motionTracking.track(blobs, keypoints)
    blobs = motionTracking.prune_noise(blobs)
    blobDetection.getKeypointIm(im, blobs)
    # blobDetection.debugKeypointIm(im, keypoints)
    # if len(blobs[0].signal)>10:
    #     print translate.decode(blobs[0].signal*2 - 1)
    # print len(blobs)

    # Display the resulting frame
    cv2.imshow('frame',im)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

blobs = motionTracking.prune_noise(blobs, 0, True)
imgs = []
for blob in blobs:
    codeImg = np.reshape(blob.signal*2 - 1, (1, -1))
    codeImg = np.repeat(codeImg, 10, axis=1)
    codeImg = np.repeat(codeImg, codeImg.shape[1]/20, axis=0)
    imgs.append(codeImg)
    print translate.decode(blob.signal*2 - 1)
    print list(blob.signal*2 - 1)
cap.release()
cv2.destroyAllWindows()

fig = plt.figure()
nrows = len(imgs)
ncols = 1
count = 1
last_ax = None;

for img in imgs: 
    ax = None
    if(last_ax != None):
        ax = fig.add_subplot(nrows, ncols, count)
    else:
        ax = fig.add_subplot(nrows, ncols, count, sharex=last_ax, sharey=last_ax)
    last_ax = ax
    ax.imshow(img);
    count = count + 1

plt.show()
