import cv2
import numpy as np
img=cv2.imread('circle.png')

bilateral_filtered_image = cv2.bilateralFilter(img, 5, 175, 175)
cv2.imshow('Bilateral', bilateral_filtered_image)

edge_detected_image = cv2.Canny(bilateral_filtered_image, 75, 200)
cv2.imshow('Edge', edge_detected_image)

ret, contours, hierarchy = cv2.findContours(edge_detected_image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contour_list = []
for contour in contours:
    approx = cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    area = cv2.contourArea(contour)
    contour_list.append(contour)
    cv2.drawContours(img, contour_list,  0, (255,0,0), 5)
    cv2.imshow('Objects Detected',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
