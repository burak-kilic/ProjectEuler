a = 1
b = 1
fibonacci = [1]
for i in range(31):
    a, b = b, a + b
    fibonacci.append(b)

sum = 0
for number in fibonacci:
    if number % 2 == 0:
        sum += number

print(sum)
