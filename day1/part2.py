file1 = open('input.txt', 'r')
# file1 = open('example.txt', 'r')
lines = file1.readlines()

single_elf_total = 0
all_elves_totals_arr = []
max_elf = 0

for line in lines:
    if line == "\n":
        all_elves_totals_arr.append(single_elf_total)
        single_elf_total = 0
    else:
        number = int(line)
        single_elf_total += number


all_elves_totals_arr.sort(reverse=True)
print(all_elves_totals_arr)
print("Answer:")
print(all_elves_totals_arr[0] + all_elves_totals_arr[1]  + all_elves_totals_arr[2])

