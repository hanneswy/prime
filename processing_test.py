from multiprocessing import Process, current_process, JoinableQueue
import time
candidateQueue = JoinableQueue()
primes = JoinableQueue()
num_worker_threads = 4
processes = []
upperBound = 100000
primeList = []

# returns true, if given number is a prime, else false
def isPrime(candidate):
    for j in range(2, int(candidate / 2)+1):
        if candidate % j == 0:
            return False
        j += 1
    return True

# worker thread: takes candidates from Queue and checks for primes. puts them in primes Queue if they are
def worker(candidateQueue, primes):
    while True:
        candidate = candidateQueue.get()
        if candidate is None:
            break
        if isPrime(candidate):
            primes.put(candidate)
        candidateQueue.task_done()


# only execute on main process, not on every worker because fork bomb
if __name__ == '__main__':
    print('i am main')
    start = time.time()

    # fill queue
    for item in range(0, upperBound):
        candidateQueue.put(item)
    print('queue filled')


    # start worker threads
    for i in range(num_worker_threads):
        p = Process(target=worker, args=(candidateQueue, primes))
        p.start()
        processes.append(p)

    # block (wait) until all tasks are done
    candidateQueue.join()
    print('queue joined')

    # kill it with fire
    for p in processes:
        p.terminate()

    # dump queue to list to output
    while not primes.empty():
        primeList.append(primes.get())
        primes.task_done()
    #primes.join()
    print(primeList)
    print(str(len(primeList)) + ' primes found up to ' + str(upperBound))
    print(str(round((time.time() - start), 3)) + ' seconds passed')

