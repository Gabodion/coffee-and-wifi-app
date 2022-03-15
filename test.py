import csv

with open('cafe-data.csv', newline='', encoding="utf-8") as csv_file:
    csv_data = csv.reader(csv_file, delimiter=',')
    list_of_rows = []
    for row in csv_data:
        list_of_rows.append(row)

# print(csv_data.)
print(list_of_rows)
#
# # for  l in range(len(list_of_rows)):
# #     print(list_of_rows[l][l])
# for l in list_of_rows:
#     for n in range(len(l)):
#         print(l[n])

