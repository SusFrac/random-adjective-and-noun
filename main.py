import random

file_a = 'a.txt'
file_b = 'b.txt'


lines_from_a = []
lines_from_b = []


with open(file_a, 'r') as file:
    for line in file:
        lines_from_a.append(line.strip())


with open(file_b, 'r') as file:
    for line in file:
        lines_from_b.append(line.strip())


num_entries_in_a = len(lines_from_a)
num_entries_in_b = len(lines_from_b)


a = input('How much do you want to generate: ')
for i in range(int(a)):
    random_a = random.randint(0, num_entries_in_a)
    random_b = random.randint(0, num_entries_in_b)
    print(lines_from_a[random_a]+' '+lines_from_b[random_b])