# calculates primes

print('up to what number should be checked for primes?')
upperBound = int(input())
count = 0

for i in range(2,upperBound + 1):
    prim = True
    for j in range(2, int(i / 2) + 1):
        if i % j == 0:
            prim = False
        j += 1
    if prim:
        count = count + 1
        print(i)
    i += 1

print(str(count) + ' primes found up to ' + str(upperBound))

