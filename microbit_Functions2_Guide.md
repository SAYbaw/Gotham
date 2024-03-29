# micro:bit Functions Part 2
## Programmer Defined Functions: Timing Mechanisms

**open ['functions' in micro:bit](https://makecode.microbit.org/) and add the following to it**

### Create your variables

Add deltaTime, isRunning and startTime to your variables
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-28%20at%202.31.32%20PM.png)

### Initialize isRunning to False in on start
Grab a false block from the logic menu
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.11.46%20PM.png)

### Create a function header called 'timer' that takes one number parameter
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.06.20%20PM.png)

### Create a function header called 'deltaTime' that takes one number parameter
In the function definition of getDeltaTime, place a '0 - 0' from math and place it in the '0' of a return block.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.17.20%20PM.png)

### From the input menu '...more', get the 'running time (ms)' variable
click on input menu (pink) then click '...more'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.18.20%20PM.png)

### Complete deltaTime function definition
Put 'running time (ms)' into first '0' of the '0 - 0' and drag 'num' from function header into second '0'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.19.09%20PM.png)

### Create a function header called 'convertMilli' that takes one parameter
In the function definition of getDeltaTime, place a 'square root' from math and place it in the '0' of a return block. Click on the down arrow next to 'square root' for a drop down menu of other options and select 'integer division'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.22.19%20PM.png)
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.22.57%20PM.png)

### Drag 'num' from function header into first '0' and type 1000 into second '0'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-05-01%20at%2011.57.38%20AM.png)

### In the timer definition, place the following blocks.
Grab the 'pause (ms)' from the basic menu and select from the dropdown (next to the white circle with the number in it) 1 second or 1000 ms. We need our for loop to start with the value of num and go to 1 so therefore we have to edit it in JavaScript.

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.30.40%20PM.png)

### Switch over to JavaScript to force edit 'for' loop block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.39.32%20PM.png)

### Look for timer definition in the JavaScript code
*NOTE: YOUR LINE NUMBERS MAY NOT BE THE SAME AS THOSE PICTURED. LOOK FOR THE WORD...* **function timer** *FOLLOWED ON THE NEXT LINE BY THE WORD* **for (**
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%209.41.12%20PM.png)

### A close up on the 'for' loop
*NOTE: YOUR INDEX VARIABLE WILL MOST LIKELY BE NAMED* index2 *THAT IS OK*
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-05-01%20at%2012.37.04%20PM.png)

### Edit the 'for' loop in JavaScript

    for (let index2 = num; index2 > 0; index2--)
Change the first 0 to [num], <= 4 to [> 0] and index2++ to [index2--]. This will make our timer count down instead of up. 
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-05-01%20at%2012.45.20%20PM.png)

### Switch back to blocks. 
This is what your timer function should look like when complete EXCEPT your index variable will be index2.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-05-01%20at%2012.39.00%20PM.png)

### Get isRunning from Variables and bring it over to your 'forever' block
You are going to place it directly into the if statement block. You DO NOT need a comparator from the logic menu. It may look like it will not fit but it does.

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.22.32%20PM.png)

### isRunning will fit and snap in place in the conditional area (the place where it says 'true v' in the header of the 'if' block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.22.54%20PM.png)

### From the led menu get a 'toggle x 0 y 0' block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.24.29%20PM.png)

### Place in the 'if' block of the 'forever' block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.25.09%20PM.png)

### Finally, add a 'pause' from the basic menu to the 'forever' block code
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.27.34%20PM.png)

### Get 'on Logo pressed' from input menu
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.32.31%20PM.png)

### The oval versions of call getDeltatime and call convertMilli will be used in the 'on logo pressed v' event
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.40.45%20PM.png)

### Place the following code in the 'on logo pressed v' event
Place the variable 'startTime' in the '1' place of the getDeltaTime function call and get a 'false' block from logic to set isRunning to false

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.41.55%20PM.png)

### Complete the 'else' clause of the 'if else' block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.46.16%20PM.png)

### Finally grab an 'on shake v' event from the input menu
Grab the call timer function block from the function menu and put a 3 as the argument for testing purposes
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions2/Screen%20Shot%202023-04-30%20at%2011.48.37%20PM.png)


