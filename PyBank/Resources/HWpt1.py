#HOMEWORK PART 1

#total months
import csv
with open('/Users/jarvis/Downloads/NUCHI201902DATA1-master/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)

#total amount
import csv
with open('/Users/jarvis/Downloads/NUCHI201902DATA1-master/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    total_amount = 0
    header = next(csv_reader)
    for row in csv_reader:
        if row not in header:
            total_amount += int(row[1])


#average change
import csv
with open('/Users/jarvis/Downloads/NUCHI201902DATA1-master/Homework/03-Python/Instructions/PyBank/Resources/budget_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    revenue_change = 0
    prev_revenue = 0
    revenue_changes = []
    date_list = []
    header = next(csv_reader)
    for row in csv_reader:
        if row not in header:
            #date
            current_month = str(row[0])
            date_list.append(str(row[0]))
            #revenue
            revenue_change = int(row[1]) - prev_revenue
            prev_revenue = int(row[1])
            revenue_changes.append(revenue_change)
test = "Rich"
#print answers
print('Total Months: ' + str(row_count))
print('Total Amount: ' + str(total_amount))
print("Average Change: " + str(sum(revenue_changes) / len(revenue_changes)))
print(f"Greatest Increase in Profits:  {max(revenue_changes)} on {test}")
print("Greatest Decrease in Profits: " + str(min(revenue_changes)) + ' on [INSERT DATE]')

#write answers to file
with open('/Users/jarvis/Downloads/NUCHI201902DATA1-master/Homework/03-Python/Instructions/PyBank/Resources/Output.txt', "w") as txt_file:
    txt_file.write("Total Months: " + str(row_count))
    txt_file.write("\n")
    txt_file.write("Total Amount: " + str(total_amount))
    txt_file.write("\n")
    txt_file.write("Average Change: " + str(sum(revenue_changes) / len(revenue_changes)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(max(revenue_changes)) + ' on [INSERT DATE]')
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(min(revenue_changes)) + ' on [INSERT DATE]')


