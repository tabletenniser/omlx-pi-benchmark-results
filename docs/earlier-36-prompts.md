# All 36 trial prompts verbatim

The same 36 trials apply to every model; only the repetition seed changes. Common system prompt:

````text
Solve the problem carefully. Give at most two sentences of visible justification, then finish with a line beginning FINAL: and the requested answer.
````

## Trial 01: make24 / repetition 1 / seed 17001

````text
How can you make 24 using 3, 8, 8, 3? Use each number exactly once, with only +, -, *, / and parentheses; no concatenation, exponents or factorials. Finish with FINAL: followed by the arithmetic expression.
````

Expected answer: `"8 / (3 - 8/3)"`

## Trial 02: crt / repetition 1 / seed 17101

````text
Find the smallest nonnegative integer x such that x mod 7 = 3, x mod 11 = 7, and x mod 13 = 9. Finish with FINAL: followed by the integer.
````

Expected answer: `997`

## Trial 03: bayes_coins / repetition 1 / seed 17201

````text
A box contains two fair coins and one double-headed coin. You choose a coin uniformly at random and flip that same coin five times, observing five heads. What is the probability that it is the double-headed coin? Give an exact fraction after FINAL:.
````

Expected answer: `"16/17"`

## Trial 04: pattern_wait / repetition 1 / seed 17301

````text
A fair coin is flipped repeatedly. What is the expected number of flips until HTH appears for the first time as three consecutive flips? Overlapping attempts count. Finish with FINAL: followed by the expected number.
````

Expected answer: `10`

## Trial 05: biased_host / repetition 1 / seed 17401

````text
There are three doors, with a car uniformly placed behind one. You choose door 1. The host knows where the car is and must open an unchosen goat door. Whenever both doors 2 and 3 contain goats, the host always opens door 3. You observe the host opening door 3. What is the probability that the car is behind door 2? Finish with FINAL: followed by an exact fraction.
````

Expected answer: `"1/2"`

## Trial 06: truth_liars / repetition 1 / seed 17501

````text
Each of A, B and C is either a truth-teller, whose statements are true, or a liar, whose statements are false. A says: B is a liar. B says: C is a liar. C says: A and B are both liars. Who are the truth-tellers? Finish with FINAL: followed by a JSON array of their names, such as ["A", "C"].
````

Expected answer: `["B"]`

## Trial 07: factorial_base12 / repetition 1 / seed 17601

````text
How many trailing zero digits does 1000! have when written in base 12? Finish with FINAL: followed by an integer.
````

Expected answer: `497`

## Trial 08: circular_bits / repetition 1 / seed 17701

````text
How many binary strings of length 12 have exactly five 1s and no adjacent 1s, where positions 12 and 1 also count as adjacent? Rotations are distinct strings; do not identify rotations. Finish with FINAL: followed by an integer.
````

Expected answer: `36`

## Trial 09: fixed_points / repetition 1 / seed 17801

````text
How many permutations of the numbers 1 through 8 have exactly two fixed points? A fixed point means that the number i is in position i. Finish with FINAL: followed by an integer.
````

Expected answer: `7420`

## Trial 10: python_aliasing / repetition 1 / seed 17901

````text
Without running it, determine the exact nested list printed by this Python 3 code:

rows = [[0] * 2] * 3
rows[0][1] = 7
rows[1] = rows[1][:]
rows[1][0] = 4
rows[2].append(9)
print(rows)

Finish with FINAL: followed by the nested list as JSON.
````

Expected answer: `[[0, 7, 9], [4, 7], [0, 7, 9]]`

## Trial 11: python_closure_cache / repetition 1 / seed 18001

````text
Without running it, determine the two lists printed by this Python 3 program:

def memoized(seq, memo={}):
    key = tuple(seq)
    if key not in memo:
        memo[key] = [lambda: seq[i] for i in range(len(seq))]
    return memo[key]

a = [1, 2, 3]
f = memoized(a)
a[2] = 9
print([g() for g in f])
print([g() for g in memoized([1, 2, 3])])

Finish with FINAL: followed by a JSON array containing the two printed lists in order.
````

Expected answer: `[[9, 9, 9], [9, 9, 9]]`

## Trial 12: negative_dijkstra / repetition 1 / seed 18101

````text
A directed graph has edges s->a with weight 2, s->b with weight 5, b->a with weight -10, a->t with weight 2, and b->t with weight 10. Consider standard Dijkstra that settles a node only once and stops immediately when t is first removed from the min-priority queue. What distance does that algorithm return for t, what is the true shortest-path distance, and what is a true shortest path? Finish with FINAL: followed by a JSON object with keys dijkstra, shortest, and path (an array of node names).
````

