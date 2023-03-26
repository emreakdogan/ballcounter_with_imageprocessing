import cv2 # import  opencv library for image processing
import os # import os library for system operations
import numpy as np  # import the numpy library for mathematical operations
from PIL import Image # import the PIL library for image 
import base64  # import  base64 library for encoding the image in base64 format
import requests # import requests library for sending POST requests

# Define BGR values of colors
yellow = [0, 255 ,255] # yellow 
green  = [0, 255 ,0] # green 
red    = [0, 0, 255] # red 
blue   = [255, 0 ,0] # blue 

video = cv2.VideoCapture('video.mp4') # open the video file
current_frame=0 # Initialize current_frame to 0 to keep track of the current frame


def get_color_limits(color): # function:  to get the lower and upper limits of a color
    clr = np.uint8([[color]])
    hsv_color = cv2.cvtColor(clr,cv2.COLOR_BGR2HSV)
    
    lower_limit = hsv_color[0][0][0] - 10, 100, 100
    upper_limit = hsv_color[0][0][0] + 10, 255, 255
    
    lower_limit = np.array(lower_limit,dtype=np.uint8)
    upper_limit = np.array(upper_limit,dtype=np.uint8)
   
    return lower_limit,upper_limit



def find_count_contours(mask): # function:  to find contours and count them
    contours_number = 0
    contours, hierarchy = cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        cv2.drawContours(frame,[contour],-1,(255,255,255),5)
        contours_number +=1 
    
    return contours_number

# loop over all the frames in the video
while (True):
    is_success, frame = video.read()  # read  frame from the video
    frame = frame[:,:frame.shape[1]//2] # take only the left half of the frame
    
    hsvImage = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # convert the frame from BGR to HSV color space
    
    
    #lower_limit, upper_limit = get_color_limits(red) # get lower_limit and upper_limit for color
    #mask = cv2.inRange(hsvImage,lower_limit, upper_limit) # create a mask for the color we want to detect 
    
    # perform such an operation only for the red color. You can use get_color_limits function for other colors  
    mask1 = cv2.inRange(hsvImage, (0, 70, 50), (10, 255, 255))
    mask2 = cv2.inRange(hsvImage, (170, 70, 50), (180, 255, 255))  
    mask = cv2.bitwise_or(mask1, mask2)  
      
    
    mask_array = Image.fromarray(mask) # get mask object in different format
    bounding_box = mask_array.getbbox() # get the bounding box(x1,y1,x2,y2) of the object in the mask
    
    
    if bounding_box is not None: # if a bounding box is found, draw a rectangle around it
        x1,y1,x2,y2 = bounding_box
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,255),5)  

    cv2.imshow('Frame', frame) # if we want to see our frame with rectangle instantly 
    
    if find_count_contours(mask)>3: # If the number of red ball in the frame is more than 3, send a warning
        print(f"Red Ball:{find_count_contours(mask)}") # when the number of red balls more than 3, we print the number of red balls on the terminal screen
        cv2.imwrite('./warning_frames/frame' + str(current_frame) + '.jpeg', frame) # save the frame where the number of red balls more than 3 in jpeg format.
        
        with open('./warning_frames/frame'+str(current_frame)+".jpeg", "rb") as image_file:      #base64 encode for image
            encoded_image = base64.b64encode(image_file.read())

        url = 'https://eldercare.unknownland.org/red_ball' # the address where we will send the POST request.
        
        data = {                                           # JSON data to be sent in the POST request
        'red_ball':  find_count_contours(mask),
        'picture': encoded_image.decode('utf-8')
            }
        
        response=requests.post(url, json=data)  # sending a request with the POST method
        
        print(response.status_code)  # print the response to check if the POST method is working
    current_frame+=1 # increase current_frame 
    
    if cv2.waitKey(1) & 0XFF == ord('q'): # condition to be able to exit the video when it ends or when we want to leave.
        break
    
cv2.destroyAllWindows() # close all windows