# speech_to_sign_language
  A project which recognises input voice and gives an output in the form of animated graphics


# Problem Statement

Communication is the main channel between people to communicate with each other. Deaf and mute people find difficulties to communicate with normal persons. This huge challenge makes them uncomfortable and they feel discriminated in society. Since mute people cannot communicate easily, they depend on some sort of visual communication. Sign language is commonly used by them to interact with the rest of the world. Similarly, deaf people also require aids to understand what is being spoken to them. Our project is aimed at helping these specially challenged people hold equal par in the society by allowing effective communication between all parties.

# Our Proposed Solution

Our application tries to solve problems of both mute and deaf people by converting the hand gestures to text and voice
simultaneously and vice versa in real time. The solution utilises a convolutional neural network running on Tensor Flow to detect hand gestures corresponding to different letters. These letters are converted to words and eventually to speech. For people who are hard of hearing we convert the speech of a person communicating to them into Sign Language. 

## Files Description

1.Test.py - A module used to perform text to speech conversion based on PyTTXs engine.

2. `img_vid.py` - A module used to convert a stream of images to a video sequence. It is used to generate a video feed of sign languages for the deaf to recognise and understand.

3. `voice_try.py` - A module used to convert speech to text using Google API.

4. Socket.py - A socket connection is established for communication with a client using TCP. The Socket API is used for implementing a bind and listen to wait for incoming connections. Symmetric Encryption has been implemented in the socket for communicating with a client based on Public and Private Keys. Once a connection with the client is established, an audio feed is transferred to the client for generation of sign language for the dead people.

5. Client.py - A client is used to connect to the socket. The sign language is displayed on a Pygame Window based on the incoming video feed.

6. Threshold Histogram.py : This module is used for detecting gestures. We segregate the portion of hand from the image. We have OpenCV thresold library to implement this. Next iteration will contain code for gesture detection for sign language.

7. Speech to Sign Language: We have used pygame to display a stream of signs based on the audio feed given by the user. 

Till now we have established modules required for our project. From now on we will work on proper integration and UI.

## Requirements

1. wave
2. opencv 
3. numpy
4. pygame

## Screenshots


Tkinter Window for recording audio.


Sign Language Output produced in Pygame for a given input speech waveform
