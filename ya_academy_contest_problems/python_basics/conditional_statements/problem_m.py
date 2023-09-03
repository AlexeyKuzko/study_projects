elf_number = input("")
gnome_number = input("")
human_number = input("")

common_digit = ""

for i in range(2):
    if elf_number[i] == gnome_number[i] == human_number[i]:
        common_digit = elf_number[i]
        break
print(common_digit)
