# DRAGCOLOUR

 Color detection is the process of detecting the name of any color. Simple
isn’t it? Well, for humans this is an extremely easy task but for computers, it
is not straightforward. Human eyes and brains work together to translate
light into color. Light receptors that are present in our eyes transmit the
signal to the brain. Our brain then recognizes the color.
The libraries that are used are as following:-
Numpy opencv-contrib
Then we will create RGB track paths using command cv2.createTrackbar.
Firstly we will capture the image by using our primary camera and the
 output of that capture image will be shown on the window called “Test”.
 
 
As we have already made the trackbars in the previous step now we will
 store the positions of trackbar in the variables. In this case it is r, g and b.
 Now we will give 2 conditions one for the upper range of the color and the
other lower range of the color and obtain the colors lying between these
ranges and the colors outside the ranges will become black due to bitwise
operations.
Now we will be showing the obtained colors in a new window called res by
 applying the mask which we defined earlier.
 
