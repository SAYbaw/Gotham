# micro:bit Functions Part 3
## Programmer Defined Functions: User input and passing arrays to functions

**open ['functions' in micro:bit](https://makecode.microbit.org/) and add the following to it**

### Create your variables
Add arrayIndex, choice, evens, and odds to your variable list
*NOTE: You **DO NOT** have to create a variable named* **list**

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/00.png)

### From the block menu, click on Advanced then Arrays
Select two 'set' blocks from the array menu(it is the first block under 'Create').

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/01.png)
### Place them in 'On start'
Change the 'set list v' by clicking on the down arrow to the right of 'list' and select 'evens' for one block and 'odds' for the other. Each array will hold 3 elements. Click on the '+' on the right hand side of the 'set' block to increase the array size from 2 to 3. Type the numbers in each array as pictured below

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/02.png)
### Create a function header called 'getUserChoice' and add an 'array' as a parameter 
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/03.png)
### In the 'getUserChoice' definition block, place a 'set' block from the variables menu
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/04.png)
### Go to the Array menu and get this block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/05.png)
### Place it inside the '0' of the 'set' block
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/06.png)
### Drag the parameter 'list' and place it where it says 'list v' in the 'list v get value at 0'
*NOTE: EVEN THOUGH THEY ARE BOTH CALLED* list *YOU MUST MAKE SURE YOU DO THIS*

This is because when you bring a 'set' block into your project, MakeCode automatically generates a variable called 'list.' We want to use the PARAMETER we created called 'list' instead.

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/07.png)

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/08.png)
### Add an 'if else' block from the logic menu
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/09.png)
### Add a '0 = 0' comparator from the logic menu
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/10.png)
### Complete your function definition
![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/11.png)
### Get an 'on button A' event from input menu
Add a 'show number' block from the basic menu

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/12.png)

### Get oval version of 'call getUserChoice' from function menu
click the 'v' inside the red oval 'list v' and select 'evens' from the dropdown menu

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/13.png)

![](https://github.com/SAYbaw/Gotham/blob/main/images/microbit/functions3/14.png)
