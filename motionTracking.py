import numpy as np
from sklearn.cluster import KMeans

MAX_MOVEMENT_RATIO = 1
MAX_SIZE_RATIO = .5
ALPHA = .2

class Element(object):
    def __init__(self, coord, rad, n):
        self.coord = coord
        self.rad = rad
        self.signal = np.append(np.zeros(n), 1).astype(int)
        self.plot = False
    def similarity(self, elem):
        if np.linalg.norm(self.coord - elem.coord) / self.rad <= MAX_MOVEMENT_RATIO:
            if abs(self.rad - elem.rad) / self.rad <= MAX_SIZE_RATIO:
                return 1
        return 0
    def merge(self, elem):
        self.coord = ALPHA * elem.coord + (1 - ALPHA) * self.coord
        self.rad = ALPHA * elem.rad + (1 - ALPHA) * self.rad

def track(elements, keypoints):
    n = len(elements[0].signal) if len(elements) != 0 else 0
    sentinel = n > 256
    for keypoint in keypoints:
        newElem = Element(np.array(keypoint.pt), keypoint.size / 2, n)
        isMerged = False
        for elem in elements:
            if len(elem.signal) == n and elem.similarity(newElem) == 1:
                elem.merge(newElem)
                elem.signal = np.append(elem.signal, 1)
                isMerged = True
                break
        if not isMerged:
            elements.append(newElem)
    for elem in elements:
        if len(elem.signal) == n:
            elem.signal = np.append(elem.signal, 0)
    elements = sorted(elements, key=lambda x: -np.sum(x.signal))
    return elements

# handles case where no lights permanently on
def prune_noise(elements, minLength=30, force=False):
    if len(elements) == 0:
        return elements
    n = len(elements[0].signal)
    averages = np.empty(0, dtype=float)
    indexes = np.empty(0, dtype=int)
    for i in range(len(elements)):
        elem = elements[i]
        start = np.min(np.where(elem.signal == 1))
        if n - start >= minLength:
            elem.plot = True
            indexes = np.append(indexes, i)
            averages = np.append(averages, np.mean(elem.signal[start:]))
    if len(averages) >= 10 or force:
        cuttoff = np.mean(KMeans(n_clusters=2).fit(averages.reshape(-1,1)).cluster_centers_)
        for i in np.flip(indexes[averages < cuttoff], 0):
            del elements[i]
    return elements
