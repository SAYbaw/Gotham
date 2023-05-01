# micro:bit Functions
## Programmer Defined Functions: Intro with the Pythagorean Theorem
### Create your variables
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2010.59.09%20AM.png)
### Create your functions
First, go to the command menu in the middle of the screen and click on the 'Advance' button.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2010.56.49%20AM.png)

Click on Functions.

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.00.21%20AM.png)
### Create function header for displaying an image.
Type the name 'displayImg' where it says 'doSomething'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-05-01%20at%2012.18.48%20AM.png)
### Make the function definition.
Place the following blocks into the function header.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-05-01%20at%2012.19.20%20AM.png)
### To save space in your work area, you can collapse the function definition
On the upper right hand corner of the fuction definition there is a up arrow '^' you can click or unclick...

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.04.40%20AM.png)

...and only the header will show.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.05.15%20AM.png)
### Create a function called 'pythagorean'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.07.39%20AM.png)
Under 'Edit Function' there is a row that says 'add a parameter' with a row of boxes. Click the box that says 'Number' twice.
### Add a return statement to the function header
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.10.29%20AM.png)
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.12.16%20AM.png)
### Add the Pythagorean formula to the return block
Go to the math menu and grab the 'square root' block.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.14.16%20AM.png)

Place it directly where it says '0' in the return block.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.15.13%20AM.png)

Go to the math menu and grab the '0 + 0' and place that in the '0' of square root.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.15.56%20AM.png)

Go to the math menu and grab 2 '0 x 0' and place them in each '0' of the '0 + 0'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.20.21%20AM.png)

Drag the 'num' from the fuction header and drag it into each '0' of the first '0 x 0' and then drag 'num2' into each '0' of the other '0 x 0'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.21.36%20AM.png)

### Go to the 'JavaScript' side to check your math
At the top of the screan click where it says 'JavaScript'
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2012.25.05%20PM.png)
Look for the function definition of 'pythagorean' in the code. If it looks like this, you did it correctly in blocks. If not, you can edit your JavaScript here and make the formula look like the picture below (**NOTE: Your line numbers for your function may be different than the picture.**). Remember, you can also add parantheses to force the order of operations.

      return Math.sqrt((num * num) + (num2 * num2))
      
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2012.25.40%20PM.png)
### In 'on start' let's "hard code" some values by initializing our variables.
By using 3 and 4 for 'height' and 'base' the answer will be '5.' You can add different numbers in there for further testing.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.26.17%20AM.png)
### Call our functions in a button event
Use 'button A+B' from input menu and place the following blocks into the event.
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.28.01%20AM.png)
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions1/Screen%20Shot%202023-04-28%20at%2011.30.41%20AM.png)

