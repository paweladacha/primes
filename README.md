<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML' async></script>
## contents
- pgen.py - prime number generator ([Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes))

## abouts

### pgen.py

Sieve of Eratostenes implementation. Mechanics are based on ["fastest way to list all primes below n" @ stackoverflow](https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n/46635266#46635266). 

#### how it works

Main difference lies in domain, "fabric" from which sieve is cutted out.
Original implementation uses integers greater than 3 not divisible by 2.
It omits half (1/2) of all integers.  

The one above uses two disjoint "fabrics" which are also disjoint from multiples of 2 and 3. It omits `1/2 + 1/3 - 1/6` of all integers which is about 66%.  

As those "fabrics" are more "sparse" the sieve generation is faster, and takes about 3/4 of time consumed by the original implementation.
Although, most of the time is spend solely on generating prime list, by either implementation. This part makes original script, faster that the one above, for `n < 10^6`. Here, also, becouse of use of two distinct "fabrics", at the end need to sort whole output list arises, in order to keep it equivalent with the original one, which is a major drawback of adopted strategy. In opposition, rather counter-intuitively, stands doubled "compress" calls, wich in turn occurs to be faster than, straight like in original.   

#### bottom bound  

Becouse of last, another modification was introduced - ability to bound the out from bottom - which is used in the most time-consuming part, the list generation. This provides large savings in time when not all, but only some large prime numbers are needed. Unfortunatelly memory cost of sieve stays same.  
Whole is contained in only one function for efficiency, though few steps can be taken out to separate functions to enhance explicitness and exceptions/testing/performance measures verbosity.  
Further improvements should be focused on minimizing memory footprint of sieve,
or generating the final prime list. First seems quite doubtful to author but the second one sparks a bit more enthusiasm.  
Sieve creation on the other hand, could be enhanced by starting "making holes" not at first available multiple of prime number but at its square. However such modification had not provided conceivable savings, to orders of magnitude that could have been tested by author.  
