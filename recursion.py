def helper(n):
    print(n)
    if n==0:
        return
    helper(n-1)
helper(5)
