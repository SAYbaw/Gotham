# micro:bit Advanced Button Logic
## Analog Rotary Emulation: Volume Control with Visual Display
## *NOTE: Make sure to creat a new project called 'volume' in micro:bit.

### Create your variables
Those that are in all caps are called constants. This is good practice to easily identify them. These values will not change during run time. We use constants instead of just using 'magic' numbers that are not descriptive. Also, if we need to change their value for whatever reason later, we only need to change it in one place.
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-18%20at%2011.28.25%20AM.png)
### Initialize your variables and constants
Notice we are using a different scale for this volume project. Therefore, we need to change CLICK_MAX and clickCt to 5 because we only have 5 rows of LEDS for our visual display. 

![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-18%20at%209.33.18%20AM.png)
### Button A
You are going to create your button logic the same way you did for your [brightness/volume project](https://github.com/SAYbaw/Gotham/blob/main/microbit_Brightness_Guide.md) (WITHOUT THE CODE FOR BRIGHTNESS) with a few aditional steps for the display. We want our visual display for volume to change the ENTIRE row of LEDs as we go up and down (button B and A), however, we can only plot one LED at a time. So we ar going to use a 'for' loop to plot all the horizontal LEDs in each row so the appear and disappear at once. The looping of the LED's one by one in a row is inperceptable by the human eye, so it will appear to turn on and off instantly. First we are going to grab a 'for' loop from Loops. The variable index is included in the 'for' loop so you DO NOT HAVE TO CREATE AN index variable. All you need to do is drag the index red oval from the loop header (the top of the loop block) and drag it into your x variable of your unplot/plot block. The XY coordiantes of the LED display are like this...
| 0 | 1 | 2 | 3 | 4 |
| :---: | :---: | :---: | :---: | :---: |
| 0,0 | 1,0 | 2,0 | 3,0 | 4,0 |
| 0,1 | 1,1 | 2,1 | 3,1 | 4,1 |
| 0,2 | 1,2 | 2,2 | 3,2 | 4,2 |
| 0,3 | 1,3 | 2,3 | 3,3 | 4,3 |
| 0,4 | 1,4 | 2,4 | 3,4 | 4,4 |

As you can see from this grid, the second coordinate y (our rows) increases as we go down the grid. 
This means, if we are lowering our volume (decreasing our clickCt by -1 with button A), then we need to INCREASE our yCt by 1 and do the opposite when we increase volume with button B (change yCt by -1). Make sure to change your yCt by 1 (or -1) OUTSIDE of your 'for' loop. Here is the button A code.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-18%20at%209.34.38%20AM.png)
### Button B
Same logic as button A but now you are increasing volume. You need to change clickCt by 1 and yCt by -1. Instead of uplotting LEDs to turn them off, we are plotting LEDs to turn them on. So we use this block instead.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-18%20at%209.36.05%20AM.png)

