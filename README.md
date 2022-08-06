# Ca$hy! - A Cash Register for all your "changing" needs
Welcome Benetech team! To use the app, please visit this [link](https://O3QIP6IQVRRRSRXS.anvil.app/MLA4SG3FOOJRTPCNLX5CVKWK).

##About 
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
are due implementing the logic within Anvil's UI components. 

The testing framework used was pytest, and the unit tests test the change logic, the register replenishing logic, invalid input, and a variety of 
possible transactions for the changemaking function. 



