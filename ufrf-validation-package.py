import json
import numpy as np
import matplotlib.pyplot as plt
import math

PHI = (1 + math.sqrt(5)) / 2

def fib(n):
    return round(PHI**n / math.sqrt(5))

def p_n(n):
    return 14 + 3 * n * (n + 2)

def validate_ufrf(max_pos=100):
    positions = list(range(1, max_pos + 1))
    fib_values = [fib(p) for p in positions]
    is_prime = [all(f % i != 0 for i in range(2, int(math.sqrt(f)) + 1)) if f > 1 else False for f in fib_values]
    harmonic_points = [p_n(i) for i in range(10) if p_n(i) <= max_pos]

    plt.figure(figsize=(10, 6))
    plt.plot(positions, is_prime, label='Prime Indicators', marker='o')
    plt.vlines(harmonic_points, 0, 1, colors='r', label='Harmonic Sync Points')
    plt.title('UFRF Prime Validation Plot')
    plt.xlabel('Fibonacci Position')
    plt.ylabel('Is Prime')
    plt.legend()
    plt.savefig('ufrf_validation_plot.png')
    plt.close()

    report = {
        'validated_positions': max_pos,
        'detected_primes': sum(is_prime),
        'harmonic_points': harmonic_points
    }
    with open('ufrf_report.json', 'w') as f:
        json.dump(report, f, indent=4)
    print('Validation complete. Plot saved as ufrf_validation_plot.png and report as ufrf_report.json')

if __name__ == '__main__':
    validate_ufrf(100)