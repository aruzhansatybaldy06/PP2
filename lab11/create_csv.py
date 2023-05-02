import csv

# Sample data
data = [
    ['Zhanel', 87772524],
    ['Madina', 87771541],
    ['Aruzhan', 87779578]
]

# Open the CSV file in write mode
with open('book.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    # Write the header row
    writer.writerow(['first_name', 'phone_number'])

    # Write the data rows
    for row in data:
        writer.writerow(row)