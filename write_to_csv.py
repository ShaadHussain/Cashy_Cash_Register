
import csv
map = {}
map[1] = -1
map[2] = -2
map[3] = -3


# for mkey in map:
#     print(f"mkey: {mkey}")

with open('map.csv', 'w') as write_file:
    writer = csv.writer(write_file)

    header_row = []
    val_row = []

    for reg_key in map:
        header_row.append(reg_key)
        val_row.append(map[reg_key])

    writer.writerow(header_row)
    writer.writerow(val_row)