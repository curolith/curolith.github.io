

//Tourism in Manhattan: Brute force
max = 0
FOR each possible path
	sum = 0
	FOR each street
		sum = previous sum + 1
	IF sum > max
		max = sum

//Tourism in Manhattan: Greedy algorithm
score = 0
intersection = START
WHILE intersection has 2 outgoing streets
	IF first street has atracktion
		score = previous score + 1
		intersection = intersection at first street
	ELSE
		score = previous score + number of atracktions on second street
		intersection = intersection at second street
WHILE intersection is not STOP
	score = previous score + number of atracktions on only street
	intersection = intersection at only street


//Tourism in Manhattan: Dynamic Algorithm  matrix calculation
FOR each intersection score in matrix
	SET intersection score to 0

ADD START to empty queue
WHILE queue is not empty
	current_intersection = next intersection from queue
	current_score = score of current_intersection in matrix
	FOR each outgoing street
		IF reachable intersection is not in queue
			ADD reacheable intersection to queue
		possible_score = current_score + street atracktions
		IF possible_score > reachable intersection score in matrix
			SET reachable intersection score to possible_score


//Tourism in Manhattan: Dynamic Algorithm  backtracking
REVERSE streets

current_intersection = STOP

WHILE current_intersetion is not START
	IF only one outgoing street
		current_intersection = only outgoing street intersection
	ELSE
		first_score = first outgoing street intersection score in matrix
		second_score = second outgoing street intersection score in matrix
		IF first_score > second_score
			current_intersection = frist outgoing street intersection
		ELSE 
			current_intersection = second outgoing street intersection


//UVA 00507
sum = 0
max = 0
FOR each value in the route
	sum = previous sum + value
	max = maximum of sum and previous max
	IF < 0
		sum = 0