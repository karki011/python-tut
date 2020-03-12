import csv

# how to write in cvs file

# with open("data.cvs", "w") as file:
#     # open writer to write in the file
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_name", "product_price"])
#     writer.writerow([1, "laptop", 39])
#     writer.writerow([2, "mac", 59])

# how to read
with open("data.cvs") as file:
    # open writer to write in the file
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
