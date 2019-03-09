#HOMEWORK PART 2

#total votes cast
import csv
with open('./Resources/election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    data = list(csv_reader)
    row_count = len(data)
print(row_count)

import csv
with open("./Resources/election_data.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    row_count = 0
    ballot_names = []
    khan_count = 0
    correy_count = 0 
    li_count = 0
    otooley_count = 0
    vote_list = ["",0]
    for row in csv_reader:
        # print(row)
        if row[2] not in ballot_names:
            ballot_names.append(row[2])
        if row[2] == "Khan":
            khan_count += 1
        if row[2] == "Correy":
            correy_count += 1
        if row[2] == "Li":
            li_count += 1
        if row[2] == "O'Tooley":
            otooley_count += 1
        row_count += 1
    print("Khan", khan_count)
    print("Correy", correy_count)

print("ELECTION RESULTS")
print("--------------------")
print(row_count)
print("--------------------")
print("Khan: " + str(((khan_count/row_count) * 100)) + "% (" + str(khan_count) + ")")
print("Correy: " + str(((correy_count/row_count) * 100)) + "% (" + str(correy_count) + ")")
print("Li: " + str(((li_count/row_count) * 100)) + "% (" + str(li_count) + ")")
print("O'Tooley: " + str(((otooley_count/row_count) * 100)) + "% (" + str(otooley_count) + ")")
print("--------------------")
print("WINNER: KHAN")

with open('./Resources/election_data.csv/Output.txt', "w") as txt_file:
    txt_file.write("ELECTION RESULTS")
    txt_file.write("\n")
    txt_file.write("--------------------")
    txt_file.write("\n")
    txt_file.write("Khan: " + str(((khan_count/row_count) * 100)) + "% (" + str(khan_count) + ")")
    txt_file.write("\n")
    txt_file.write("Correy: " + str(((correy_count/row_count) * 100)) + "% (" + str(correy_count) + ")")
    txt_file.write("\n")
    txt_file.write("Li: " + str(((li_count/row_count) * 100)) + "% (" + str(li_count) + ")")
    txt_file.write("\n")
    txt_file.write("Li: " + str(((li_count/row_count) * 100)) + "% (" + str(li_count) + ")")
    txt_file.write("O'Tooley: " + str(((otooley_count/row_count) * 100)) + "% (" + str(otooley_count) + ")")
    txt_file.write("\n")
    txt_file.write("O'Tooley: " + str(((otooley_count/row_count) * 100)) + "% (" + str(otooley_count) + ")")
    txt_file.write("\n")
    txt_file.write("--------------------")
    txt_file.write("\n")
    txt_file.write("WINNER: KHAN")
    txt_file.write("\n")