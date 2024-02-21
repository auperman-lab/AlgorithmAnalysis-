import numpy as np
import time
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from decimal import Decimal, getcontext
import sys


def calculate_execution_time(func, *args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time


def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fibonacci_memoization(n, memo):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoization(n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]


def fibonacci_matrix(n):
    F = np.array([[1, 1], [1, 0]], dtype=object)
    if n == 0:
        return 0
    power(F, n - 1)
    return F[0][0]


def power(F, n):
    if n == 0 or n == 1:
        return
    M = np.array([[1, 1], [1, 0]], dtype=object)
    power(F, n // 2)
    F = np.dot(F, F)
    if n % 2 != 0:
        F = np.dot(F, M)


def fibonacci_binet(n):
    getcontext().prec = 100  # Set precision
    phi = Decimal((1 + Decimal(5).sqrt()) / 2)  # Golden ratio
    return (phi**n - (1 - phi)**n) / Decimal(5).sqrt()


def fastDoubling(n, res):
    if (n == 0):
        res[0] = 0
        res[1] = 1
        return

    fastDoubling((n // 2), res)

    a = res[0]
    b = res[1]
    c = 2 * b - a

    if (c < 0):
        c += MOD

    c = (a * c) % MOD

    d = (a * a + b * b) % MOD

    if (n % 2 == 0):
        res[0] = c
        res[1] = d
    else:
        res[0] = d
        res[1] = c + d


MOD = 1000000007
table = PrettyTable()
memo = {}
sys.setrecursionlimit(10**6)  # Change the value as needed

fib_list = [1, 5, 10, 15, 20, 25, 30, 35]
fib_big_list = [501, 631, 794, 1000, 1259, 1585, 1995, 2512, 3162, 3981, 5012, 6310, 7943, 10000, 12589, 15849, 100000]

execution_func = {'Recursive': fibonacci_recursive, 'Iterative': fibonacci_iterative, 'Memoization': fibonacci_memoization, 'Matrix': fibonacci_matrix, 'Binet': fibonacci_binet, 'fastDoubling': fastDoubling}
execution_times = {'Recursive': [], 'Iterative': [], 'Memoization': [], 'Matrix': [], 'Binet': [], 'fastDoubling': []}

name = 'Memoization'
res = [0] * 2


for n in fib_big_list:
    _, execution_time = calculate_execution_time(execution_func[name], n, memo)
    execution_times[name].append(execution_time)


plt.plot(fib_big_list, execution_times[name], label=name, marker='.')

plt.xlabel('Number in Fibonacci List')
plt.ylabel('Execution Time (seconds)')
plt.title('Execution Time of '+name+' Fibonacci Algorithms')
plt.legend()
plt.show()

table.field_names = ["Number in Fibonacci List", "Execution Time (seconds)"]
for n, execution_time in zip(fib_big_list, execution_times[name]):
    table.add_row([n, execution_time])

# Print the table
print(table)
