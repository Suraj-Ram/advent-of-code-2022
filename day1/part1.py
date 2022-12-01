file = open('input.txt', 'r')
# file1 = open('example.txt', 'r')
lines = file.readlines()

single_elf_total = 0
max_elf = 0

for line in lines:
    if line == "\n":
        if single_elf_total > max_elf:
            max_elf = single_elf_total
        single_elf_total = 0
    else:
        number = int(line)
        single_elf_total += number

print(max_elf)
