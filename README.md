# Circle-Detection-UAV
A python program using OpenCV to detect target circles on the ground in order to drop a humanitaian aid package on the target.

1. circleColour.py

This program makes use of the colour of the circle to detect it by converting RGB colourspace to HSV first.

2. Circle_Detection.py

This program uses Contour detection and contour shape and area approximation for detecting circles. This program gives the best result for a video (moving circle).

3. circleDetectImage.py

This program detects circles in an image using contour detection and approximation.

4. circleDetectMoments.py

Instead of using contour are approximation this program uses the moments() function along with contours to detect circles.

5. houghCircle.py

Thisprogram makes use of the inbuilt hough transform function to detect shapes in a frame.
