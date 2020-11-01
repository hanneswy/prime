import threading, queue, time
num_worker_threads = 4
upperBound = 5000
start = time.time()
candidateQueue = queue.Queue()
threads = []
primes = queue.Queue()
primelist = []


# returns true, if given number is a prime, else false
def isPrime(candidate):
    for j in range(2, int(candidate / 2)+1):
        if candidate % j == 0:
            return False
        j += 1
    return True

# worker thread: takes candidates from Queue and checks for primes. puts them in primes Queue if they are
def worker():
    while True:
        candidate = candidateQueue.get()
        if candidate is None:
            break
        if isPrime(candidate):
            primes.put(candidate)
        candidateQueue.task_done()


# start worker threads
for i in range(num_worker_threads):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

# fill queue
for item in range(0, upperBound):
    candidateQueue.put(item)

# block (wait) until all tasks are done
candidateQueue.join()
print('queue joined')

# stop workers
for i in range(num_worker_threads):
    candidateQueue.put(None)
for t in threads:
    t.join()

#print results
while not primes.empty():
    primelist.append(primes.get())
    primes.task_done()
#primes.join()
print(primelist)
print(str(len(primelist)) + ' primes found up to ' + str(upperBound))
print(str(round((time.time()-start), 3)) + ' seconds passed')
