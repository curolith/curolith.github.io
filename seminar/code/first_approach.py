def probability_for_color(character, box):
	return box.count(character)/len(box)

def calculate_combination_probability(combination, box):
	probability = 1
	for character in combination:
		probability = probability * probability_for_color(character, box)
	return probability

def find_all_combinations(combination_length):
	combinations = []
	for i in range(0, 2**combination_length):
		binary_suffix = (list(str(bin(i)))[2:])
		#string representations of binary values have 0b in the first two locations		
		binary_prefix = ['0'] * (combination_length - len(binary_suffix))
		binary_representation = binary_prefix + binary_suffix
		combination = map(
			(lambda x : 'r' if x == '1' else 'b'), binary_representation)
		combinations.append(list(combination))
	return combinations



#print(find_all_combinations(5))
#print(list(map(lambda x: calculate_combination_probability(x, ['r', 'b', 'b']), find_all_combinations(5))))