Expected answer: `{"dijkstra": 4, "shortest": -3, "path": ["s", "b", "a", "t"]}`

## Trial 13: make24 / repetition 2 / seed 17002

````text
How can you make 24 using 3, 8, 8, 3? Use each number exactly once, with only +, -, *, / and parentheses; no concatenation, exponents or factorials. Finish with FINAL: followed by the arithmetic expression.
````

Expected answer: `"8 / (3 - 8/3)"`

## Trial 14: crt / repetition 2 / seed 17102

````text
Find the smallest nonnegative integer x such that x mod 7 = 3, x mod 11 = 7, and x mod 13 = 9. Finish with FINAL: followed by the integer.
````

Expected answer: `997`

## Trial 15: bayes_coins / repetition 2 / seed 17202

````text
A box contains two fair coins and one double-headed coin. You choose a coin uniformly at random and flip that same coin five times, observing five heads. What is the probability that it is the double-headed coin? Give an exact fraction after FINAL:.
````

Expected answer: `"16/17"`

## Trial 16: pattern_wait / repetition 2 / seed 17302

````text
A fair coin is flipped repeatedly. What is the expected number of flips until HTH appears for the first time as three consecutive flips? Overlapping attempts count. Finish with FINAL: followed by the expected number.
````

Expected answer: `10`

## Trial 17: biased_host / repetition 2 / seed 17402

````text
There are three doors, with a car uniformly placed behind one. You choose door 1. The host knows where the car is and must open an unchosen goat door. Whenever both doors 2 and 3 contain goats, the host always opens door 3. You observe the host opening door 3. What is the probability that the car is behind door 2? Finish with FINAL: followed by an exact fraction.
````

Expected answer: `"1/2"`

## Trial 18: truth_liars / repetition 2 / seed 17502

````text
Each of A, B and C is either a truth-teller, whose statements are true, or a liar, whose statements are false. A says: B is a liar. B says: C is a liar. C says: A and B are both liars. Who are the truth-tellers? Finish with FINAL: followed by a JSON array of their names, such as ["A", "C"].
````

Expected answer: `["B"]`

## Trial 19: factorial_base12 / repetition 2 / seed 17602

````text
How many trailing zero digits does 1000! have when written in base 12? Finish with FINAL: followed by an integer.
````

Expected answer: `497`

## Trial 20: circular_bits / repetition 2 / seed 17702

````text
How many binary strings of length 12 have exactly five 1s and no adjacent 1s, where positions 12 and 1 also count as adjacent? Rotations are distinct strings; do not identify rotations. Finish with FINAL: followed by an integer.
````

Expected answer: `36`

## Trial 21: fixed_points / repetition 2 / seed 17802

````text
How many permutations of the numbers 1 through 8 have exactly two fixed points? A fixed point means that the number i is in position i. Finish with FINAL: followed by an integer.
````

Expected answer: `7420`

## Trial 22: python_aliasing / repetition 2 / seed 17902

````text
Without running it, determine the exact nested list printed by this Python 3 code:

rows = [[0] * 2] * 3
rows[0][1] = 7
rows[1] = rows[1][:]
rows[1][0] = 4
rows[2].append(9)
print(rows)

Finish with FINAL: followed by the nested list as JSON.
````

Expected answer: `[[0, 7, 9], [4, 7], [0, 7, 9]]`

## Trial 23: python_closure_cache / repetition 2 / seed 18002

````text
Without running it, determine the two lists printed by this Python 3 program:

def memoized(seq, memo={}):
    key = tuple(seq)
    if key not in memo:
        memo[key] = [lambda: seq[i] for i in range(len(seq))]
    return memo[key]

a = [1, 2, 3]
f = memoized(a)
a[2] = 9
print([g() for g in f])
print([g() for g in memoized([1, 2, 3])])

Finish with FINAL: followed by a JSON array containing the two printed lists in order.
````

Expected answer: `[[9, 9, 9], [9, 9, 9]]`

## Trial 24: negative_dijkstra / repetition 2 / seed 18102

````text
A directed graph has edges s->a with weight 2, s->b with weight 5, b->a with weight -10, a->t with weight 2, and b->t with weight 10. Consider standard Dijkstra that settles a node only once and stops immediately when t is first removed from the min-priority queue. What distance does that algorithm return for t, what is the true shortest-path distance, and what is a true shortest path? Finish with FINAL: followed by a JSON object with keys dijkstra, shortest, and path (an array of node names).
````

