print("Pham Viet QUuan 235752021610022")
def sieve_of_eratosthenes(limit):
    is_prime = [True] * (limit + 1)
    p = 2
    while (p * p <= limit):
        if (is_prime[p] == True):
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, limit + 1):
        if is_prime[p]:
            primes.append(p)
    return tuple(primes)  
P = sieve_of_eratosthenes(1000000)
print(f"So luong so nguyen to nho hon 1 trieu: {len(P)}")
print(f"Mot vai so nguyen to: {P[:10]}")
