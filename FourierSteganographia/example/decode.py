import numpy  as np
import matplotlib.pyplot as pyplot
import cv2

img         = cv2.imread("./question.png", cv2.IMREAD_GRAYSCALE)
spectrum    = np.fft.fft2(img)
spectrumlog = np.log(abs(spectrum)) * 20 

cv2.imwrite("./solve.png", np.abs(spectrumlog))