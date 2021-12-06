def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)
if __name__ == "__main__":
    print(fib1(5))
    # print(fib1(20)) # 자신을 21,891번 호출한다.

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}
def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n-1) + fib2(n-2)
    return memo[n]
if __name__ == "__main__":
    print(fib2(20)) # 자신을 39번 호출한다.

from functools import lru_cache
@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n-1) + fib3(n-2)
if __name__ == "__main__":
    print(fib3(20))

def fib4(n: int) -> int:
    if n == 0:
        return 0
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next
if __name__ == "__main__":
    print(fib4(20)) # 반복문이 19번 순회한다.