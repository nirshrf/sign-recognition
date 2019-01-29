import numpy
import cv2
import random

' left sign '
arr = cv2.imread("left.jpg")

' right sign '
#arr = cv2.imread("right.jpg")

orig = arr.copy()
cornerRight, cornerLeft = 0, 0

' filters on frame '
arr = cv2.inRange(arr, (200, 200, 200), (255, 255, 255))
arr = cv2.blur(arr, (2, 2))
arr = cv2.Canny(arr, 0, 100)

' finds sign circle '
circles = cv2.HoughCircles(arr, cv2.HOUGH_GRADIENT, 1, 50, param1=50, param2=30, minRadius=100, maxRadius=0)

' write circle on frame '
for circle in circles[0]:
    cv2.circle(orig, tuple(circle[:2]), circle[2], (0, 0, 255), 2)

' gets corners '
corners = cv2.goodFeaturesToTrack(arr, 8, 0.01, 10)

' find right and left corner quantity '
for corner in corners:
    cv2.circle(orig, tuple(corner[0]), 3, (0, 255, 0), -1)
    if corner[0][0] > (numpy.shape(arr)[1])/2:
        cornerRight += 1
    else:
        cornerLeft += 1

' writes the sign diraction '
if cornerLeft < cornerRight:
    cv2.putText(orig, "Sign is right", (25, 25), 3, 1, [0, 200, 255], 2)
else:
    cv2.putText(orig, "Sign is Left", (25, 25), 3, 1, [0, 200, 255], 2)

' shows processed signs '
cv2.namedWindow("signLeft", cv2.WINDOW_AUTOSIZE)
cv2.imshow("signLeft", orig)
cv2.namedWindow("signLeftProcessed", cv2.WINDOW_AUTOSIZE)
cv2.imshow("signLeftProcessed", arr)

' destroy windows on key press '
if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
