import cv2 # import  opencv library for image processing
import os # import os library for system operations

video = cv2.VideoCapture('video.mp4')  # open the video file

current_frame = 0 #  # Initialize current_frame to 0 to keep track of the current frame

if not os.path.exists('frames'): # create a folder if it does not exist to save the images 
    os.makedirs('frames')

while (True):
    is_success, frame = video.read() #  # read frame from the video

    cv2.imshow('Frame', frame) #  if we want to see our frame 
    cv2.imwrite('./images/frame' + str(current_frame) + '.jpeg', frame) # save frame
    current_frame += 1 # increase current_frame
    if cv2.waitKey(1) & 0XFF == ord('q'): # condition to be able to exit the video when it ends or when we want to leave.
        break

cv2.destroyAllWindows() # close all windows