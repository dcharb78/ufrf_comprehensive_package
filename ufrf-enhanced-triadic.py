
"""Enhanced Triadic Interference Prototype
Copyright (c) 2025 Daniel Charbonneau. All rights reserved.

Author : UFRF Team
Date   : 2025-07-10

This script demonstrates how to extend the baseline UFRF implementation with
scale-based triadic interference (per the A/B-test design).
Run directly to compute predicted interference constants for sample scales.
Requires: numpy, math (install via pip).
"""
import math, itertools, numpy as np

PHI = (1 + 5**0.5) / 2
FIB_PRIMES = {2, 3, 5, 13}
PRIMES = [2, 3, 5, 7, 11, 13]

def ticks_to_harmonic(p:int, k:int=1)->float:
    logv = math.log(1.5) if p==1 else math.log(p)
    return p * (logv**0.5) * PHI * k

def n_way_interference(pos:float, primes, n:int=4)->float:
    total = 0.0
    for combo in itertools.combinations(primes, n):
        ticks = sum(ticks_to_harmonic(p) for p in combo)
        phase = 2*math.pi*pos / ticks
        weight = 1 / math.log(math.prod(combo))
        fib_boost = 2 if sum(p in FIB_PRIMES for p in combo)>=n-1 else 1
        total += weight * math.sin(phase) * fib_boost
    return total

if __name__ == '__main__':
    position = 1.75  # Example harmonic position near p=7 cycle
    for order in (4,5):
        amp = n_way_interference(position, PRIMES, n=order)
        print(f"{order}-way interference amplitude ≈ {amp:.6f}")
