#fib returns the n-th fibonacci number
def fib(n):
    fnum = [0,1]
    for i in range(0,n+1):
        if i+1 <= len(fnum):
            f = fnum[i]
        else:
            f = fnum[0]+fnum[1]
            fnum[0] = fnum[1]
            fnum[1] = f
    return f