Expected answer: `{"dijkstra": 4, "shortest": -3, "path": ["s", "b", "a", "t"]}`

## Trial 25: make24 / repetition 3 / seed 17003

````text
How can you make 24 using 3, 8, 8, 3? Use each number exactly once, with only +, -, *, / and parentheses; no concatenation, exponents or factorials. Finish with FINAL: followed by the arithmetic expression.
````

Expected answer: `"8 / (3 - 8/3)"`

## Trial 26: crt / repetition 3 / seed 17103

````text
Find the smallest nonnegative integer x such that x mod 7 = 3, x mod 11 = 7, and x mod 13 = 9. Finish with FINAL: followed by the integer.
````

Expected answer: `997`

## Trial 27: bayes_coins / repetition 3 / seed 17203

````text
A box contains two fair coins and one double-headed coin. You choose a coin uniformly at random and flip that same coin five times, observing five heads. What is the probability that it is the double-headed coin? Give an exact fraction after FINAL:.
````

Expected answer: `"16/17"`

## Trial 28: pattern_wait / repetition 3 / seed 17303

````text
A fair coin is flipped repeatedly. What is the expected number of flips until HTH appears for the first time as three consecutive flips? Overlapping attempts count. Finish with FINAL: followed by the expected number.
````

Expected answer: `10`

## Trial 29: biased_host / repetition 3 / seed 17403

````text
There are three doors, with a car uniformly placed behind one. You choose door 1. The host knows where the car is and must open an unchosen goat door. Whenever both doors 2 and 3 contain goats, the host always opens door 3. You observe the host opening door 3. What is the probability that the car is behind door 2? Finish with FINAL: followed by an exact fraction.
````

Expected answer: `"1/2"`

## Trial 30: truth_liars / repetition 3 / seed 17503

````text
Each of A, B and C is either a truth-teller, whose statements are true, or a liar, whose statements are false. A says: B is a liar. B says: C is a liar. C says: A and B are both liars. Who are the truth-tellers? Finish with FINAL: followed by a JSON array of their names, such as ["A", "C"].
````

Expected answer: `["B"]`

## Trial 31: factorial_base12 / repetition 3 / seed 17603

````text
How many trailing zero digits does 1000! have when written in base 12? Finish with FINAL: followed by an integer.
````

Expected answer: `497`

## Trial 32: circular_bits / repetition 3 / seed 17703

````text
How many binary strings of length 12 have exactly five 1s and no adjacent 1s, where positions 12 and 1 also count as adjacent? Rotations are distinct strings; do not identify rotations. Finish with FINAL: followed by an integer.
````

Expected answer: `36`

## Trial 33: fixed_points / repetition 3 / seed 17803

````text
How many permutations of the numbers 1 through 8 have exactly two fixed points? A fixed point means that the number i is in position i. Finish with FINAL: followed by an integer.
````

Expected answer: `7420`

## Trial 34: python_aliasing / repetition 3 / seed 17903

````text
Without running it, determine the exact nested list printed by this Python 3 code:

rows = [[0] * 2] * 3
rows[0][1] = 7
rows[1] = rows[1][:]
rows[1][0] = 4
rows[2].append(9)
print(rows)

Finish with FINAL: followed by the nested list as JSON.
````

Expected answer: `[[0, 7, 9], [4, 7], [0, 7, 9]]`

## Trial 35: python_closure_cache / repetition 3 / seed 18003

````text
Without running it, determine the two lists printed by this Python 3 program:

def memoized(seq, memo={}):
    key = tuple(seq)
    if key not in memo:
        memo[key] = [lambda: seq[i] for i in range(len(seq))]
    return memo[key]

a = [1, 2, 3]
f = memoized(a)
a[2] = 9
print([g() for g in f])
print([g() for g in memoized([1, 2, 3])])

Finish with FINAL: followed by a JSON array containing the two printed lists in order.
````

Expected answer: `[[9, 9, 9], [9, 9, 9]]`

## Trial 36: negative_dijkstra / repetition 3 / seed 18103

````text
A directed graph has edges s->a with weight 2, s->b with weight 5, b->a with weight -10, a->t with weight 2, and b->t with weight 10. Consider standard Dijkstra that settles a node only once and stops immediately when t is first removed from the min-priority queue. What distance does that algorithm return for t, what is the true shortest-path distance, and what is a true shortest path? Finish with FINAL: followed by a JSON object with keys dijkstra, shortest, and path (an array of node names).
````

Expected answer: `{"dijkstra": 4, "shortest": -3, "path": ["s", "b", "a", "t"]}`

