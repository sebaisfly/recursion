from functools import lru_cache
from linecache import cache


# def fibonacci(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 1
#     elif n>2:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for i in range (1,200):
#     print(i, ":", fibonacci(i))

# cache = {}
#
# value=0
#
# def fib2(n):
#     if n in cache:
#         return cache[n]
#     if n==1 or n==2:
#         value=1
#     # elif n == 2:
#     #     value = 1
#     elif n>2:
#         value =fib2(n-1) + fib2(n-2)
#
#     cache[n]=value
#
#     return value

# for i in range(1,500):
#     print(i,":", fib(i))


# @lru_cache(maxsize=1000)
# def fib3(n):
#     if n==1 or n==2:
#         return 1
#     elif n>2:
#         return fib3(n-1) + fib3(n-2)
#
# for i in range(1,20579):
#     print(i, ":" , fib3(i))

def TowerOfHanoi(n,source, destination_rod, auxillary_rod):

    if n==1:
        print("Move disk 1 from source ", source, "to destination rod",destination_rod)
        return

    TowerOfHanoi(n-1,source,auxillary_rod,destination_rod)
    print("Move disk ",n,"from source ", source, "to destination rod",destination_rod)
    TowerOfHanoi(n-1,source,auxillary_rod,destination_rod)


n=4
TowerOfHanoi(n, "a", "b", "c")
