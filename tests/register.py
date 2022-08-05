import csv

currency_map = {}

def p(val):
    print(str(val))
def init_curr_map():
    # global currency_map

    # currency_map[0.01] = 200
    # currency_map[0.05] = 200
    # currency_map[0.1] = 170
    # currency_map[0.25] = 170
    # currency_map[0.5] = 30
    # currency_map[1.0] = 150
    # currency_map[5.0] = 100
    # currency_map[10.0] = 100
    # currency_map[20.0] = 150

    currency_map[0.01] = 10
    currency_map[0.05] = 10
    currency_map[0.1] = 10
    currency_map[0.25] = 10
    currency_map[0.5] = 10
    currency_map[1.0] = 10
    currency_map[5.0] = 10
    currency_map[10.0] = 10
    currency_map[20.0] = 10

    return currency_map


# Taking the user's payment (deposit) and allocating it to register
def replenishRegister(deposit, register_map):
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

    deposit = round(deposit, 2)

    print(f"Deposit: {deposit}")

    for amount in amounts:
            while deposit >= amount:

                register_map[amount] += 1
                deposit -= amount

                deposit = round(deposit, 2)

                # replenishing the register by adding to it


def makeChange(price, payment, register_map):

    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

    user_change_map = {}

    try:
        price = float(price)
        payment = float(payment)
    except ValueError:
        return "Error! Values are not numbers"

    if payment < 0 or price < 0:
        return "Error! Non-negative numbers"
    
    change = (payment - price)

    change = round(change, 2)

    print(f"Change b4 loop: {change}")


    if change > 0:
        
        '''print(f"Register map before replenishing: {register_map}")
        # replenishRegister(price, register_map) # adds the payment - change to the register
        print(f"Register map AFTER replenishing: {register_map}")'''

        for amount in amounts:
            while change >= amount and register_map[amount] != 0:

                print(f"Curr amount: {amount}")
                print(f"Curr change before: {change}")

                change -= amount

                print(f"Curr change after: {change}")

                change = round(change, 2)
                register_map[amount] -= 1

                user_change_map[amount] = user_change_map.get(amount, 0) + 1
        
        if change > 0:
            print("No money in register!")

            return "No money in register!"
        '''
        # print(f"-- Final change -- ")

        # for amount in amounts:
        #     if amount >= 1.0:
        #         print(f"Num of ${amount}: {user_change_map.get(amount, 0)}")
        #     elif 0 <= amount < 1.0:
        #         print(f"Num of {amount}¢: {user_change_map.get(amount, 0)}")
        
        replenishRegister(price, register_map) # adds the payment - change to the register
        '''
        
    elif change < 0:
        print("Error! Payment is not sufficient.")

        # user_change_map[-1] = -1
        # user_change_map = {}

    elif change == 0:
        print("No change")
    
    return user_change_map

register = init_curr_map()
user_map = makeChange(5, 187.92, register)

# print(str(currency_map))
print(str(user_map))
    