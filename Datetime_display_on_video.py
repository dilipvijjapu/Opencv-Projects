import cv2
import datetime

# define a video capture object
vid = cv2.VideoCapture(0)

while (vid.isOpened()):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    font = cv2.FONT_HERSHEY_SIMPLEX
    tim=str(datetime.datetime.now())
    frame=cv2.putText(frame,tim,(10, 50),font,1,(0,255,0),2,cv2.LINE_AA)
    cv2.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()