# calculates primes
import time, sys


# returns true, if given number is a prime, else false
def isPrime(candidate):
    for j in range(2, int(candidate / 2)+1):
        if candidate % j == 0:
            return False
        j += 1
    return True


print('up to what number should be checked for primes?')
try:
    upperBound = 50000 #int(input())
except:
    print('error')
    sys.exit()
primes =[]
start = time.time()

for i in range(2,upperBound + 1):
    if isPrime(i):
        primes += [i]
    i += 1

print(primes)
print(str(len(primes)) + ' primes found up to ' + str(upperBound))
print(str(round((time.time()-start), 3)) + ' seconds passed')

