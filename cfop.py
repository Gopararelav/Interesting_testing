import cv2 as cv
from PIL import ImageGrab, Image
import numpy
from time import sleep
# sleep(2)
# rl = ImageGrab.grab((836, 275+85, 1173, 541+125))
# d = list(rl.getdata())
d = [((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 0)), ((0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 0, 0)), ((0, 0, 255), (255, 0, 0), (0, 255, 0), (255, 0, 0))]
sc = numpy.array(d, dtype=numpy.uint8)
sc = cv.cvtColor(sc, cv.COLOR_BGR2RGB)
sc = cv.resize(sc, (400, 400))
cv.imshow("new", sc)
k = cv.waitKey(0)
cv.destroyAllWindows()
