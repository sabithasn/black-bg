import numpy as np
import cv2
my_img_1 = np.zeros((512, 512, 1), dtype = "uint8")
cv2.imshow('Single Channel Window', my_img_1)
my_img_3 = np.zeros((512, 512, 3), dtype = "uint8")
cv2.imshow('3 Channel Window', my_img_3)
cv2.waitKey(0)
cv2.destroyAllWindows()
