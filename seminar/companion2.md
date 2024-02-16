---
layout: default
title: Companion 2
categories: markdown
obsidianshare: "true"
---





<script type="text/javascript" charset="utf-8" 
src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML,
https://vincenttam.github.io/javascripts/MathJaxLocal.js"></script>



# Dynamic Programming - Second Look


# Contents



* TOC 
{:toc}


## Tourism in Manhattan


### Definitions

- $\textbf{Graph}$: $G = (N, E, w)$, where
	- $N$ is a set of Nodes
	- $E$ is a set of Edges
	- $w$ is a function mapping each edge to a weight.
- $\textbf{Node}$: unique element $n \in N$ 
- $\textbf{Edge}$: $e = (u, v)$ where $e \in E$ and $u, v \in N$ 
- Function $w: E \to \mathbb{N}$ (can be implemented in constant time, see [below](https://curolith.github.io/seminar/companion2#constant-function))
- $\textbf{Path}$: Ordered set $P \subset E$ where $\forall e_i = (u_i, v_i) \in P, i > 1, i \in \mathbb{N} \in P: (u_{i} = v_{i-1})$
- $\textbf{Score of a path}$: $\sum_{e \in P} w(e)$
- $\textbf{Max score path}$:  $max\left(\sum_{e \in P} w\left(e\right)\right), P \subset E$

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