# micro:bit Advanced Button Logic
## Analog Rotary Emulation: Brightness Control
### Create your variables
Those that are in all caps are called constants. This is good practice to easily identify them. These values will not change during run time. We use constants instead of just using 'magic' numbers that are not descriptive. Also, if we need to change their value for whatever reason later, we only need to change it in one place.
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.20.53%20PM.png)
### Initialize your variables and constants
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.21.55%20PM.png)
### Button A and B
Get 2 button events from inputs. make sure to change one of them to 'B.' The 'If else' block is in the logic section, the 'set brightness' block is in the Led section (click on ...more) and the change & set blocks are in the variables section. Make sure you change the appropriate variable using the down arrow in the block. To put the proper math formula into the set brightness block, follow the directions below 'Converting Bit values to a 10 point scale (0-9).'
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.22.27%20PM.png)
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.22.46%20PM.png)
### Converting Bit values to a 10 point scale (0-9) for 'set brightness' above
The brightness attribute of the LEDs is a range from 0 to 255. The number 255 is used often because that is the the largest number that can be stored in one binary byte or 8 bits. However, our users expext neat, decimal ranges like 10 or 100. Therefore we must convert the bit value to our scale. The formula is (bit value max/highest scale value) * current scale level or (255/9) * click count. In block programming, there are no parantheses, so to get the math right...
### 1. From the Math menu grab a '0 * 0' block and place it in the 'set brightness' block
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.28.56%20PM.png)
### 2. Put a '0 / 0' block into the first '0' of the '0 * 0' block
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.29.31%20PM.png)
### 3. Place the variables in the appropriate order in the formula replacing the zeros
![alt text](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-16%20at%204.30.21%20PM.png)
## Adding Volume Control
### Add a variable
Add MAX_VOLUME
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-17%20at%209.23.27%20AM.png)
### Define (set) MAX_VALUE and add a sound to the 'On Start' Block
'Set volume' block is in the Music section
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-17%20at%209.24.03%20AM.png)
### Add 'Set volume' and some kind of tune or tone from music to each button event (button A and button B)
Place in the 'if' section of the 'if else' block of buttan A and button B. Make sure it is placed after the 'change clickCt' block. The formula for 'set volume' is the same as the brightness, just with MAX_VOLUME. If you have a long tune playing on start, then you do not have to add another tone or tune here but it may be easier for testing to triger a new tone or tune on each button click.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/Screen%20Shot%202023-04-17%20at%2012.04.46%20PM.png)
