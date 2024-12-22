from collections import deque

# 递归
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# 动态规划
def fib_dp(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

# 迭代
def fib_iter(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# 队列
def fib_queue(n):
    q = deque([0, 1])
    for _ in range(n-2):
        q.append(q[0] + q[1])
        q.popleft()
    return q[-1]

# 测试
print(fib(10))  # 55
print(fib_dp(10))  # 55
print(fib_iter(10))  # 55
print(fib_queue(10))  # 55