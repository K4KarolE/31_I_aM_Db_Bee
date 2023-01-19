'''
- Active / inactive radio button
    + inactive: grayed out?
- OpenCV or in still in browser?
- options for all 3 diff. sizes + all?
- roll down window for selecting the size?
'''

import sys # to access the system
import cv2
img = cv2.imread("yingyang.jpg", cv2.IMREAD_ANYCOLOR)

while True:
    cv2.imshow("Ying Yang", img)
    cv2.waitKey(0)
    sys.exit() # to exit from all the processes

cv2.destroyAllWindows() # destroy all windows

