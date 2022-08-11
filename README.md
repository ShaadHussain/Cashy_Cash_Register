# Ca$hy! - A Cash Register for all your "changing" needs
Welcome! To use Ca$hy, please visit this [link](https://O3QIP6IQVRRRSRXS.anvil.app/MLA4SG3FOOJRTPCNLX5CVKWK).

## About 
Ca$hy is a cash register web app that takes a given price and payment and outputs the change in the least amount of coins/bills.

The app was written in Python and uses Anvil, a Python-only full-stack framework for building and publishing web apps quickly. 

## Assumptions

There were a couple of assumptions made for the design of this app.

The first is that I assumed that when a transaction was conducted, the register would be replenished *after* the change was given out. 
This coincides with the example given in the description of the transaction of $1 - 0.89¢ with zero dimes in the register. 
Although that 0.89¢ would put 1 dime (as well as 1 50¢ piece, 1 quarter, and 4 pennies) into the register, the description asked for 
a return value of 2 nickels and 1 penny, indicating that the register should be replenished after the change is given out. 

The second assumption is that the user has the ability to update the register. Although this wasn't explicitly specified in the project description, 
it made sense for testing purposes because the user may want to simulate different scenarios where the register may not have a certain amount of one coin/bill,
and they would need to compensate with other coins/bills. To see why this might be necessary, take the prior example of $1 - 0.89¢ with no dimes in the register. For this to work and return 2 nickels and 1 penny, the default number of dimes in the register would have to be 0. But does the user want
the number of dimes to be 0 for all of the transactions they test? Probably not, they may wish to see the amount they would get back with no shortages. All in all, it made more sense to have more flexibility in this area as opposed to less.


## Testing
To view unit tests for this app, please view tests/register_test.py. This file tests the corresponding register.py in the same directory. Please note that
while the code is not verbatim the code written for the Anvil app (see anvil_app_files/Form for that), the logic is exactly the same and the only differences
are due to implementing the logic within Anvil's UI components. 

The testing framework used was pytest, and the unit tests test the change logic, the register replenishing logic, invalid input, and a variety of 
possible transactions for the changemaking function. Manual testing was also performed on the Anvil GUI. 

## Design and Development Decisions

There are some design/development decisions I felt were worth commenting on. The first and perhaps the most obvious one is the choice to use Anvil to create and deploy my app. While I had initially had my mind set on Flask due to my past experience with it, I researched other tools anyway and wound up discovering Anvil. Being a full-stack Python tool where I could essentially write everything in Python and publish in a matter of seconds, Anvil seemed like the perfect solution for building Ca$hy. Its drag-and-drop interface meant I wouldn’t have to worry as much about tinkering with front-end code and databases, which would allow me to focus on getting an app up and running as quickly as possible and iterating just as quickly. 

The great thing was that using Anvil was indeed fast. I could toy with changes and iterate on the app quickly, and publish and test easily. However, given that Anvil is still a fairly young technology, a major downside to it is its lack of flexibility. This is especially in regard to front-end design. The drag-and-drop interface ended up being a double-edged sword, as Anvil doesn’t allow the developer much access to the CSS it builds the UI on (the feature had been available in the past but was disabled), and as a result I wasn’t able to build the UI I had in mind, instead being relegated to some preset templates and fonts. While I was able to manage to design and fit in a logo thanks to Canva, I do wish I had more flexibility to toy around with the CSS that working with Flask and a traditional front-end framework like React would have provided me in order to achieve a more modern design. Despite this, Anvil is still a great tool and I’m glad I discovered it, and I’m sure it will evolve to the point where it gives the developer greater control over their app’s look and feel. 


---
That's about it, please enjoy the app! If you have any feedback, please feel free to let me know. Thank you!
