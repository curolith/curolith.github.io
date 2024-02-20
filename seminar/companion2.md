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

- - -

# Manhattan tourist problem

### Definitions 

- $\textbf{Graph}$: $G = (N, E, w)$, where  
	- $N$ is a set of Nodes $(i, j)$  
	- $E$ is a set of Edges $(a, b)$ with according to the rules:  
		$m$ being either one column to the right of $a$:  
			$b = (i_a, \space j_a+1)$   
		or one row below $n$:  
			$b = (i_a + 1, \space j_a)$  
	- $w$ is a function mapping each edge to a weight. (number of attractions)  
- $\textbf{Node}$: $a = (i, j) \in N$  
- $\textbf{Edge}$: $e = (a, b) \in E$, where $a, b \in N$   
- $\textbf{Weight function}$ $w: E \to \mathbb{N}, w((a, b)) = w(((i_{a}, j_{a}), (i_{b}, j_{b})))$, where $a, b \in N$  
	(can be implemented in constant time, see [below](https://curolith.github.io/seminar/companion2#constant-time-weight-function))  
- $\textbf{Path}$: Sequence $P \subset E$ where $\forall a, b \in P, \space a = P_i, \space b = P_{i+1}$:   
		$b$ is either one column to the right of $a$:  
			$b = (i_a, \space j_a+1)$   
		or one row below $a$:  
			$b = (i_a + 1, \space j_a)$  
	- $P_{1}=(0,0)$ (start is top left)  
	- $P_{max} = (i_{max}, j_{max})$  (stop is bottom right)  
- $\textbf{Score of a path}$: Function $s: P \rightarrow \mathbb{N}, \space s(P) = \sum_{e \in P} w(e)$  
- $\textbf{Max score path}$: Path $P \subset E : s(P) = max(s(Q))$, where $Q$ is any Path in $E$   
	- sub**set**, meaning there can be multiple maximising paths with equal scores  
	- Problem: find one of these maximising pahts  

### Constant time weight function

To give an example of how the weight function can be implemented with constant time, consider the Graph
- $G = (N, E, w)$
- $N = {1, 2, 3}$
- $E = {(1, 2), (1, 3), (2, 3)}$  

with the edge weights
- $w(1, 2)=0$  
- $w(1,3)=1$  
- $w(2,3)=1$

assume the weights are stored in a two dimensional array:
```python
#for demonstration, this is actual python code:

weights = [#   from:
		   #1  2  3    to:
		   [0, 0, 0],#  1
		   [0, 0, 1],#  2
		   [0, 1, 0],#  3
]

def w(u, v):
	return weights[v][w]
#   note that v and w are inverted because of the
#   subarray access order.
```

### Maxima Matrix
- $\textbf{Maxima matrix}$: Matrix for each graph node, holding max node path
	- Per definition: Origin of a path can only be the node above or to the left of the inspected node for any $n = (i, j), \space i, j > 0$
	- $\Rightarrow$Maximum score of a Path at $n$ is either   
		- max score of the entry above plus the weight of the edge to the inspected node  
		- max score of the entry to the left plus the weight of the edge to the inspected node  
	- $\Rightarrow$Maxima matrix: 
		$M: m_{i,j} =$  
		$\max \begin{cases} m_{i-1,j} + w((i-1, j), (i, j)), & \text{if } i > 0 \\ m_{i,j-1} + w((i, j-1), (i, j)), & \text{if } j > 0 \end{cases}$  
		were $m_{i,j} = 0$ if $i = 0$ or $j = 0$  

#### Proof

- $\textbf{Diagonal:}$ set of entries $mm_{i, j} \in M$, so that $i + j = k$  
- Assumption:   
	$m_{i-1, j}$ and $m_{i, j-1}$ are calculated for all $m_{i, j},$ where $i+j = k$  
	
- Base step:  
	$k = 2$:     
	$m_{1, 1}, \space 1 + 1 = 2$    
	$m_{1, 0} = 0$ by definition  
	$m_{0, 1} = 0$ by definition  
	*Assumption holds true* 

- Induction step:  
	$k = k+1$:  
	$m_{i, j}, \space i + j = k + 1$  
	$k + 1 = i + j$  
	- $\Leftrightarrow k = (i-1) +  j$ :  
		$m_{i-1, j}$ which by induction assumption is already calculated  
	- $\Leftrightarrow k = i + (j-1)$ :  
		$m_{i, j-1}$ which by induction assumption is already calculated  
	Assumption holds true:  
	$\Rightarrow$ for $k+1$, all entries $m_{i-1, j}$ and $m_{i, j-1}$ are calculated for all $m_{i,j}$   where $i + j = k + 1$  

$\Rightarrow$By calculating the entries of the matrix in diagonals as shown, we calculate the maximum score for a path passing through the equivalent node.  

### Backtracking
After matrix calculation:  
$m_{n, n} = max(s(Q))$ (Maximum score possible for a path through graph)  

considering the definition:  
		$M: m_{i,j} =$  
		$\max \begin{cases} m_{i-1,j} + w((i-1, j), (i, j)), & \text{if } i > 0 \\ m_{i,j-1} + w((i, j-1), (i, j)), & \text{if } j > 0 \end{cases}$  
		were $m_{i,j} = 0$ if $i = 0$ or $j = 0$  

At least one of the two nodes above or to the left has to be the origin of the score:  
- $p_{max} = m_{n,n}$  
- $p_{k-1} = (i, j) : m_{i_{k},j_{k}} - w((i, j), (i_{k}, j_{k})) = m_{i, j}$  

## Pseudocode

### Greedy

```python
n = ...
max_path = [(1, 1)]
max_score = 0
i, j = 1

while not (i, j is n):
	#if j at border or i direction has bigger weight:
	 if j = n or w((i, j), (i+1, j)) > w((i, j), (i, j+1)):
		i = i+1
		max_score = max_score + w((i, j), (i+1, j))
	else:
		j = j+1
		max_score = max_score + w((i,j), (i,j+1))
	max_path.append((i, j)) #new calculated values
```
-  either $i$ or $j$ increment each iteration until they are $n$
 - $\Rightarrow$ Runtime: $2n \in \mathcal{O}(n)$


### Dynamic
#### Matrix calculation


```python
M = [
		 [0 … 0]
		 … 
		 [0 … 0] 
	]

for k = 1 … n:
	for i = 1 … k, j = k … 1: #diagonal iteration
		M[i,j] = max(
			M[i-1,j] + w((i-1, j), (i, j)), 
			M[i,j-1] + w((i, j-1), (i, j))
		)
``` 
since matrix is iterated over exactly once: $\mathcal{O}(n^2)$  

#### Backtracking

```python
M = ...
n = ...
i = n
j = n
path = [(n, n)]

while (i, j) not (1, 1):
	if M[i, j] - w((i-1, j), (i, j)) is M[i-1, j]:
		#i-1, j is possible origin
		i = i-1
	else: #one has to be the origin per definition, no check needed
		j = j-1
	path.prepend(i, j) #add to left end of path
```
-  either $i$ or $j$ decrement each iteration until they are $1$  
 - $\Rightarrow$ Runtime: $2n \in \mathcal{O}(n^{2})$  

# UVA 00507: Jill rides again

## Definitions
- $\textbf{Array}$:   
	Sequence $A = [x_{1}, ... , x_{n}]$  
- $\textbf{Subarray}$:  
	Sequence $S = [x_{i}, ... x_{j}] \in A$  
- $\textbf{Maximum subarray of A}$:  
	$S_{max}$ = $S \in A: max\left(\sum\limits x \textbf{, } x \in S\right)$  
- $\textbf{Helper array for A}$: (iteration current sum)  
	Sequence $H = [h_{1}, ... ,h_{n}]$:  
	$h_{1} = x_{1}$  
	for $i > 1$:  
	$h_{i} = \begin{cases} h_{i-1} + x_{i} & \text{ if } & h_{i-1} + x_{i} > 0 \\ 0 & \text{ if } & h_{i-1} + x_{i} \leq 0 \end{cases}$  
- $\textbf{Maximum subarray sum array of A}:$  (iteration max sum)  
	Sequence $M$ = $[m_{1}, ... , m_{n}]$:   
	$m_{1}= h_1$  
	for $i > 1$:  
	$m_{i} = max(m_{i-1}, \space h_{i})$  


## Pseudocode
```python
A = [...]
sum = 0
max_sum = 0
c_left = 0
m_left = 0 #max
m_right = 0 #max

for i = 1 ... n: #one dependency on n -> O(n)
	sum = sum + A[i]
	if sum > max_sum:
		max_sum = sum
		m_left = c_left
		m_right = i
	if sum < 0:
		sum = 0
		c_left = i
```

#### Example

| position:      | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| -------------- | --- | --- | --- | --- | --- | --- | --- |
| item:          | 1   | -2  | 3   | -2  | 10  | -14 | 10  |
| sum:           | 1   | 0   | 3   | 1   | 11  | 0   | 10  |
| max sum:       | 1   | 1   | 3   | 3   | 11  | 11  | 11  |
| current left:  | 1    | 1    | 3    | 3    | 3    | 3    | 7    |
| current right: | 1    | 2    | 3    | 4    | 5    | 6    | 7    |
| max left:      | 1    | 1    | 3    | 3    | 3    | 3    | 3    |
| max right:               | 1    | 1    | 3    | 4    | 5    | 5    | 5    |


## Sources

- [Seminar ILIAS website](https://ilias.hhu.de/ilias.php?ref_id=1529360&cmdClass=ilrepositorygui&cmdNode=y8&baseClass=ilrepositorygui) : provided resources/instructions

- Abramov, D. (n.d.). _What the fuck is memoization? ・ Dan’s JavaScript Glossary_. [online] whatthefuck.is. Available at: https://whatthefuck.is/memoization [Accessed 8 Dec. 2023].

- Cormen, T.H., Charles Eric Leiserson, Rivest, R.L., Stein, C. and Al, E. (2009). _Introduction to algorithms_. MIT Press.

- Demaine, E. (2011). _Lecture 19: Dynamic Programming I: Fibonacci, Shortest Paths - Introduction to Algorithms - Electrical Engineering and Computer Science_. [online] MIT OpenCourseWare. Available at: https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-fall-2011/resources/lecture-19-dynamic-programming-i-fibonacci-shortest-paths/ [Accessed 8 Dec. 2023].

- Holländer, B. (2020). _Understanding Combinatorics: Number of Paths on a Grid_. [online] Medium. Available at: https://towardsdatascience.com/understanding-combinatorics-number-of-paths-on-a-grid-bddf08e28384 [Accessed 8 Dec. 2023].

- OpenAI (2023). _DALL·E 3_. [online] openai.com. Available at: https://openai.com/dall-e-3 [Accessed 8 Dec. 2023].

- Schmidt, D. and Schmidt, M. (2022). _Algorithmen und Datenstrukturen_. [online] Heinrich-Heine-Universität Düsseldorf. Available at: https://ilias.hhu.de/goto.php?target=file_1567461_download&client_id=UniRZ [Accessed 8 Dec. 2023]. Skript zur Vorlesung.

- WikiDiff. (2017). _Memorize vs Memoize - What’s the difference?_ [online] Available at: https://wikidiff.com/memoize/memorize [Accessed 8 Dec. 2023].

