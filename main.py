import cv2
# Initialize video capture from the default webcam (index 0)
webcam = cv2.VideoCapture(0)

# Infinite loop to continuously capture and display frames
while True:
    # Reading a frame from the webcam
    # ret: Boolean indicating if the frame was successfully captured
    # frame: The actual image frame captured from the webcam
    ret, frame = webcam.read()

    cv2.imshow('frame', frame)

    # If 'q' is pressed exit program
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()