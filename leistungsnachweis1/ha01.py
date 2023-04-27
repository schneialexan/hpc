import multiprocessing
import matplotlib.pyplot as plt
import time

def sum_iterative(n):
    s = 0
    a = [i+1 for i in range(n)]
    for i in range(n):
        s = s + a[i]
    return s

def block_sum(start, end):
    return sum(range(start, end))

def parallel_sum(n, num_blocks=8):
    pool = multiprocessing.Pool(processes=num_blocks)
    block_size = n // num_blocks
    results = [pool.apply_async(block_sum, (i*block_size+1, (i+1)*block_size+1)) for i in range(num_blocks)]
    pool.close()
    pool.join()
    return sum(result.get() for result in results)

def time_function(f, n):
    start = time.time()
    f(n)
    return time.time() - start

# Plot Graph
nums = [10**i for i in range(1, 10)]

print('Iterative calculations:')
start = time.time()
times_iterative = [time_function(sum_iterative, n) for n in nums]
print(f'DONE! Time: {time.time() - start}s')
print('Parallel calculations:')
start = time.time()
times_parallel = [time_function(parallel_sum, n) for n in nums]
print(f'DONE! Time: {time.time() - start}s')

plt.plot(nums, times_iterative, label='Iterative')
plt.plot(nums, times_parallel, label='Parallel')
plt.title('Laufzeitvergleich')
plt.xlabel('n')
plt.ylabel('Time (s)')
plt.legend()
plt.savefig('ha01.png')