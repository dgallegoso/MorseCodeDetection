import numpy as np
from sklearn.cluster import KMeans

MAX_MOVEMENT_RATIO = 1.5
MAX_SIZE_RATIO = .5
ALPHA = .3
NONMAX_COUNTER = 1

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

def eliminate_noise(elements, minLength, force):
    n = len(elements[0].signal)
    averages = np.empty(0, dtype=float)
    indexes = np.empty(0, dtype=int)
    print '-'*80
    for i in range(len(elements)):
        elem = elements[i]
        start = np.min(np.where(elem.signal == 1))
        if n - start >= minLength:
            elem.plot = True
            indexes = np.append(indexes, i)
            mean = np.mean(elem.signal[start:])
            # Attempt at filtering out lights that are permanently on
            # If it doesn't work then just use the commented out metric
            # It works well on data without permanent lights
            metric = 32 * (mean * (1 - mean))**5 + np.sum(elem.signal)/float(n)
            # metric = mean + np.sum(elem.signal)/float(n)
            averages = np.append(averages, metric)
            print np.sum(elem.signal[start:]), metric
    if len(averages) >= 10 or (force and len(averages) > 2):
        cuttoff = np.mean(KMeans(n_clusters=2).fit(averages.reshape(-1,1)).cluster_centers_)
        # print indexes[averages < cuttoff], cuttoff
        for i in np.flip(indexes[averages < cuttoff], 0):
            del elements[i]
    return elements

def merge_similar(elements, minLength, force):
    if np.random.rand() > .05 and not force:
        return elements
    n = len(elements[0].signal)
    toDelete = []
    # print '-'*80
    for i in range(len(elements)):
        elem = elements[i]
        start = np.min(np.where(elem.signal == 1))
        for j in range(len(elements)):
            x = elements[j]
            startx = np.min(np.where(x.signal == 1))
            if startx >= start and (n - startx) >= minLength*4 and i != j and i not in toDelete:
                corr = np.corrcoef(elem.signal[startx:], x.signal[startx:])[0,1]
                # print corr, i, j
                if corr > .8:
                    # Instead of combining both might want to simply delete one
                    temp = elem.signal[startx:] + x.signal[startx:] + np.random.rand() - .5
                    elem.signal[startx:] = (temp > 1).astype(int)
                    toDelete.append(j)
    for i in sorted(toDelete, reverse=True):
        del elements[i]
    return elements

def prune_noise(elements, minLength=50, force=False):
    if len(elements) == 0:
        return elements
    elements = merge_similar(elements, minLength, force)
    elements = eliminate_noise(elements, minLength, force)
    return elements
