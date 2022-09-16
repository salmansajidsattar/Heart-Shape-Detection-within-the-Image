import cv2 as cv
def Pre(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    thresh = cv.threshold(blurred, 245, 255, cv.THRESH_BINARY_INV)[1]
    return thresh
