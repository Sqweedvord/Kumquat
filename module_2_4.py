from collections import defaultdict

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for n in numbers:
    if n < 2:
        continue
    is_prime = True
    for a in range(2, int((n ** 0.5) + 1)):   #k = n ** (1 / 2)
        if n % a == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(n)
    else:
        not_primes.append(n)
is_prime = True
print('Простые числа ', primes)
print('Непростые числа', not_primes)
