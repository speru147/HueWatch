import cv2
from helper import colorRange

# Get user input for target color detection
color = input("What color would you like to detect? ")

# Initialize video capture from the default webcam (index 0)
webcam = cv2.VideoCapture(0)


# Infinite loop to continuously capture and display frames
while True:
    # Reading a frame from the webcam
    # ret: Boolean indicating if the frame was successfully captured
    # frame: The actual image frame captured from the webcam
    ret, frame = webcam.read()

    # Convert the frame from BGR to HSV color space
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the HSV range for the target color
    lowerLimit, upperLimit = colorRange(color)

    # Created a binary mask where:
    # White pixels represent areas within the target color range
    # Black pixels represent everything else
    maskedFrame = cv2.inRange(hsvFrame, lowerLimit, upperLimit)

    cv2.imshow('Webcam View', maskedFrame)

    # If 'q' is pressed exit program
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()