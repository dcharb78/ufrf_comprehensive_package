"""
UFRF Quick Test Script
Performs basic sanity checks on key UFRF concepts.
"""

import math

PHI = (1 + math.sqrt(5)) / 2

def is_fib_prime(n):
    # Simple check for small Fibonacci primes
    fib = round(PHI**n / math.sqrt(5))
    return fib > 1 and all(fib % i != 0 for i in range(2, int(math.sqrt(fib)) + 1))

print('Quick Test: Known Fibonacci Prime Positions')
positions = [3, 4, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 83, 89, 97, 101]
for pos in positions[:5]:  # Check first 5
    print(f'Position {pos}: Is prime? {is_fib_prime(pos)}')
print('Test passed if all True for known positions.')