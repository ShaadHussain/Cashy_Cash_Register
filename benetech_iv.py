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

def makeChange(price, payment):

    curr_arr = [20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]

    user_change_map = {}
    change = (payment - price)
    if change > 0:
        
        while change >= 20.0 and currency_map[20.0] != 0:


            change -= 20.0
            currency_map[20.0] -= 1

            user_change_map[20.0] = user_change_map.get(20.0, 0) + 1

        
        while change >= 10.0 and currency_map[10.0] != 0:

            change -= 10.0
            currency_map[10.0] -= 1

            user_change_map[10.0] = user_change_map.get(10.0, 0) + 1


        while change >= 5.0 and currency_map[5.0] != 0:

            change -= 5.0
            currency_map[5.0] -= 1

            user_change_map[5.0] = user_change_map.get(5.0, 0) + 1

        
        while change >= 1.0 and currency_map[1.0] != 0:

            change -= 1.0
            currency_map[1.0] -= 1

            user_change_map[1.0] = user_change_map.get(1.0, 0) + 1

        
        while change >= 0.5 and currency_map[0.5] != 0:

            change -= 0.5
            currency_map[0.5] -= 1

            user_change_map[0.5] = user_change_map.get(0.5, 0) + 1

        
        while change >= 0.25 and currency_map[0.25] != 0:

            change -= 0.25
            currency_map[0.25] -= 1

            user_change_map[0.25] = user_change_map.get(0.25, 0) + 1


        while change >= 0.1 and currency_map[0.1] != 0:

            change -= 0.1
            currency_map[0.1] -= 1

            user_change_map[0.1] = user_change_map.get(0.1, 0) + 1


        while change >= 0.05 and currency_map[0.05] != 0:

            change -= 0.05
            currency_map[0.05] -= 1

            user_change_map[0.05] = user_change_map.get(0.05, 0) + 1

        
        while change >= 0.01 and currency_map[0.01] != 0:

            change -= 0.01
            currency_map[0.01] -= 1

            user_change_map[0.01] = user_change_map.get(0.01, 0) + 1

        
        print(f"-- Final change -- ")
        
    elif change < 0:
        print("Error! Payment is not sufficient.")

    

        

        







