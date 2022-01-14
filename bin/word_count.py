#!/usr/bin/python3

word_count = {}

with open('input.txt') as input_file:
    word = input_file.readline()
    while word:
        word = word.replace('\n', '')
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
        word = input_file.readline()

for k, v in word_count.items():
    print("{}:{}".format(k, v))
