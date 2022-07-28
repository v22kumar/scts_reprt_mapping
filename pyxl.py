with open("output.csv", 'r') as in_file:
    in_file_data = in_file.readlines()


for line in in_file_data:
    print(line)