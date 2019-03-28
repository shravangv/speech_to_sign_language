import pygame
import speech_recognition as spr 
import time
import cv2
import numpy as np
import os
 
from os.path import isfile, join


def speech_to_text():
    sample_rate = 48000
    chunk_size = 2048 
    r = spr.Recognizer() 
     
    with spr.Microphone(sample_rate = sample_rate, chunk_size = chunk_size) as source: 
            r.adjust_for_ambient_noise(source) 
            print("Say Something")
            audio = r.listen(source)
           # print(type(audio))
            text='could not recognize'
            try:
                    text = r.recognize_google(audio) 
                    print("you said: " + text)
            
            except spr.UnknownValueError: 
                    print("Google Speech Recognition could not understand audio") 
            
            except spr.RequestError as e: 
                    print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    return text


def run():

    text = speech_to_text()
    #text = 'hi'
    #text= text+text[-1]
    print('receieved',text)

    text_list = list(text)
    pygame.init()


    modes = pygame.display.list_modes()
    #pygame.display.set_mode(max(modes))
    pygame.display.set_mode([600,600])
    
    screen = pygame.display.get_surface()
    pygame.display.set_caption('final result')
    pygame.display.toggle_fullscreen()
    clock = pygame.time.Clock()
    crashed = False
    waittime = 1000
    while(not crashed):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
        try:
            #print(text_list)
            if(text_list[0]==' '):
                img = pygame.image.load('./dat/space'+'.png')
            else:
                img = pygame.image.load('./dat/'+text_list[0]+'.jpg')
            #print(text_list)
            text_list.pop(0)
            #print(text_list)
            #print("!!!!!")
            img = img.convert()
            # rescale the image to fit the current display
            img = pygame.transform.scale(img, [600,600])
            screen.blit(img, (0, 0))
            pygame.display.flip()
            #print("!")

            #input(pygame.event.get())
            clock.tick(200)
            time.sleep(1)
            #print('1')
        except pygame.error as err:
            #print ("Failed to display %s: %s" % (file_list[current], err))
            pass
        except:
            text_list = list(speech_to_text())
            pass
        # When we get to the end, re-start at the beginning
        #current = (current + 1) % num_files;
