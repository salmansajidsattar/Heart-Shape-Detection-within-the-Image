import cv2 as cv
import imutils
def Detect(image,c,ratio):
    for cnt in c:
        shape = "unidentified"
        M = cv.moments(cnt)
        try:
         cX = int((M["m10"] / M["m00"]) * ratio)
         cY = int((M["m01"] / M["m00"]) * ratio)
        except:
          print('some thing went wrong')
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.04 * peri, True)
        if len(approx) == 3:
            shape = "triangle"
        elif len(approx) == 4:
            (x, y, w, h) = cv.boundingRect(approx)
            ar = w / float(h)
            shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
        elif len(approx) == 5:
            shape = "HEART"
        else:
            shape = "HEART"
        cnt = cnt.astype("float")
        cnt *= ratio
        cnt = cnt.astype("int")
        if (shape == "HEART"):
            cv.drawContours(image, [cnt], -1, (250, 250, 210), 5)
            cv.putText(image, shape, (cX, cY), cv.FONT_HERSHEY_PLAIN, 1.5, (250, 250, 210), 3)
    return image