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
    if color != 'red':
        # binary mask 
        maskedFrame = cv2.inRange(hsvFrame, lowerLimit, upperLimit)
    else:
        # binary mask 
        mask1 = cv2.inRange(hsvFrame, lowerLimit[0], lowerLimit[1])
        mask2 = cv2.inRange(hsvFrame, upperLimit[0], upperLimit[1])
        maskedFrame = cv2.bitwise_or(mask1, mask2)


    # Find contours in the binary mask
    contours, hierarchy = cv2.findContours(maskedFrame, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours based on minimum area to reduce noise
    valid_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 1000]

    if valid_contours:
        # Documentation: x1, y1, w, h = cv2.boundingRect(cnt)
        # Finding extreme points among all contours
        x_min = min([cv2.boundingRect(cnt)[0] for cnt in valid_contours])
        y_min = min([cv2.boundingRect(cnt)[1] for cnt in valid_contours])

        x_max = max([cv2.boundingRect(cnt)[0] + cv2.boundingRect(cnt)[2] for cnt in valid_contours])
        y_max = max([cv2.boundingRect(cnt)[1] + cv2.boundingRect(cnt)[3] for cnt in valid_contours])
        
        # Drawing one rectangle around all detected objects
        cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 255, 0), 8)


    cv2.imshow('Webcam View', frame)

    # If 'q' is pressed exit program
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()