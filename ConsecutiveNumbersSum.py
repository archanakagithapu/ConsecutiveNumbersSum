'''Given an integer n,return the number of ways you can write
n as the sum of consecutive positive integers
i/p:n=5 o/p=2'''
n = int(input())
count = 0
for i in range(1, n+1):
    sum = 0
    for j in range(i, n+1):
        sum += j
        if sum == n:
            count += 1
            break
        elif sum > n:
            break
print(count)
