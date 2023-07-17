import cv2
import numpy as np

def compare_fingerprints(image1, image2):
    fingerprint1 = cv2.imread(image1, cv2.IMREAD_GRAYSCALE)
    fingerprint2 = cv2.imread(image2, cv2.IMREAD_GRAYSCALE)

    fingerprint1 = cv2.resize(fingerprint1, (300, 400))
    fingerprint2 = cv2.resize(fingerprint2, (300, 400))

    hist1 = cv2.calcHist([fingerprint1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([fingerprint2], [0], None, [256], [0, 256])

    score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    if score > 0.6:
        return True
    else:
        return False

image1_path = 'images/1.png'
image2_path = 'images/2.png'

result = compare_fingerprints(image1_path, image2_path)
if result:
    print('Fingerprints are matching.')
else:
    print('Fingerprint are not matching.')
