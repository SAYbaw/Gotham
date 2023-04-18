# micro:bit Advanced Button Logic
## Analog Rotary Emulation: Volume Control with Visual Display
### Create your variables
Those that are in all caps are called constants. This is good practice to easily identify them. These values will not change during run time. We use constants instead of just using 'magic' numbers that are not descriptive. Also, if we need to change their value for whatever reason later, we only need to change it in one place.
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-18%20at%2011.28.25%20AM.png)
### Initialize your variables and constants
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-18%20at%209.33.18%20AM.png)
### Button A
You are going to create your button logic the same way you did for your [brightness/volume project](https://github.com/SAYbaw/Gotham/blob/main/microbit_Brightness_Guide.md) (WITHOUT THE CODE FOR BRIGHTNESS) with a few aditional steps for the display. We want our visual display for volume to change the ENTIRE row of LEDs as we go up and down (button B and A), however, we can only plot one LED at a time. So we ar going to us a 'for' loop to plot all the horizontal LEDs in each row so the appear and disappear at once. The looping of the LED's one by one in a row is inperceptable by the human eye, so it will appear to turn on and off instantly. The coordiantes of the LED display is like this...
| 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: |
|*|*|*|*|*|
|*|*|*|*|*|
|*|*|*|*|*|
|*|*|*|*|*|
|*|*|*|*|*|

