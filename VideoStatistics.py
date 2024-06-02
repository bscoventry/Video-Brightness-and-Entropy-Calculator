#--------------------------------------------------------------------------------------------------------------
#Author: Brandon S Coventry          WITNe UW Madison   
#Date: 06/02/2024                     Lovely day in WISCo
#Updated Code from Marc
#--------------------------------------------------------------------------------------------------------------
import numpy as np
import cv2
import matplotlib.pyplot as plt
import statistics
import pdb 
import pandas as pd
from scipy.stats import entropy
def get_frames_brightness_complexity(filename):
    # Create a VideoCapture object 'video' to open the video file for reading.
    video = cv2.VideoCapture(filename)
    brightness_values = []
    entropyVec = []
    # Use a while loop to continuously read frames from the video until it's open.
    while video.isOpened():
        # Read the next video frame.
        ret, frame = video.read()

        # If 'ret' is True, the frame was read successfully.
        if ret:
            # compute average brightness/frame
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            avg = np.mean(hsv[:,:, 2]) 
            avg = (avg/255)*100
            brightness_values.append(avg)
            #Brandon Addition, calculate complexity from image histogram entropy
            # calculate mean value from RGB channels and flatten to 1D array
            gray_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            _bins = 256
            hist, _ = np.histogram(gray_image.ravel(), bins=_bins, range=(0, _bins))
            prob_dist = hist / hist.sum()
            frameentropy = entropy(prob_dist, base=2)
            entropyVec.append(frameentropy)
        else:
            # If 'ret' is False, it means there are no more frames to read in the video,
            # so we break the loop and stop the generator.
            break
    Avg_frame_entropy = np.mean(entropyVec)
    # Release the VideoCapture object to free up resources.
    video.release()
    #compute mean brightness
    avg_brightness = statistics.mean(brightness_values)

    return brightness_values, avg_brightness, entropyVec,Avg_frame_entropy
#List to iterate through videos
VidNames = ['VidA1.mp4','VidA2.mp4','VidA3.mp4','VidA4.mp4','VidB1.mp4','VidB2.mp4','VidB3.mp4','VidC1.mp4','VidC2.mp4','VidC3.mp4','VidD1.mp4','VidD2.mp4','VidD3.mp4','VidD4.mp4','VidE1.mp4','VidE2.mp4','VidE3.mp4','VidF1.mp4','VidF2.mp4','VidG1.mp4','VidG2.mp4','VidH1.mp4','VidH2.mp4','VidH3.mp4','VidH4.mp4','VidJ1.mp4','VidJ2.mp4']
#Setup the dataframe with the columns you want!
df = pd.DataFrame(columns=['VideoName', 'brightness_values', 'avg_brightness','Complexity_Vector','avg_frame_complexity'])
filenameBase = 'C://CodeRepos//Videos//'
#Loop through and calculate
for ck,vid in enumerate(VidNames):
    filename = filenameBase+vid
    print('Calculating'+' '+vid)
    [brightness_values, avg_brightness,complexity,avg_complexity] = get_frames_brightness_complexity(filename)
    #Add to dataframe
    df.loc[-1] = [vid,brightness_values,avg_brightness,complexity,avg_complexity]
    df.index = df.index + 1  # shifting index
    df = df.sort_index()  # sorting by index
#Now write to a user friendly csv file
df.to_csv('Brightness_Complexity.csv',index=False)
#pdb.set_trace()