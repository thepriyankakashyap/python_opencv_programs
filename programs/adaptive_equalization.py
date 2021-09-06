import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to the input image")
ap.add_argument("-c", "--clip", type=float, default=2.0,
	help="threshold for contrast limiting")
ap.add_argument("-t", "--tile", type=int, default=8,
	help="tile grid size -- divides image into tile x tile cells")
args = vars(ap.parse_args())

print("[INFO] loading input image...")
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("[INFO] applying CLAHE...")
clahe = cv2.createCLAHE(clipLimit=args["clip"],
	tileGridSize=(args["tile"], args["tile"]))
equalized = clahe.apply(gray)

cv2.imshow("Input", gray)
cv2.imshow("CLAHE", equalized)
cv2.waitKey(0)