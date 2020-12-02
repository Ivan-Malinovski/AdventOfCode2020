passwords = open('advent_of_code/day 2/passwords.txt').read().split("\n")
part1, part2 = 0, 0
for line in passwords:
    line = line.split()
    numbers = line[0].split('-')
    first_num, last_num = int(numbers[0]), int(numbers[1])
    letter = line[1][0]
    password = line[2]
    letter_count = password.count(letter)

    if letter_count >= first_num and letter_count <= last_num: # part 1
        part1 += 1

    if letter == password[first_num-1] or letter == password[last_num-1]: # part 2
        if password[first_num-1] != password[last_num-1]:
            part2 += 1

print(part1, part2)
