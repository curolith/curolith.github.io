def probability_for_color(character, box):
	return box.count(character)/len(box)

def calculate_recursively(combination, box, probability, comb_max):
    if (len(combination) == comb_max):
        return(str(list(combination)) + " : " + str(probability) + "\n")
    
    return (calculate_recursively(combination + 'b', 
                        box,
                        probability * probability_for_color('b', box),
                        comb_max)
    +
    calculate_recursively(combination + 'r', 
                          box,
                          probability * probability_for_color('r', box),
                          comb_max))


#calculate_recursively("", box=['r', 'b', 'b'], probability=1, comb_max=5)