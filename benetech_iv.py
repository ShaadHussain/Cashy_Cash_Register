currency_map = {}

def init_curr_map():
    global currency_map

    currency_map[0.01] = 200
    currency_map[0.05] = 200
    currency_map[0.1] = 170
    currency_map[0.25] = 170
    currency_map[0.5] = 30
    currency_map[1.0] = 150
    currency_map[5.0] = 100
    currency_map[10.0] = 100
    currency_map[20.0] = 150



# Taking the user's payment (deposit) and allocating it to register
def replenishRegister(deposit):
    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

    deposit = round(deposit, 2)

    for amount in amounts:

            while deposit >= amount:

                print(f"Curr amount: {amount}")
                print(f"Curr deposit before: {deposit}")

                currency_map[amount] += 1

                deposit -= amount

                deposit = round(deposit, 2)

                # replenishing the register by adding to it



def makeChange(price, payment):

    amounts = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

    user_change_map = {}
    change = (payment - price)

    print(f"Change b4 loop: {change}")

    change = round(change, 2)

    if change > 0:

        replenishRegister(price)

        for amount in amounts:

            while change >= amount and currency_map[amount] != 0:

                print(f"Curr amount: {amount}")
                print(f"Curr change before: {change}")

                change -= amount

                change = round(change, 2)
                currency_map[amount] -= 1

                user_change_map[amount] = user_change_map.get(amount, 0) + 1
            

        print(f"-- Final change -- ")

        for amount in amounts:
            if amount >= 1.0:
                print(f"Num of ${amount}: {user_change_map.get(amount, 0)}")
            elif 0 <= amount < 1.0:
                print(f"Num of {amount}¢: {user_change_map.get(amount, 0)}")

        
    elif change < 0:
        print("Error! Payment is not sufficient.")

    elif change == 0:
        print("No change")


init_curr_map()
makeChange(400.33, 400.33)
print(str(currency_map))
    

        

        







