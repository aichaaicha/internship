The idea is to go through the pyramid from the bottom to the top
Let's take the example we have:

1

8   4

2  6  9

8  5  9  3

the first thing I did was to replace all the primes with -infinity, OUR pyramid becomes:

1

8  4

-inf  6  9

8  -inf  9  -inf

we won't touch the base of the pyramid, so we keep 

8  -inf  9  -inf 

THEN, we take the node 9 which is in the 3 rd line, it has three possible paths, that is -inf 9 -inf , we take the maximum element of these 3 and we add it with the node 9, we do the same thing for the 6 to which we add 9 which is the max of 8 -inf 9 AND FINALLY THE SAME FOR -inf which we will add to 8 which is the max of 8 -inf.
The 3rd line of the pyramid becomes:

-inf  15  18 

similarly for 4 which will take the value 4+max(18,15) and 8 which will take the value 8+max(-inf,15)
the second line becomes:
23 22 and we do the same for 1 which will take the value 24
our pyramid becomes:

24

23  22

-inf  15  18

8  -inf  9  -inf

the maximum value is located at the top of the pyramid: 24
There is a case that caused me problem is when all the lines of the pyramid are prime, in this case this algorithm will give in the top of the pyramid the infinite value, the solution that I proposed is to go through the pyramid and look for the line that contains only prime numbers, and so in the second path of the pyramid from the bottom to the top, I started from this line and it solved the problem.
