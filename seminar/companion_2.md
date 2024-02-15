---
layout: default
title: Companion 2
categories: markdown
share: "true"
---

<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>

# Dynamic Programming - Second Look

* TOC <newline>
{:toc}

## Tourism in Manhattan

### Definitions

$\textbf{Ordered}$: knowledge assumed (important: **ordered $\neq$ sorted**)

$\textbf{Graph}$: Tuple $G = (N, E)$ where $N$ is the set of Nodes (intersections) and $E$ is the set of Edges

$\textbf{Node}$: includes a Set of outward edges

$\textbf{Edge}$: Tuple $(a, b)$ where $a$ and $b$ are connected Nodes

$\textbf{Weighted edge}$: Edge $(a, b, w)$ where $w$ is the weight value

$\textbf{Directed edge}$: Edge $(a, b)$ where $(a, b) \neq (b, a)$ (ordered)

$\textbf{Path}$: List $P$ of Edges $(a_i, b_i)$ where $b_i = a_{i+1}$ 

$\textbf{Score of a path}$: Sum of weights of the edges in its list.


### Pseudocode

#### Brute Force

```java
max = 0
FOR each possible path
	sum = 0
	FOR each street
		sum = previous sum + 1
	IF sum > max
		max = sum
```


#### Greedy

```java
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
```

#### Dynamic

Matrix calculation:
```java
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

```

Backtracking:
```java
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
```

## UVA 000507: Jill rides again

### Pseudocode

#### DYN?
```java
sum = 0
max = 0
FOR each value in the route
	sum = previous sum + value
	max = maximum of sum and previous max
	IF < 0
		sum = 0
```

## Sources

- Abramov, D. (n.d.). What the fuck is memoization? ・ Dan’s JavaScript Glossary. [online] whatthefuck.is. Available at: <https://whatthefuck.is/memoization> [Accessed 8 Dec. 2023].

- Cormen, T.H., Charles Eric Leiserson, Rivest, R.L., Stein, C. and Al, E. (2009). Introduction to algorithms. MIT Press.

- Demaine, E. (2011). Lecture 19: Dynamic Programming I: Fibonacci, Shortest Paths \| Introduction to Algorithms \| Electrical Engineering and Computer Science. [online] MIT OpenCourseWare. Available at: <https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/> [Accessed 8 Dec. 2023].

- Holländer, B. (2020). Understanding Combinatorics: Number of Paths on a Grid. [online] Medium. Available at: <https://towardsdatascience.com/understanding-combinatorics-number-of-paths-on-a-grid-bddf08e28384> [Accessed 8 Dec. 2023].

- OpenAI (2023). DALL·E 3. [online] openai.com. Available at: <https://openai.com/dall-e-3> [Accessed 8 Dec. 2023].

- Schmidt, D. and Schmidt, M. (2022). Algorithmen und Datenstrukturen. [online] Heinrich-Heine-Universität Düsseldorf. Available at: <https://ilias.hhu.de/goto.php?target=file_1567461_download&client_id=UniRZ> [Accessed 8 Dec. 2023]. 

- Skript zur Vorlesung.WikiDiff. (2017). Memorize vs Memoize - What’s the difference? [online] Available at: <https://wikidiff.com/memoize/memorize> [Accessed 8 Dec. 2023].