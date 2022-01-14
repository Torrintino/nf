#!/usr/bin/python3

parsed_list = []

with open('input.txt') as input_file:
    line = input_file.readline()
    while line:
        line = line.replace("\n", "")
        word, value = line.split(":")
        value = int(value)
        parsed_list.append((word, value))
        line = input_file.readline()
    
parsed_list = sorted(parsed_list, key=lambda x: x[0])
result = sorted(parsed_list, key=lambda x: x[1], reverse=True)

for line in result:
    print("{}:{}".format(line[0], line[1]))
