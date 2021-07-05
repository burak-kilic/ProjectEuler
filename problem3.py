primefactor = []
n = 600851475143
while n % 2 == 0:
    primefactor.append(2)
    n = n / 2

for i in range(3, int(n**0.5) + 1, 2):
    while n % i == 0:
        primefactor.append(i)
        n = n / i

if n > 2:
    primefactor.append(n)

print(max(primefactor))
