import cv2 as cv
import imutils
import argparse
import PreProcessing
import DetectShape


arg=argparse.ArgumentParser()
arg.add_argument("-i", "--image", required=True,help="ENTER THE IMAGE PATH")
args = vars(arg.parse_args())


image = cv.imread(args["image"])

resizedImage = imutils.resize(image, width=400)
ratio = image.shape[0] / float(resizedImage.shape[0])

thresh=PreProcessing.Pre(resizedImage)
c = cv.findContours(thresh.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
c= imutils.convenience.grab_contours(c)

image=DetectShape.Detect(image,c,ratio)

image=imutils.resize(image,width=800,height=800)
cv.imshow('FRAME',image)
k=cv.waitKey()
if k is ord('q'):
 cv.destroyAllWindows()