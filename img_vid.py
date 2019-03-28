import cv2
import numpy as np
import os
 
from os.path import isfile, join

def old():
    for i in range(len(files)):
        filename=pathIn + files[i]
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
        print(frame_array)
def convert_frames_to_video(pathIn,pathOut,fps,str):
    frame_array = []
    #files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]
 
    #for sorting the file names properly
    for i in range(len(str)):
        
        filename=pathIn + str[i] +'.jpg'
        print(filename)
        #reading each files
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        #print(filename)
        #inserting the frames into an image array
        frame_array.append(img)
        print(frame_array)
    
 
    
    
 
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
 
    for i in range(len(frame_array)):
        # writing to a image array
        print('i',i)
        out.write(frame_array[i])
    out.release()
 
def main():
    pathIn= './dat/'
    pathOut = 'video.avi'
    fps = 1
    str = 'helloo'
    convert_frames_to_video(pathIn, pathOut, fps,str)
 
if __name__=="__main__":
    main()
