numbers = [
	'one',
	'two',
	'three',
	'four',
	'five',
	'six',
	'seven',
	'eight',
	'nine',
]

with open('input01.txt') as file:
	part_one = 0
	part_two = 0 
	for line in file.readlines():
		found_one = []
		found_two = []
		for i, char in enumerate(line):
			if char.isdigit():
				found_one.append(char)
				found_two.append(char)

			else:
				for j, spelled in enumerate(numbers):
					if line[i:].startswith(spelled):
						found_two.append(str(j + 1))
		part_one += int(found_one[0] + found_one[-1]) 
		part_two += int(found_two[0] + found_two[-1])

	print(f"Part one total is: {part_one}")
	print(f"Part two total is: {part_two}")
		

