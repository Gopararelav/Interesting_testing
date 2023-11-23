import cv2 as cv
from PIL import ImageGrab
import numpy
sc = ImageGrab.grab()
sc = numpy.array(sc)
sc = cv.cvtColor(sc, cv.COLOR_BGR2RGB)
sc = cv.resize(sc, (1300, 700))
cv.imshow("new", sc)
k = cv.waitKey(0)
cv.destroyAllWindows()
