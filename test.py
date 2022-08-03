# hmap = {}

# hmap[20.0] = 5

# x = hmap.get(20, 0)


# Testing rounding
# num = 29.399999

# num = round(num, 2)
# print(f"Num: {num}")

# Testing dictReader

import csv

with open('register.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)

    line_ct = 0

    amt_num_map = {}

    amounts = []
    amounts_nums = []
    for row in csv_reader:
        if line_ct == 0:
            line_ct += 1

            # amounts = ",".join(row)
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


    print(str(dict(amt_num_map)))