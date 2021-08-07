import cv2
import numpy as np
import matplotlib.pyplot as plt

print("done importing libraries and functions")

def display(frame_name, frame):
    cv2.imshow(frame_name, frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
