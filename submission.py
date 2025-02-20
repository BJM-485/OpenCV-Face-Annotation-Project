import cv2 as cv

# Global variables
vertex1 = None
vertex2 = None


def drawRectangle(event, x, y, flags, param):
    global vertex1, vertex2
    if event == cv.EVENT_LBUTTONDOWN:
        vertex1 = (x, y)
    elif event == cv.EVENT_LBUTTONUP:
        vertex2 = (x, y)
        # Draw the rectangle
        cv.rectangle(image, vertex1, vertex2, (255, 0, 0), 2, cv.LINE_AA)
        # Crop the region defined by the rectangle
        cropped_region = image[min(vertex1[1], vertex2[1]):max(vertex1[1], vertex2[1]),
                         min(vertex1[0], vertex2[0]):max(vertex1[0], vertex2[0])]
        # Save the cropped image
        cv.imwrite("face.png", cropped_region)


# Load the image
image = cv.imread('sample.jpg', cv.IMREAD_COLOR)

dummy = image.copy()

# Create a window and set the mouse callback function
cv.namedWindow("Window")
cv.setMouseCallback("Window", drawRectangle)

key = 0
while key != 27:
    cv.imshow("Window", image)
    cv.putText(image, '''Choose corner and drag, Press ESC to exit and c to clear''',
               (10, 30), cv.FONT_HERSHEY_SIMPLEX,
               0.52, (255, 255, 255), 2)
    key = cv.waitKey(1000) & 0xFF
    if key == 99:
        image = dummy

# Close all OpenCV windows
cv.destroyAllWindows()
