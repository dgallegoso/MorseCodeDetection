import numpy as np

MAX_MOVEMENT_RATIO = 1
MAX_SIZE_RATIO = .2
ALPHA = .2

class Element(object):
    def __init__(self, coord, rad, n):
        self.coord = coord
        self.rad = rad
        self.signal = np.append(np.zeros(n), 1)
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
    # if elements[0].signal[-1] == 1: print elements[0].rad
    return elements
