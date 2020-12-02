passwords = open('advent_of_code/day 2/passwords.txt').read().split("\n")
part1, part2 = 0, 0 # counters
for line in passwords:
    line = line.split() # splits the line into three parts
    numbers = line[0].split('-') # splits the numbers into separate parts
    first_num, last_num = int(numbers[0]), int(numbers[1]) # numbers
    letter = line[1][0] # required letter
    pw = line[2] # password string
    letter_count = pw.count(letter) # counts the letter in question

    if letter_count >= first_num and letter_count <= last_num: # part 1
        part1 += 1

    if letter == pw[first_num-1] or letter == pw[last_num-1]: # part 2
        if pw[first_num-1] != pw[last_num-1]:
            part2 += 1

print(part1, part2)
