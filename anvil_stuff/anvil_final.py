import csv


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

def get_register(file_name = "register.csv"):
    with open('register.csv', mode='r+') as csv_file:
        csv_reader = csv.reader(csv_file)

        line_ct = 0

        amt_num_map = {}

        amounts = []
        amounts_nums = []
        for row in csv_reader:
            if line_ct == 0:
                line_ct += 1

                amounts = list(row)
                amounts = [int(num) for num in amounts]

                print(f"Row 0: {amounts}")


            elif line_ct == 1:
                # amounts_nums = ",".join(row)
                amounts_nums = list(row)

                amounts_nums = [int(num) for num in amounts_nums]

                print(f"Row 1: {amounts_nums}")
                # line_ct += 1


    for i in range(len(amounts)):
        amt_num_map[amounts[i]] = amounts_nums[i]
    
    return amt_num_map

def update_register(register_map):
    with open('register.csv', 'w') as write_file:
        writer = csv.writer(write_file)

        header_row = []
        val_row = []

        for reg_key in register_map:
            header_row.append(reg_key)
            val_row.append(register_map[reg_key])

        writer.writerow(header_row)
        writer.writerow(val_row)

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

        replenishRegister(price) # adds the payment - change to the register

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
    

        

        







